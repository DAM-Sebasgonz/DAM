USE ComplejoDeportivo;

DELIMITER $$    

DROP PROCEDURE IF EXISTS InformeSocios$$
CREATE PROCEDURE InformeSocios(n_min INT, OUT total INT)
BEGIN
    SELECT DNI, Nombre, Apellidos, COUNT(*) as total_res
    FROM Socios s
    JOIN Reservas r ON s.DNI = r.DNISocio
    WHERE r.FechaReserva > DATE_SUB(NOW(), INTERVAL 30 DAY)
    GROUP BY s.DNI
    HAVING total_res > n_min;

    SELECT COUNT(*) INTO total FROM (
        SELECT DNISocio FROM Reservas 
        WHERE FechaReserva > DATE_SUB(NOW(), INTERVAL 30 DAY)
        GROUP BY DNISocio HAVING COUNT(*) > n_min
    ) t;
END$$

DROP PROCEDURE IF EXISTS ResumenClasesPorInstructor$$
CREATE PROCEDURE ResumenClasesPorInstructor(dni_inst VARCHAR(9), m INT, a INT, OUT cant INT)
BEGIN
    SELECT IDClase, NombreClase, FechaClase, HoraInicio,
           (SELECT COUNT(*) FROM AsistenciasClase a WHERE a.IDClase = c.IDClase) as num_asist
    FROM Clases c
    WHERE DNIInstructor = dni_inst 
      AND MONTH(FechaClase) = m 
      AND YEAR(FechaClase) = a;

    SELECT COUNT(*) INTO cant FROM Clases 
    WHERE DNIInstructor = dni_inst AND MONTH(FechaClase) = m AND YEAR(FechaClase) = a;
END$$


DROP PROCEDURE IF EXISTS AsignarReservasMasivas$$
CREATE PROCEDURE AsignarReservasMasivas(id_inst INT, f DATE, h1 TIME, h2 TIME, lista TEXT)
BEGIN
    DECLARE socio_dni VARCHAR(20);
    DECLARE libre INT;

    WHILE CHAR_LENGTH(lista) > 0 DO
        SET socio_dni = SUBSTRING_INDEX(lista, ',', 1);
        
        -- ¿Está libre el hueco?
        SELECT COUNT(*) INTO libre FROM Reservas
        WHERE IDInstalacion = id_inst AND FechaReserva = f
        AND (h1 < HoraFin AND h2 > HoraInicio);

        IF libre = 0 THEN
            INSERT INTO Reservas(DNISocio, IDInstalacion, FechaReserva, HoraInicio, HoraFin)
            VALUES (TRIM(socio_dni), id_inst, f, h1, h2);
        END IF;

        -- Recortar la lista para el siguiente
        IF LOCATE(',', lista) > 0 THEN
            SET lista = SUBSTRING(lista, LOCATE(',', lista) + 1);
        ELSE
            SET lista = '';
        END IF;
    END WHILE;
END$$