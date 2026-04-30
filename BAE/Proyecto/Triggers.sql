-- ============================================================
--  PROYECTO 4 – COMPLEJO DEPORTIVO
--  Bases de Datos | UT7 Programación BD
--  Alumno: ___________________
--
--  Script adaptado al esquema real de PR4_BD_Complejo_Deportivo.sql
--  Ejecutar sobre la BD: ComplejoDeportivo
-- ============================================================

USE ComplejoDeportivo;

DELIMITER $$

-- ============================================================
--  TRIGGERS
-- ============================================================

-- ------------------------------------------------------------
-- TRIGGER 1a – BEFORE INSERT en Reservas
-- Verifica que no haya solapamiento de horario para la misma
-- instalación y fecha antes de insertar una nueva reserva.
-- ------------------------------------------------------------
DROP TRIGGER IF EXISTS trg_solapamiento_insert$$
CREATE TRIGGER trg_solapamiento_insert
BEFORE INSERT ON Reservas
FOR EACH ROW
BEGIN
    DECLARE v_solapamiento INT DEFAULT 0;

    SELECT COUNT(*) INTO v_solapamiento
    FROM Reservas
    WHERE IDInstalacion = NEW.IDInstalacion
      AND FechaReserva  = NEW.FechaReserva
      AND HoraInicio    < NEW.HoraFin
      AND HoraFin       > NEW.HoraInicio;

    IF v_solapamiento > 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'ERROR [T1]: Solapamiento de horario. Ya existe una reserva para esa instalación en ese horario.';
    END IF;
END$$


-- ------------------------------------------------------------
-- TRIGGER 1b – BEFORE UPDATE en Reservas
-- Igual que el anterior pero para actualizaciones,
-- excluyendo la propia fila que se está modificando.
-- ------------------------------------------------------------
DROP TRIGGER IF EXISTS trg_solapamiento_update$$
CREATE TRIGGER trg_solapamiento_update
BEFORE UPDATE ON Reservas
FOR EACH ROW
BEGIN
    DECLARE v_solapamiento INT DEFAULT 0;

    SELECT COUNT(*) INTO v_solapamiento
    FROM Reservas
    WHERE IDInstalacion = NEW.IDInstalacion
      AND FechaReserva  = NEW.FechaReserva
      AND IDReserva    != NEW.IDReserva       -- excluimos la propia fila
      AND HoraInicio    < NEW.HoraFin
      AND HoraFin       > NEW.HoraInicio;

    IF v_solapamiento > 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'ERROR [T1]: Solapamiento de horario. Ya existe una reserva para esa instalación en ese horario.';
    END IF;
END$$


-- ------------------------------------------------------------
-- TRIGGER 2 – AFTER UPDATE en Instalaciones
-- Cuando el Estado cambia a 'Mantenimiento', inserta
-- automáticamente un registro en HistorialMantenimiento.
-- ------------------------------------------------------------
DROP TRIGGER IF EXISTS trg_registrar_mantenimiento$$
CREATE TRIGGER trg_registrar_mantenimiento
AFTER UPDATE ON Instalaciones
FOR EACH ROW
BEGIN
    IF NEW.Estado = 'Mantenimiento' AND OLD.Estado != 'Mantenimiento' THEN
        INSERT INTO HistorialMantenimiento (IDInstalacion, FechaMantenimiento, Comentario)
        VALUES (
            NEW.IDInstalacion,
            NOW(),
            'Instalación puesta en mantenimiento de forma automática por el sistema.'
        );
    END IF;
END$$


-- ------------------------------------------------------------
-- TRIGGER 3 – BEFORE INSERT en AsistenciasClase
-- Comprueba que el número de inscritos no supere CupoMaximo
-- de la clase antes de permitir la inscripción.
-- ------------------------------------------------------------
DROP TRIGGER IF EXISTS trg_verificar_cupo$$
CREATE TRIGGER trg_verificar_cupo
BEFORE INSERT ON AsistenciasClase
FOR EACH ROW
BEGIN
    DECLARE v_inscritos  INT DEFAULT 0;
    DECLARE v_cupoMax    INT DEFAULT 0;

    -- Socios ya inscritos en esa clase
    SELECT COUNT(*) INTO v_inscritos
    FROM AsistenciasClase
    WHERE IDClase = NEW.IDClase;

    -- Cupo máximo definido para esa clase
    SELECT CupoMaximo INTO v_cupoMax
    FROM Clases
    WHERE IDClase = NEW.IDClase;

    IF v_inscritos >= v_cupoMax THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'ERROR [T3]: Cupo máximo alcanzado. No se puede inscribir al socio en esta clase.';
    END IF;
END$$


-- ============================================================
--  PROCEDIMIENTOS ALMACENADOS
-- ============================================================

