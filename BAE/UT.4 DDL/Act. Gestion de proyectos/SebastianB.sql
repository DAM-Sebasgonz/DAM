create schema if not exists proyectos default character set latin1;
use proyectos;

create table if not exists Empleados (
    DNI varchar(9),
    Nombre varchar(20),
    Apellido varchar(45),
    Cargo enum ("Director", "Junior", "Gestor", "Responsable") not null,  
    Primary Key (DNI)
) Engine = InnoDB;

create table if not exists Clientes (
    CIF Varchar(9),
    NombreEmpresa Varchar(30) not null unique,
    ContactoNombre varchar(15),
    tlf Int,
    Municipio Int, 
    Primary Key (CIF)
) Engine = InnoDB;

create table if not exists Proyecto (
    ProyectoID Int,
    NombreProyecto Varchar(30) unique not null,
    FechaInicio Datetime,
    FechaEntrega Datetime,
    ClienteID Varchar(9),
    ResponsableID Varchar(9),
    Presupuesto Int Not Null check(Presupuesto >= 1000),
    revision_presupuesto int (Presupuesto * 1.15 )
    Primary Key (ProyectoID),
    CHECK (FechaInicio >= '2025-01-01' AND FechaInicio <= FechaEntrega),
    
    Constraint FK_Proyectos_Clientes Foreign Key (ClienteID) References Clientes(CIF) 
		ON UPDATE CASCADE 
		ON DELETE RESTRICT,
    Constraint FK_Proyectos_Empleados Foreign Key (ResponsableID) References Empleados(DNI) 
		ON UPDATE CASCADE 
		ON DELETE RESTRICT
) Engine = InnoDB;

create table if not exists Tareas (
    TareaID Int,
    ProyectoID Int,
    FechaAsignacion Datetime Not Null,
    FechaLimite Datetime Not Null,
    Descripcion Varchar(100),
    Primary Key (TareaID, ProyectoID),
    CONSTRAINT FK_Tareas_Proyecto FOREIGN KEY (ProyectoID) REFERENCES Proyecto(ProyectoID) 
		ON UPDATE CASCADE 
		ON DELETE RESTRICT
) Engine = InnoDB;

create table if not exists Avance_Tareas (
    TareaID Int,
    ProyectoID Int,
    PorcentajeAvance Int not null default 0 check (PorcentajeAvance between 0 and 100),
    Primary Key (TareaID, ProyectoID),
    Constraint FK_AvanceTareas_Tareas Foreign Key (TareaID, ProyectoID) References Tareas(TareaID, ProyectoID) 
		ON UPDATE CASCADE 
        ON DELETE RESTRICT
) Engine = InnoDB;







