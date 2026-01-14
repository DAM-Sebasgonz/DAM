create schema if not exists proyectos default character set latin1;

-- Tabla Empleados

create table if not exists Empleados (
	DNI varchar(9),
    Nombre varchar(20),
    Apellido varchar(45),
    Cargo enum ("Director", "Junior", "Gestor", "Responsable") not null,  
    Primary Key (Dni)
) Engine = InnoDB;

-- Tabla Clientes

create table if not exists Clientes (
	CIF Varchar(9),
    NombreEmpresa Varchar(30) not null unique,
    ContactoNombre varchar(15),
    tlf Int,
    Municipio Int,
    Primary Key (CIF)
) Engine = InnoDN;

-- Tabla Proyecto

create table if not exists Proyecto (
	ProyectoID Int,
    NombreProyecto Varchar(30) unique not null,
    FechaInicio Datetime,
    FechaEntrega Datetime,
    ClienteID Varchar(9), -- FK_Cliente
    ResponsableID Varchar(9), -- FK_Empleado
	Presupuesto Int Not Null
) Engine = InnoDB

create table if not exists 