-- ------------------------------------------------------------
-- PROCEDIMIENTO 1: InformeSocios
-- Lista los socios que han realizado más de p_minReservas
-- reservas en el último mes y devuelve el total via OUT.
--
-- Llamada: CALL InformeSocios(2, @total); SELECT @total;
-- ------------------------------------------------------------
DROP PROCEDURE IF EXISTS InformeSocios$$
CREATE PROCEDURE InformeSocios(
    IN  p_minReservas INT,
    OUT p_total       INT
)
BEGIN
    -- Resultado con detalle por socio
    SELECT
        s.DNI,
        CONCAT(s.Nombre, ' ', s.Apellidos) AS Socio,
        COUNT(r.IDReserva)                 AS TotalReservas
    FROM Socios s
    JOIN Reservas r ON s.DNI = r.DNISocio
    WHERE r.FechaReserva >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
    GROUP BY s.DNI, s.Nombre, s.Apellidos
    HAVING TotalReservas > p_minReservas
    ORDER BY TotalReservas DESC;

    -- Contador total de socios que cumplen la condición
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


-- ------------------------------------------------------------
-- PROCEDIMIENTO 2: ResumenClasesPorInstructor
-- Resumen de clases impartidas por un instructor en un mes
-- y año concretos. Devuelve el total de clases via OUT.
--
-- Llamada: CALL ResumenClasesPorInstructor('12345678A', 4, 2026, @total);
--          SELECT @total;
-- ------------------------------------------------------------
DROP PROCEDURE IF EXISTS ResumenClasesPorInstructor$$
CREATE PROCEDURE ResumenClasesPorInstructor(
    IN  p_dniInstructor VARCHAR(9),
    IN  p_mes           INT,
    IN  p_anio          INT,
    OUT p_totalClases   INT
)
BEGIN
    -- Detalle de cada clase con número de asistentes
    SELECT
        c.IDClase,
        c.NombreClase,
        c.FechaClase,
        c.HoraInicio,
        c.HoraFin,
        c.CupoMaximo,
        COUNT(a.DNISocio) AS Asistentes
    FROM Clases c
    LEFT JOIN AsistenciasClase a ON c.IDClase = a.IDClase
    WHERE c.DNIInstructor     = p_dniInstructor
      AND MONTH(c.FechaClase) = p_mes
      AND YEAR(c.FechaClase)  = p_anio
    GROUP BY c.IDClase, c.NombreClase, c.FechaClase,
             c.HoraInicio, c.HoraFin, c.CupoMaximo
    ORDER BY c.FechaClase, c.HoraInicio;

    -- Total de clases impartidas ese mes
    SELECT COUNT(*) INTO p_totalClases
    FROM Clases
    WHERE DNIInstructor     = p_dniInstructor
      AND MONTH(FechaClase) = p_mes
      AND YEAR(FechaClase)  = p_anio;
END$$


-- ------------------------------------------------------------
-- PROCEDIMIENTO 3: AsignarReservasMasivas
-- Recorre una lista de DNIs de socios separados por comas
-- e intenta crear una reserva para cada uno en la misma
-- instalación, fecha y horario, evitando conflictos.
--
-- Llamada:
--   CALL AsignarReservasMasivas(
--       1, '2026-05-10', '10:00:00', '11:00:00',
--       '64350807C,47093353Z,37306183Q'
--   );
-- ------------------------------------------------------------
DROP PROCEDURE IF EXISTS AsignarReservasMasivas$$
CREATE PROCEDURE AsignarReservasMasivas(
    IN p_idInstalacion INT,
    IN p_fecha         DATE,
    IN p_horaInicio    TIME,
    IN p_horaFin       TIME,
    IN p_listaDNIs     TEXT        -- DNIs separados por comas
)
BEGIN
    DECLARE v_dni          VARCHAR(9);
    DECLARE v_solapamiento INT       DEFAULT 0;
    DECLARE v_pos          INT       DEFAULT 1;
    DECLARE v_token        VARCHAR(20);
    DECLARE v_separador    VARCHAR(1) DEFAULT ',';

    -- Aseguramos que la cadena termine en coma para facilitar el parseo
    SET p_listaDNIs = CONCAT(TRIM(p_listaDNIs), v_separador);

    WHILE v_pos <= CHAR_LENGTH(p_listaDNIs) DO
        -- Extraemos el siguiente token
        SET v_token = TRIM(
            SUBSTRING_INDEX(SUBSTRING(p_listaDNIs, v_pos), v_separador, 1)
        );
        SET v_pos = v_pos + CHAR_LENGTH(v_token) + 1;

        IF v_token != '' THEN
            SET v_dni = v_token;

            -- Verificamos solapamiento para ese horario e instalación
            SELECT COUNT(*) INTO v_solapamiento
            FROM Reservas
            WHERE IDInstalacion = p_idInstalacion
              AND FechaReserva  = p_fecha
              AND HoraInicio    < p_horaFin
              AND HoraFin       > p_horaInicio;

            IF v_solapamiento = 0 THEN
                INSERT INTO Reservas (DNISocio, IDInstalacion, FechaReserva, HoraInicio, HoraFin)
                VALUES (v_dni, p_idInstalacion, p_fecha, p_horaInicio, p_horaFin);
                SELECT CONCAT('✔ Reserva creada para DNI: ', v_dni) AS Resultado;
            ELSE
                SELECT CONCAT('✘ Conflicto de horario para DNI: ', v_dni, '. Reserva omitida.') AS Resultado;
            END IF;
        END IF;
    END WHILE;
