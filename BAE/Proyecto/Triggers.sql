USE ComplejoDeportivo;

DELIMITER $$    

-- ============================================================
-- PROCEDIMIENTOS
-- ============================================================

-- PROCEDIMIENTO 1: InformeSocios
-- Muestra los socios que han hecho más de X reservas en el
-- último mes. También devuelve cuántos son en total (OUT).
--
-- Ejemplo: CALL InformeSocios(2, @total); SELECT @total;
DROP PROCEDURE IF EXISTS InformeSocios$$
CREATE PROCEDURE InformeSocios(
    IN  p_minReservas INT,
    OUT p_total       INT
)
BEGIN
    -- Lista de socios que superan el mínimo
    SELECT
        s.DNI,
        CONCAT(s.Nombre, ' ', s.Apellidos) AS Socio,
        COUNT(r.IDReserva)                 AS NumReservas
    FROM Socios s
    JOIN Reservas r ON s.DNI = r.DNISocio
    WHERE r.FechaReserva >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
    GROUP BY s.DNI, s.Nombre, s.Apellidos
    HAVING NumReservas > p_minReservas
    ORDER BY NumReservas DESC;

    -- Cuántos socios cumplen la condición
    SELECT COUNT(*) INTO p_total
    FROM (
        SELECT s.DNI
        FROM Socios s
        JOIN Reservas r ON s.DNI = r.DNISocio
        WHERE r.FechaReserva >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
        GROUP BY s.DNI
        HAVING COUNT(r.IDReserva) > p_minReservas
    ) sub;
END$$


-- PROCEDIMIENTO 2: ResumenClasesPorInstructor
-- Muestra las clases de un instructor en un mes y año dados.
-- También devuelve cuántas clases son en total (OUT).
--
-- Ejemplo: CALL ResumenClasesPorInstructor('12345678A', 4, 2026, @total);
--          SELECT @total;
DROP PROCEDURE IF EXISTS ResumenClasesPorInstructor$$
CREATE PROCEDURE ResumenClasesPorInstructor(
    IN  p_dniInstructor VARCHAR(9),
    IN  p_mes           INT,
    IN  p_anio          INT,
    OUT p_totalClases   INT
)
BEGIN
    SELECT
        c.IDClase,
        c.NombreClase,
        c.FechaClase,
        c.HoraInicio,
        c.HoraFin,
        COUNT(a.DNISocio) AS Asistentes
    FROM Clases c
    LEFT JOIN AsistenciasClase a ON c.IDClase = a.IDClase
    WHERE c.DNIInstructor     = p_dniInstructor
      AND MONTH(c.FechaClase) = p_mes
      AND YEAR(c.FechaClase)  = p_anio
    GROUP BY c.IDClase, c.NombreClase, c.FechaClase, c.HoraInicio, c.HoraFin
    ORDER BY c.FechaClase;

    SELECT COUNT(*) INTO p_totalClases
    FROM Clases
    WHERE DNIInstructor     = p_dniInstructor
      AND MONTH(FechaClase) = p_mes
      AND YEAR(FechaClase)  = p_anio;
END$$


