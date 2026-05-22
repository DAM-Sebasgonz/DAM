USE `Hermes IT support` ;
SET GLOBAL event_scheduler = ON;

-- =============================================================================
-- TAREA A: ESTRUCTURAS AUXILIARES
-- =============================================================================
ALTER SCHEMA `Hermes IT support` DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;
-- TAREA A: Estructura Auxiliar Corregida sin Warnings
CREATE TABLE IF NOT EXISTS Auditoria_Tickets (
    IdAuditoria INT PRIMARY KEY AUTO_INCREMENT,
    CodigoTicket INT NOT NULL,
    EstadoAnterior VARCHAR(50),
    EstadoNuevo VARCHAR(50) NOT NULL,
    FechaCambio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CodigoTicket) REFERENCES Ticket(CodigoTicket) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =============================================================================
-- TAREA B: DESARROLLO DEL PROCEDIMIENTO ALMACENADO
-- =============================================================================
DELIMITER //
CREATE PROCEDURE nsertarTicketManual(
    IN p_Email VARCHAR(150),
    IN p_NombreCompleto VARCHAR(200),
    IN p_Telefono VARCHAR(20),
    IN p_Titulo VARCHAR(255),
    IN p_Descripcion TEXT,
    IN p_IdEmpleado INT
)
BEGIN
    DECLARE v_IdCliente INT DEFAULT NULL;
    DECLARE v_IdEstadoInicial INT;
    DECLARE v_IdPrioridadInicial INT;
    DECLARE v_IdCategoriaInicial INT;

    SELECT IdCliente INTO v_IdCliente 
    FROM Cliente 
    WHERE Email = p_Email 
    LIMIT 1;

    IF v_IdCliente IS NULL THEN
        INSERT INTO Cliente (NombreCompleto, Email, Telefono) 
        VALUES (p_NombreCompleto, p_Email, p_Telefono);
        
        SET v_IdCliente = LAST_INSERT_ID();
    END IF;

    SELECT IdEstado INTO v_IdEstadoInicial FROM Estado ORDER BY OrdenVisualizacion ASC LIMIT 1;
    SELECT IdPrioridad INTO v_IdPrioridadInicial FROM Prioridad ORDER BY Nivel ASC LIMIT 1;
    SELECT IdCategoria INTO v_IdCategoriaInicial FROM Categoria WHERE Activa = TRUE LIMIT 1;

    IF v_IdEstadoInicial IS NULL THEN SET v_IdEstadoInicial = 1; END IF;
    IF v_IdPrioridadInicial IS NULL THEN SET v_IdPrioridadInicial = 1; END IF;
    IF v_IdCategoriaInicial IS NULL THEN SET v_IdCategoriaInicial = 1; END IF;

    INSERT INTO Ticket (Titulo, Descripcion, IdCliente, IdCategoria, IdEstado, IdPrioridad, IdEmpleado)
    VALUES (p_Titulo, p_Descripcion, v_IdCliente, v_IdCategoriaInicial, v_IdEstadoInicial, v_IdPrioridadInicial, p_IdEmpleado);
END //
DELIMITER ;

-- =============================================================================
-- TAREA C: DESARROLLO DE TRIGGERS (DISPARADORES)
-- =============================================================================

-- Trigger 1 (Validación): Evitar cerrar un ticket si no posee un historial de mensajes
DELIMITER //
CREATE TRIGGER tg_validar_cierre_ticket
BEFORE UPDATE ON Ticket
FOR EACH ROW
BEGIN
    DECLARE v_NombreEstadoCerrado VARCHAR(50) DEFAULT 'Cerrado';
    DECLARE v_IdEstadoCerrado INT;
    DECLARE v_CantMensajes INT DEFAULT 0;

    SELECT IdEstado INTO v_IdEstadoCerrado 
    FROM Estado 
    WHERE NombreEstado = v_NombreEstadoCerrado 
    LIMIT 1;

    IF NEW.IdEstado = v_IdEstadoCerrado AND OLD.IdEstado <> v_IdEstadoCerrado THEN
        SELECT COUNT(*) INTO v_CantMensajes 
        FROM Mensaje 
        WHERE CodigoTicket = NEW.CodigoTicket;
        IF v_CantMensajes = 0 THEN
            SIGNAL SQLSTATE '45000' 
            SET MESSAGE_TEXT = 'No se puede cerrar un ticket sin historial de mensajes';
        END IF;
        IF NEW.FechaCierre IS NULL THEN
            SET NEW.FechaCierre = NOW();
        END IF;
    END IF;
END //
DELIMITER ;

-- Trigger 2 (Auditoría): Registrar los cambios históricos de estado de un ticket
DELIMITER //
CREATE TRIGGER tg_auditar_cambio_estado
AFTER UPDATE ON Ticket
FOR EACH ROW
BEGIN
    DECLARE v_NombreEstadoAnterior VARCHAR(50);
    DECLARE v_NombreEstadoNuevo VARCHAR(50);

    IF OLD.IdEstado <> NEW.IdEstado THEN
        SELECT NombreEstado INTO v_NombreEstadoAnterior FROM Estado WHERE IdEstado = OLD.IdEstado;
        SELECT NombreEstado INTO v_NombreEstadoNuevo FROM Estado WHERE IdEstado = NEW.IdEstado;
        INSERT INTO Auditoria_Tickets (CodigoTicket, EstadoAnterior, EstadoNuevo, FechaCambio)
        VALUES (NEW.CodigoTicket, v_NombreEstadoAnterior, v_NombreEstadoNuevo, NOW());
    END IF;
END //
DELIMITER ;

-- =============================================================================
-- TAREA D: TAREA PROGRAMADA (EVENTOS)
-- =============================================================================
DELIMITER //
CREATE EVENT ev_archivado_nocturno_tickets
ON SCHEDULE EVERY 1 DAY
STARTS TIMESTAMP(CURRENT_DATE, '03:00:00')
DO
BEGIN
    DECLARE v_IdEstadoCerrado INT;
    DECLARE v_IdEstadoArchivado INT;

    SELECT IdEstado INTO v_IdEstadoCerrado FROM Estado WHERE NombreEstado = 'Cerrado' LIMIT 1;
    SELECT IdEstado INTO v_IdEstadoArchivado FROM Estado WHERE NombreEstado = 'Archivado' LIMIT 1;
    IF v_IdEstadoArchivado IS NULL AND v_IdEstadoCerrado IS NOT NULL THEN
        INSERT INTO Estado (NombreEstado, Descripcion, OrdenVisualizacion) 
        VALUES ('Archivado', 'Tickets cerrados hace más de 3 años', 99);
        SET v_IdEstadoArchivado = LAST_INSERT_ID();
    END IF;
    IF v_IdEstadoCerrado IS NOT NULL AND v_IdEstadoArchivado IS NOT NULL THEN
        UPDATE Ticket 
        SET IdEstado = v_IdEstadoArchivado
        WHERE IdEstado = v_IdEstadoCerrado 
          AND FechaCierre IS NOT NULL 
          AND DATEDIFF(NOW(), FechaCierre) > 1095;
    END IF;
END //
DELIMITER ;