END$$


-- ============================================================
--  FUNCIONES DE USUARIO
-- ============================================================

-- ------------------------------------------------------------
-- FUNCIÓN 1: PromedioReservasPorSocio
-- Devuelve el promedio de reservas realizadas por los socios
-- cuya edad es mayor o igual a p_edadMinima.
--
-- Llamada: SELECT PromedioReservasPorSocio(18);
-- ------------------------------------------------------------
DROP FUNCTION IF EXISTS PromedioReservasPorSocio$$
CREATE FUNCTION PromedioReservasPorSocio(p_edadMinima INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE v_promedio DECIMAL(10,2) DEFAULT 0.00;

    SELECT IFNULL(AVG(conteo), 0.00) INTO v_promedio
    FROM (
        SELECT
            s.DNI,
            COUNT(r.IDReserva) AS conteo
        FROM Socios s
        LEFT JOIN Reservas r ON s.DNI = r.DNISocio
        WHERE TIMESTAMPDIFF(YEAR, s.FechaNacimiento, CURDATE()) >= p_edadMinima
        GROUP BY s.DNI
    ) sub;

    RETURN v_promedio;
END$$


-- ------------------------------------------------------------
-- FUNCIÓN 2: DisponibilidadInstalacion
-- Devuelve cuántas franjas horarias de 1 hora (08:00-20:00)
-- están libres para una instalación en una fecha dada.
-- Total posible: 12 franjas (08-09, 09-10, ..., 19-20).
--
-- Llamada: SELECT DisponibilidadInstalacion(1, '2026-05-10');
-- ------------------------------------------------------------
DROP FUNCTION IF EXISTS DisponibilidadInstalacion$$
CREATE FUNCTION DisponibilidadInstalacion(
    p_idInstalacion INT,
    p_fecha         DATE
)
RETURNS INT
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE v_hora        TIME    DEFAULT '08:00:00';
    DECLARE v_horaFin     TIME;
    DECLARE v_disponibles INT     DEFAULT 0;
    DECLARE v_ocupada     INT     DEFAULT 0;

    -- Recorremos cada franja horaria de una hora entre las 08:00 y las 20:00
    WHILE v_hora < '20:00:00' DO
        SET v_horaFin = ADDTIME(v_hora, '01:00:00');

        -- Una franja está ocupada si cualquier reserva se solapa con ella
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

-- ============================================================
--  EJEMPLOS DE PRUEBA
-- ============================================================

-- -- TRIGGER 1: insertar reserva sin solapamiento (debe funcionar)
-- INSERT INTO Reservas (DNISocio, IDInstalacion, FechaReserva, HoraInicio, HoraFin)
-- VALUES ('64350807C', 1, '2026-06-01', '10:00:00', '11:00:00');

-- -- TRIGGER 1: insertar reserva con solapamiento (debe fallar)
-- INSERT INTO Reservas (DNISocio, IDInstalacion, FechaReserva, HoraInicio, HoraFin)
-- VALUES ('47093353Z', 1, '2026-06-01', '10:30:00', '11:30:00');

-- -- TRIGGER 2: cambiar estado a Mantenimiento (genera registro en HistorialMantenimiento)
-- UPDATE Instalaciones SET Estado = 'Mantenimiento' WHERE IDInstalacion = 1;
-- SELECT * FROM HistorialMantenimiento;

-- -- TRIGGER 3: inscripción en clase (falla si CupoMaximo ya está cubierto)
-- INSERT INTO AsistenciasClase (IDClase, DNISocio) VALUES (1, '64350807C');

-- -- PROCEDIMIENTO 1
-- CALL InformeSocios(2, @total); SELECT @total AS TotalSociosFiltrados;

-- -- PROCEDIMIENTO 2
-- CALL ResumenClasesPorInstructor('12345678A', 4, 2026, @total); SELECT @total;

-- -- PROCEDIMIENTO 3
-- CALL AsignarReservasMasivas(1, '2026-06-15', '09:00:00', '10:00:00', '64350807C,47093353Z');

-- -- FUNCIÓN 1
-- SELECT PromedioReservasPorSocio(18) AS PromedioReservas;

-- -- FUNCIÓN 2
-- SELECT DisponibilidadInstalacion(1, '2026-06-01') AS FranjasLibres;

-- ============================================================
--  FIN DEL SCRIPT
-- ============================================================