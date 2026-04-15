CREATE DATABASE  IF NOT EXISTS `po_ut5_bae` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `po_ut5_bae`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: po_ut5_bae
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alumnos`
--

DROP TABLE IF EXISTS `alumnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumnos` (
  `DNI` varchar(9) NOT NULL,
  `Nombre` varchar(20) NOT NULL,
  `Apellido` varchar(20) NOT NULL,
  `Bilingue` enum('S','N') NOT NULL,
  PRIMARY KEY (`DNI`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumnos`
--

LOCK TABLES `alumnos` WRITE;
/*!40000 ALTER TABLE `alumnos` DISABLE KEYS */;
INSERT INTO `alumnos` VALUES ('13409827D','Ángel','Luque','S'),('35143098B','Dolores','García','N'),('39099100E','Josefa','Muñoz','S'),('51437206G','David','Chaparro','N'),('94342001A','Rosa','Blanco','S'),('94392805F','Pilar','Cea','S'),('98105401C','Pedro','Marín','N');
/*!40000 ALTER TABLE `alumnos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asignatura`
--

DROP TABLE IF EXISTS `asignatura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asignatura` (
  `CodAsig` int unsigned NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `NumHoras` int unsigned NOT NULL,
  `CodCiclo` int unsigned NOT NULL,
  `Bilingue` enum('S','N') NOT NULL,
  PRIMARY KEY (`CodAsig`),
  KEY `fk_asig_ciclo_idx` (`CodCiclo`),
  CONSTRAINT `fk_asig_ciclo` FOREIGN KEY (`CodCiclo`) REFERENCES `ciclo` (`CodCF`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asignatura`
--

LOCK TABLES `asignatura` WRITE;
/*!40000 ALTER TABLE `asignatura` DISABLE KEYS */;
INSERT INTO `asignatura` VALUES (1,'Bases de datos',165,1,'S'),(2,'Lenguaje de marcas',120,1,'N'),(3,'Seguridad informática',90,2,'S'),(4,'Despliegue aplicaciones webs',110,1,'N'),(5,'Fundamentos de hardware',90,2,'N'),(6,'Acceso a datos',180,1,'N'),(7,'Gestión de datos',65,5,'S'),(8,'Elementos de derecho',80,5,'N'),(9,'Contabilidad y fiscalidad',90,4,'N'),(10,'Administración pública',100,4,'S');
/*!40000 ALTER TABLE `asignatura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bilingue`
--

DROP TABLE IF EXISTS `bilingue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bilingue` (
  `DNI` varchar(9) NOT NULL,
  `FechaCertf` date NOT NULL,
  `ComAut` varchar(20) NOT NULL,
  PRIMARY KEY (`DNI`),
  CONSTRAINT `fk_alu_bilingue` FOREIGN KEY (`DNI`) REFERENCES `alumnos` (`DNI`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bilingue`
--

LOCK TABLES `bilingue` WRITE;
/*!40000 ALTER TABLE `bilingue` DISABLE KEYS */;
INSERT INTO `bilingue` VALUES ('39099100E','2019-08-10','Cataluña'),('51437206G','2017-03-01','Madrid'),('94342001A','2018-09-10','Andalucía'),('94392805F','2018-10-28','Canarias');
/*!40000 ALTER TABLE `bilingue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ciclo`
--

DROP TABLE IF EXISTS `ciclo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ciclo` (
  `CodCF` int unsigned NOT NULL,
  `Nombre` varchar(55) NOT NULL,
  `Siglas` varchar(4) NOT NULL,
  `Dpto` int unsigned NOT NULL,
  PRIMARY KEY (`CodCF`),
  KEY `fk_dpto_ciclo_idx` (`Dpto`),
  CONSTRAINT `fk_dpto_ciclo` FOREIGN KEY (`Dpto`) REFERENCES `departamento` (`CodDep`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciclo`
--

LOCK TABLES `ciclo` WRITE;
/*!40000 ALTER TABLE `ciclo` DISABLE KEYS */;
INSERT INTO `ciclo` VALUES (1,'Desarrollo de aplicaciones webs','DAW',1),(2,'Administración de sistemas informáticos en red','ASIR',1),(3,'Desarrollo de aplicaciones multiplataforma','DAM',1),(4,'Contabilidad y finanzas','CYF',2),(5,'Secretariado','SEC',2);
/*!40000 ALTER TABLE `ciclo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departamento`
--

DROP TABLE IF EXISTS `departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamento` (
  `CodDep` int unsigned NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `JefeDpto` varchar(9) NOT NULL,
  PRIMARY KEY (`CodDep`),
  KEY `fk_JefeDpto_idx` (`JefeDpto`),
  CONSTRAINT `fk_JefeDpto` FOREIGN KEY (`JefeDpto`) REFERENCES `profesor` (`DNI`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamento`
--

LOCK TABLES `departamento` WRITE;
/*!40000 ALTER TABLE `departamento` DISABLE KEYS */;
INSERT INTO `departamento` VALUES (1,'Informática y Comunicaciones','48103100A'),(2,'Administración y Finanzas','48300100B');
/*!40000 ALTER TABLE `departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imparte`
--

DROP TABLE IF EXISTS `imparte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `imparte` (
  `DNIProf` varchar(9) NOT NULL,
  `CodAsig` int unsigned NOT NULL,
  `Curso` year NOT NULL,
  PRIMARY KEY (`DNIProf`,`CodAsig`,`Curso`),
  KEY `fk4_asig_imparte_idx` (`CodAsig`),
  CONSTRAINT `fk3_profe_imparte` FOREIGN KEY (`DNIProf`) REFERENCES `profesor` (`DNI`),
  CONSTRAINT `fk4_asig_imparte` FOREIGN KEY (`CodAsig`) REFERENCES `asignatura` (`CodAsig`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imparte`
--

LOCK TABLES `imparte` WRITE;
/*!40000 ALTER TABLE `imparte` DISABLE KEYS */;
INSERT INTO `imparte` VALUES ('28900194X',1,2022),('29600501A',1,2021),('44102321Y',1,2021),('84501495H',1,2023),('44102321Y',2,2022),('90100200G',3,2022),('44102321Y',4,2022),('48300100B',5,2022),('48103100A',6,2021),('90100200G',6,2023);
/*!40000 ALTER TABLE `imparte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matricula`
--

DROP TABLE IF EXISTS `matricula`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matricula` (
  `DNI` varchar(9) NOT NULL,
  `CodAsig` int unsigned NOT NULL,
  `Curso` year NOT NULL,
  `Nota` int unsigned NOT NULL,
  PRIMARY KEY (`DNI`,`CodAsig`,`Curso`),
  KEY `fk_matric_asig_idx` (`CodAsig`),
  CONSTRAINT `fk_matric_alu` FOREIGN KEY (`DNI`) REFERENCES `alumnos` (`DNI`),
  CONSTRAINT `fk_matric_asig` FOREIGN KEY (`CodAsig`) REFERENCES `asignatura` (`CodAsig`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matricula`
--

LOCK TABLES `matricula` WRITE;
/*!40000 ALTER TABLE `matricula` DISABLE KEYS */;
INSERT INTO `matricula` VALUES ('13409827D',1,2022,8),('35143098B',1,2021,3),('35143098B',2,2023,7),('35143098B',4,2022,5),('35143098B',6,2021,7),('39099100E',1,2022,4),('51437206G',1,2021,3),('51437206G',1,2022,9),('51437206G',6,2021,6),('94392805F',1,2022,4),('94392805F',1,2023,8),('94392805F',6,2021,8),('98105401C',2,2023,5);
/*!40000 ALTER TABLE `matricula` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profesor`
--

DROP TABLE IF EXISTS `profesor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profesor` (
  `DNI` varchar(9) NOT NULL,
  `Nombre` varchar(20) NOT NULL,
  `Apellido` varchar(20) NOT NULL,
  `Departamento` int unsigned NOT NULL,
  PRIMARY KEY (`DNI`),
  KEY `fk2_Dpto_prof_idx` (`Departamento`),
  CONSTRAINT `fk2_Dpto_prof` FOREIGN KEY (`Departamento`) REFERENCES `departamento` (`CodDep`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profesor`
--

LOCK TABLES `profesor` WRITE;
/*!40000 ALTER TABLE `profesor` DISABLE KEYS */;
INSERT INTO `profesor` VALUES ('28900194X','Marta','Negro',1),('29600501A','Dolores','Ramos',1),('44102321Y','Antonio','Martínez',1),('48103100A','Miguel Ángel','Martínez',1),('48300100B','Ian','Oxley',2),('84501495H','Iván','Sánchez',1),('90100200G','Alejandro','Martín',1);
/*!40000 ALTER TABLE `profesor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-03 22:07:55
