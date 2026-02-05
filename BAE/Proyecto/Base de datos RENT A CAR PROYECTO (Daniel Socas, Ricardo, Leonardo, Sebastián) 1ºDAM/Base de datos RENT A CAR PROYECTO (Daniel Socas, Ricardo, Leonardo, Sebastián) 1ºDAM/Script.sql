SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `alquiler_coches`
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;
USE `alquiler_coches`;

-- =============================
-- area_cliente
-- =============================
CREATE TABLE IF NOT EXISTS `area_cliente` (
  `id_area_cliente` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(25) NOT NULL,
  `descripcion` TEXT NULL,
  PRIMARY KEY (`id_area_cliente`)
) ENGINE=InnoDB;

-- =============================
-- area_empresa
-- =============================
CREATE TABLE IF NOT EXISTS `area_empresa` (
  `id_area_empresa` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(25) NOT NULL,
  `descripcion` TEXT NULL,
  PRIMARY KEY (`id_area_empresa`)
) ENGINE=InnoDB;

-- =============================
-- contrato
-- =============================
CREATE TABLE IF NOT EXISTS `contrato` (
  `id_contrato` INT NOT NULL AUTO_INCREMENT,
  `fecha_inicio` DATE NOT NULL,
  `fecha_fin` DATE NOT NULL,
  `precio_total` DECIMAL(10,2) NOT NULL,
  `estado` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id_contrato`)
) ENGINE=InnoDB;

-- =============================
-- cliente
-- =============================
CREATE TABLE IF NOT EXISTS `cliente` (
  `dni_cliente` VARCHAR(9) NOT NULL,
  `nombre` VARCHAR(25) NOT NULL,
  `apellidos` VARCHAR(25) NOT NULL,
  `telefono` INT NOT NULL,
  `email` VARCHAR(40) NOT NULL,
  `direccion` VARCHAR(25) NOT NULL,
  `fecha_registro` DATE NOT NULL,
  `id_contrato` INT NOT NULL,
  PRIMARY KEY (`dni_cliente`),
  CONSTRAINT `fk_cliente_contrato`
    FOREIGN KEY (`id_contrato`)
    REFERENCES `contrato` (`id_contrato`)
) ENGINE=InnoDB;

-- =============================
-- sucursal
-- =============================
CREATE TABLE IF NOT EXISTS `sucursal` (
  `id_sucursal` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(25) NOT NULL,
  `direccion` VARCHAR(25) NOT NULL,
  `telefono` INT NOT NULL,
  `ciudad` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`id_sucursal`)
) ENGINE=InnoDB;

-- =============================
-- empleado
-- =============================
CREATE TABLE IF NOT EXISTS `empleado` (
  `dni_empleado` VARCHAR(9) NOT NULL,
  `nombre` VARCHAR(25) NOT NULL,
  `apellidos` VARCHAR(25) NOT NULL,
  `telefono` INT NOT NULL,
  `email` VARCHAR(80) NOT NULL,
  `puesto` VARCHAR(80) NOT NULL,
  `fecha_contratacion` DATE NOT NULL,
  `id_area_cliente` INT NULL,
  `id_area_empresa` INT NULL,
  `id_sucursal` INT NOT NULL,
  `id_contrato` INT NOT NULL,
  PRIMARY KEY (`dni_empleado`),
  CONSTRAINT `fk_empleado_area_cliente`
    FOREIGN KEY (`id_area_cliente`)
    REFERENCES `area_cliente` (`id_area_cliente`),
  CONSTRAINT `fk_empleado_area_empresa`
    FOREIGN KEY (`id_area_empresa`)
    REFERENCES `area_empresa` (`id_area_empresa`),
  CONSTRAINT `fk_empleado_sucursal`
    FOREIGN KEY (`id_sucursal`)
    REFERENCES `sucursal` (`id_sucursal`),
  CONSTRAINT `fk_empleado_contrato`
    FOREIGN KEY (`id_contrato`)
    REFERENCES `contrato` (`id_contrato`)
) ENGINE=InnoDB;

-- =============================
-- entrega
-- =============================
CREATE TABLE IF NOT EXISTS `entrega` (
  `id_entrega` INT NOT NULL AUTO_INCREMENT,
  `fecha_entrega` DATETIME NOT NULL,
  `km_entrega` INT NOT NULL,
  `combustible_entrega` DECIMAL(4,2) NOT NULL,
  `id_contrato` INT NOT NULL,
  PRIMARY KEY (`id_entrega`),
  UNIQUE (`id_contrato`),
  CONSTRAINT `fk_entrega_contrato`
    FOREIGN KEY (`id_contrato`)
    REFERENCES `contrato` (`id_contrato`)
) ENGINE=InnoDB;

-- =============================
-- mantenimiento
-- =============================
CREATE TABLE IF NOT EXISTS `mantenimiento` (
  `id_mantenimiento` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NOT NULL,
  `descripcion` TEXT NOT NULL,
  `coste` FLOAT NOT NULL,
  PRIMARY KEY (`id_mantenimiento`)
) ENGINE=InnoDB;

-- =============================
-- pago
-- =============================
CREATE TABLE IF NOT EXISTS `pago` (
  `id_pago` INT NOT NULL AUTO_INCREMENT,
  `fecha_pago` DATE NOT NULL,
  `monto` DECIMAL(10,2) NOT NULL,
  `metodo` VARCHAR(20) NOT NULL,
  `id_contrato` INT NOT NULL,
  PRIMARY KEY (`id_pago`),
  CONSTRAINT `fk_pago_contrato`
    FOREIGN KEY (`id_contrato`)
    REFERENCES `contrato` (`id_contrato`)
) ENGINE=InnoDB;

-- =============================
-- seguro
-- =============================
CREATE TABLE IF NOT EXISTS `seguro` (
  `id_seguro` INT NOT NULL AUTO_INCREMENT,
  `aseguradora` VARCHAR(25) NOT NULL,
  `tipo` VARCHAR(25) NOT NULL,
  `fecha_inicio` DATE NOT NULL,
  `fecha_fin` DATE NOT NULL,
  `cobertura_detalle` TEXT NOT NULL,
  PRIMARY KEY (`id_seguro`)
) ENGINE=InnoDB;

-- =============================
-- taller
-- =============================
CREATE TABLE IF NOT EXISTS `taller` (
  `id_taller` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(25) NOT NULL,
  `direccion` VARCHAR(25) NOT NULL,
  `telefono` INT NOT NULL,
  `ciudad` VARCHAR(25) NOT NULL,
  `id_mantenimiento` INT NOT NULL,
  PRIMARY KEY (`id_taller`),
  CONSTRAINT `fk_taller_mantenimiento`
    FOREIGN KEY (`id_mantenimiento`)
    REFERENCES `mantenimiento` (`id_mantenimiento`)
) ENGINE=InnoDB;

-- =============================
-- vehiculo
-- =============================
CREATE TABLE IF NOT EXISTS `vehiculo` (
  `matricula` VARCHAR(7) NOT NULL,
  `marca` VARCHAR(25) NOT NULL,
  `modelo` VARCHAR(25) NOT NULL,
  `anio` SMALLINT NOT NULL,
  `tipo` VARCHAR(30) NOT NULL,
  `estado` VARCHAR(20) NOT NULL,
  `precio_dia` DECIMAL(10,2) NOT NULL,
  `id_sucursal` INT NOT NULL,
  `id_seguro` INT NOT NULL,
  `id_mantenimiento` INT NOT NULL,
  `id_contrato` INT NOT NULL,
  PRIMARY KEY (`matricula`),
  CONSTRAINT `fk_vehiculo_sucursal`
    FOREIGN KEY (`id_sucursal`)
    REFERENCES `sucursal` (`id_sucursal`),
  CONSTRAINT `fk_vehiculo_seguro`
    FOREIGN KEY (`id_seguro`)
    REFERENCES `seguro` (`id_seguro`),
  CONSTRAINT `fk_vehiculo_mantenimiento`
    FOREIGN KEY (`id_mantenimiento`)
    REFERENCES `mantenimiento` (`id_mantenimiento`),
  CONSTRAINT `fk_vehiculo_contrato`
    FOREIGN KEY (`id_contrato`)
    REFERENCES `contrato` (`id_contrato`)
) ENGINE=InnoDB;

-- =============================
-- devolucion
-- =============================
CREATE TABLE IF NOT EXISTS `devolucion` (
  `id_devolucion` INT NOT NULL AUTO_INCREMENT,
  `fecha_devolucion` DATETIME NOT NULL,
  `km_devolucion` INT NOT NULL,
  `combustible_devolucion` DECIMAL(4,2) NOT NULL,
  `daños` TEXT NOT NULL,
  `id_contrato` INT NOT NULL,
  PRIMARY KEY (`id_devolucion`),
  UNIQUE (`id_contrato`),
  CONSTRAINT `fk_devolucion_contrato`
    FOREIGN KEY (`id_contrato`)
    REFERENCES `contrato` (`id_contrato`)
) ENGINE=InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