-- PROCEDIMIENTO 3: AsignarReservasMasivas
-- Recibe una lista de DNIs separados por comas y crea una
-- reserva para cada uno, solo si no hay conflicto de horario.
--
-- Ejemplo:
--   CALL AsignarReservasMasivas(1, '2026-06-15', '09:00', '10:00', '64350807C,47093353Z');
DROP PROCEDURE IF EXISTS AsignarReservasMasivas$$
CREATE PROCEDURE AsignarReservasMasivas(
    IN p_idInstalacion INT,
    IN p_fecha         DATE,
    IN p_horaInicio    TIME,
    IN p_horaFin       TIME,
    IN p_listaDNIs     TEXT
)
BEGIN
    DECLARE v_dni    VARCHAR(9);
    DECLARE v_cuenta INT;
    DECLARE v_pos    INT DEFAULT 1;
    DECLARE v_token  VARCHAR(20);

    -- Añadimos coma al final para que el bucle funcione con el último DNI
    SET p_listaDNIs = CONCAT(TRIM(p_listaDNIs), ',');

    WHILE v_pos <= CHAR_LENGTH(p_listaDNIs) DO

        -- Sacamos el siguiente DNI de la cadena
        SET v_token = TRIM(SUBSTRING_INDEX(SUBSTRING(p_listaDNIs, v_pos), ',', 1));
        SET v_pos   = v_pos + CHAR_LENGTH(v_token) + 1;

        IF v_token != '' THEN
            SET v_dni = v_token;

            -- Comprobamos si hay solapamiento
            SELECT COUNT(*) INTO v_cuenta
            FROM Reservas
            WHERE IDInstalacion = p_idInstalacion
              AND FechaReserva  = p_fecha
              AND HoraInicio    < p_horaFin
              AND HoraFin       > p_horaInicio;

            IF v_cuenta = 0 THEN
                INSERT INTO Reservas (DNISocio, IDInstalacion, FechaReserva, HoraInicio, HoraFin)
                VALUES (v_dni, p_idInstalacion, p_fecha, p_horaInicio, p_horaFin);
                SELECT CONCAT('Reserva creada para: ', v_dni) AS Resultado;
            ELSE
                SELECT CONCAT('Conflicto de horario para: ', v_dni) AS Resultado;
            END IF;
        END IF;

    END WHILE;
END$$


-- ============================================================
-- FUNCIONES
-- ============================================================

-- FUNCIÓN 1: PromedioReservasPorSocio
-- Calcula el promedio de reservas de los socios que tienen
-- al menos la edad mínima indicada.
--
-- Ejemplo: SELECT PromedioReservasPorSocio(18);
DROP FUNCTION IF EXISTS PromedioReservasPorSocio$$
CREATE FUNCTION PromedioReservasPorSocio(p_edadMinima INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE v_promedio DECIMAL(10,2);

    SELECT IFNULL(AVG(conteo), 0) INTO v_promedio
    FROM (
        SELECT COUNT(r.IDReserva) AS conteo
        FROM Socios s
        LEFT JOIN Reservas r ON s.DNI = r.DNISocio
        WHERE TIMESTAMPDIFF(YEAR, s.FechaNacimiento, CURDATE()) >= p_edadMinima
        GROUP BY s.DNI
    ) sub;

    RETURN v_promedio;
END$$


-- FUNCIÓN 2: DisponibilidadInstalacion
-- Devuelve cuántas franjas de 1 hora (de 08:00 a 20:00)
-- están libres para una instalación en una fecha concreta.
-- En total hay 12 franjas posibles.
--
-- Ejemplo: SELECT DisponibilidadInstalacion(1, '2026-06-01');
DROP FUNCTION IF EXISTS DisponibilidadInstalacion$$
CREATE FUNCTION DisponibilidadInstalacion(
    p_idInstalacion INT,
    p_fecha         DATE
)
RETURNS INT
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE v_hora        TIME DEFAULT '08:00:00';
    DECLARE v_horaFin     TIME;
    DECLARE v_disponibles INT  DEFAULT 0;
    DECLARE v_ocupada     INT;

    WHILE v_hora < '20:00:00' DO
        SET v_horaFin = ADDTIME(v_hora, '01:00:00');

        SELECT COUNT(*) INTO v_ocupada
        FROM Reservas
        WHERE IDInstalacion = p_idInstalacion
          AND FechaReserva  = p_fecha
          AND HoraInicio    < v_horaFin
          AND HoraFin       > v_hora;

        IF v_ocupada = 0 THEN
            SET v_disponibles = v_disponibles + 1;
        END IF;

        SET v_hora = v_horaFin;
    END WHILE;

    RETURN v_disponibles;
END$$

DELIMITER ;
