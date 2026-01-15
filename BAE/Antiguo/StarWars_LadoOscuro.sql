
-- StarWars_LadoOscuro.sql
-- Modelo relacional generado respetando el diagrama E-R suministrado.
-- MySQL 8.0, InnoDB.
SET FOREIGN_KEY_CHECKS = 0;

-- ============================
-- Tablas principales
-- ============================

CREATE TABLE `TROOPER` (
  `codigo` INT NOT NULL,
  `categoriaT` VARCHAR(50),
  `es_clon` TINYINT(1),
  `armamento` VARCHAR(100),
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `PLANETA` (
  `idPlaneta` INT NOT NULL AUTO_INCREMENT,
  `nombreP` VARCHAR(100) NOT NULL,
  `galaxia` VARCHAR(100),
  `cantidadHabitantes` BIGINT,
  PRIMARY KEY (`idPlaneta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `SITH` (
  `idSith` INT NOT NULL AUTO_INCREMENT,
  `nombreS` VARCHAR(100) NOT NULL,
  `genero` VARCHAR(20),
  `poder` VARCHAR(100),
  `tatuaje` VARCHAR(100),
  `color` VARCHAR(50),
  `lugar` VARCHAR(100),
  `tieneAprendiz` TINYINT(1),
  `idPlaneta` INT DEFAULT NULL,
  PRIMARY KEY (`idSith`),
  CONSTRAINT `fk_sith_planeta` FOREIGN KEY (`idPlaneta`) REFERENCES `PLANETA`(`idPlaneta`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `JEDI` (
  `idJedi` INT NOT NULL AUTO_INCREMENT,
  `nombreJ` VARCHAR(100) NOT NULL,
  `nivelAprendizaje` VARCHAR(50),
  `nivelEnergia` INT,
  `habilidad` VARCHAR(100),
  `reemplaza` INT DEFAULT NULL,
  PRIMARY KEY (`idJedi`),
  CONSTRAINT `fk_jedi_reemplaza` FOREIGN KEY (`reemplaza`) REFERENCES `JEDI`(`idJedi`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `SABLE_LASER` (
  `idSable` INT NOT NULL AUTO_INCREMENT,
  `categoriaSL` VARCHAR(50),
  `colorSL` VARCHAR(30),
  `tipoCristal` VARCHAR(50),
  `componente` VARCHAR(100),
  PRIMARY KEY (`idSable`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `ANDROIDE` (
  `idAndroide` INT NOT NULL AUTO_INCREMENT,
  `numSerie` VARCHAR(50) UNIQUE,
  `tipoFabricacion` VARCHAR(50),
  `apodo` VARCHAR(50),
  `especialidad` VARCHAR(100),
  PRIMARY KEY (`idAndroide`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `NAVE` (
  `idNave` INT NOT NULL AUTO_INCREMENT,
  `tipoN` VARCHAR(50),
  `modelo` VARCHAR(50),
  `chasis` VARCHAR(50),
  `motor` VARCHAR(50),
  PRIMARY KEY (`idNave`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ============================
-- Tablas intermedias / relaciones
-- ============================

-- TROOPER - SITH : 'COLABORA' (N:M impl. como tabla si fuera N:M en diagrama)
-- En el diagrama original se muestra Colabora (1,N) desde SITH a TROOPER (o viceversa).
-- Asumimos una relación M:N segura: permitimos múltiples troopers por sith y viceversa.
CREATE TABLE `COLABORA` (
  `idSith` INT NOT NULL,
  `codigoTrooper` INT NOT NULL,
  PRIMARY KEY (`idSith`, `codigoTrooper`),
  CONSTRAINT `fk_colabora_sith` FOREIGN KEY (`idSith`) REFERENCES `SITH`(`idSith`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_colabora_trooper` FOREIGN KEY (`codigoTrooper`) REFERENCES `TROOPER`(`codigo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- JEDI - SABLE_LASER : 'PORTA' (1:1 por el diagrama)
-- Implementamos como tabla con UNIQUEs para garantizar 1:1/0:1
CREATE TABLE `PORTA` (
  `idJedi` INT NOT NULL,
  `idSable` INT NOT NULL,
  PRIMARY KEY (`idJedi`, `idSable`),
  CONSTRAINT `uk_porta_jedi` UNIQUE (`idJedi`),
  CONSTRAINT `uk_porta_sable` UNIQUE (`idSable`),
  CONSTRAINT `fk_porta_jedi` FOREIGN KEY (`idJedi`) REFERENCES `JEDI`(`idJedi`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_porta_sable` FOREIGN KEY (`idSable`) REFERENCES `SABLE_LASER`(`idSable`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- JEDI - ANDROIDE : 'POSEE' (1:N en el diagrama: un Jedi puede poseer varios androides)
CREATE TABLE `POSEE` (
  `idJedi` INT NOT NULL,
  `idAndroide` INT NOT NULL,
  PRIMARY KEY (`idJedi`, `idAndroide`),
  CONSTRAINT `fk_posee_jedi` FOREIGN KEY (`idJedi`) REFERENCES `JEDI`(`idJedi`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_posee_androide` FOREIGN KEY (`idAndroide`) REFERENCES `ANDROIDE`(`idAndroide`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- JEDI - SITH : 'PELEA' (N:M con atributos fecha, region)
CREATE TABLE `PELEA` (
  `idJedi` INT NOT NULL,
  `idSith` INT NOT NULL,
  `fecha` DATE,
  `region` VARCHAR(100),
  PRIMARY KEY (`idJedi`, `idSith`, `fecha`),
  CONSTRAINT `fk_pelea_jedi` FOREIGN KEY (`idJedi`) REFERENCES `JEDI`(`idJedi`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_pelea_sith` FOREIGN KEY (`idSith`) REFERENCES `SITH`(`idSith`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- JEDI - NAVE : 'PILOTEA' (1:N, un Jedi puede pilotear varias naves o una nave varios Jedi según diagrama)
CREATE TABLE `PILOTEA` (
  `idJedi` INT NOT NULL,
  `idNave` INT NOT NULL,
  PRIMARY KEY (`idJedi`, `idNave`),
  CONSTRAINT `fk_pilotea_jedi` FOREIGN KEY (`idJedi`) REFERENCES `JEDI`(`idJedi`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_pilotea_nave` FOREIGN KEY (`idNave`) REFERENCES `NAVE`(`idNave`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

SET FOREIGN_KEY_CHECKS = 1;

-- ============================
-- Notas:
-- - Los nombres de tablas y columnas respetan el diagrama original.
-- - Claves foráneas y cardinalidades están implementadas. 
-- - Si alguna relación del diagrama era 1:1/1:N distinto a lo que interpreté, dímelo y lo ajusto.
-- - Para convertir este script en un modelo visual en MySQL Workbench:
--     1) Abre MySQL Workbench.
--     2) Ve a File > New Model (o abre uno existente).
--     3) File > Import > Reverse Engineer MySQL Create Script...
--     4) Selecciona este archivo SQL y sigue el asistente; Workbench generará el EER y podrás guardarlo como .mwb.
-- ============================
