SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `Hermes IT support` DEFAULT CHARACTER SET utf8;
USE `Hermes IT support`;

CREATE TABLE IF NOT EXISTS `Mensaje` (
  `idMensaje` INT NOT NULL AUTO_INCREMENT,
  `Cuerpo`    TEXT NOT NULL,
  `FechaHora` DATETIME NOT NULL,
  PRIMARY KEY (`idMensaje`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Operador` (
  `idEmpleado`        INT NOT NULL AUTO_INCREMENT,
  `CorreoCorporativo` VARCHAR(100) NOT NULL,
  `Nombre`            VARCHAR(100) NOT NULL,
  `Mensaje_idMensaje` INT NOT NULL,
  PRIMARY KEY (`idEmpleado`),
  INDEX `fk_Operador_Mensaje1_idx` (`Mensaje_idMensaje` ASC),
  CONSTRAINT `fk_Operador_Mensaje1`
    FOREIGN KEY (`Mensaje_idMensaje`)
    REFERENCES `Mensaje` (`idMensaje`)
    ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Ticket` (
  `CodigoTicket`       INT NOT NULL AUTO_INCREMENT,
  `Prioridad`          VARCHAR(45) NOT NULL,
  `Categoria`          VARCHAR(45) NOT NULL,
  `Titulo`             VARCHAR(100) NOT NULL,
  `Descripcion`        TEXT NOT NULL,
  `FechaCreacion`      DATE NOT NULL,
  `FechaCierre`        DATE NULL,
  `Estado`             VARCHAR(45) NOT NULL,
  `Mensaje_idMensaje`  INT NOT NULL,
  `Operador_idEmpleado` INT NOT NULL,
  PRIMARY KEY (`CodigoTicket`),
  INDEX `fk_Ticket_Mensaje1_idx` (`Mensaje_idMensaje` ASC),
  INDEX `fk_Ticket_Operador1_idx` (`Operador_idEmpleado` ASC),
  CONSTRAINT `fk_Ticket_Mensaje1`
    FOREIGN KEY (`Mensaje_idMensaje`)
    REFERENCES `Mensaje` (`idMensaje`)
    ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Ticket_Operador1`
    FOREIGN KEY (`Operador_idEmpleado`)
    REFERENCES `Operador` (`idEmpleado`)
    ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Cliente` (
  `idCliente`          INT NOT NULL AUTO_INCREMENT,
  `NombreCompleto`     VARCHAR(100) NOT NULL,
  `Email`              VARCHAR(100) NOT NULL,
  `Telefono`           INT NOT NULL,
  `Mensaje_idMensaje`  INT NOT NULL,
  `Ticket_CodigoTicket` INT NOT NULL,
  PRIMARY KEY (`idCliente`),
  UNIQUE INDEX `Email_UNIQUE` (`Email` ASC),
  INDEX `fk_Cliente_Mensaje_idx` (`Mensaje_idMensaje` ASC),
  INDEX `fk_Cliente_Ticket1_idx` (`Ticket_CodigoTicket` ASC),
  CONSTRAINT `fk_Cliente_Mensaje`
    FOREIGN KEY (`Mensaje_idMensaje`)
    REFERENCES `Mensaje` (`idMensaje`)
    ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Cliente_Ticket1`
    FOREIGN KEY (`Ticket_CodigoTicket`)
    REFERENCES `Ticket` (`CodigoTicket`)
    ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Departamento` (
  `idDepartamento`     INT NOT NULL AUTO_INCREMENT,
  `Ubicacion`          VARCHAR(45) NOT NULL,
  `NombreDep`          VARCHAR(45) NOT NULL,
  `Operador_idEmpleado` INT NOT NULL,
  PRIMARY KEY (`idDepartamento`, `Operador_idEmpleado`),
  INDEX `fk_Departamento_Operador1_idx` (`Operador_idEmpleado` ASC),
  CONSTRAINT `fk_Departamento_Operador1`
    FOREIGN KEY (`Operador_idEmpleado`)
    REFERENCES `Operador` (`idEmpleado`)
    ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;