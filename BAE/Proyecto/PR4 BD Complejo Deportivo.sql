-- Crear la base de datos
CREATE DATABASE if not exists ComplejoDeportivo;
USE ComplejoDeportivo;

-- Tabla 1: Socios
CREATE TABLE Socios (
    DNI VARCHAR(9) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellidos VARCHAR(100) NOT NULL,
    FechaNacimiento DATE,
    Telefono VARCHAR(15),
    Email VARCHAR(100),
    FechaAlta DATE DEFAULT (CURRENT_DATE)
) ENGINE = InnoDB;

-- Tabla 2: Empleados
CREATE TABLE Empleados (
    DNI VARCHAR(9) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellidos VARCHAR(100) NOT NULL,
    Puesto VARCHAR(50),
    FechaContrato DATE,
    Salario DECIMAL(10,2)
) ENGINE = InnoDB;

-- Tabla 3: Instalaciones
CREATE TABLE Instalaciones (
    IDInstalacion INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Tipo VARCHAR(50),
    Capacidad INT,
    Estado ENUM('Disponible', 'Mantenimiento', 'Ocupada') DEFAULT 'Disponible'
) ENGINE = InnoDB;

-- Tabla 4: Reservas
CREATE TABLE Reservas (
    IDReserva INT AUTO_INCREMENT PRIMARY KEY,
    DNISocio VARCHAR(9),
    IDInstalacion INT,
    FechaReserva DATE,
    HoraInicio TIME,
    HoraFin TIME,
    FOREIGN KEY (DNISocio) REFERENCES Socios(DNI),
    FOREIGN KEY (IDInstalacion) REFERENCES Instalaciones(IDInstalacion)
) ENGINE = InnoDB;

-- Tabla 5: Clases
CREATE TABLE Clases (
    IDClase INT AUTO_INCREMENT PRIMARY KEY,
    NombreClase VARCHAR(100) NOT NULL,
    DNIInstructor VARCHAR(9),
    FechaClase DATE,
    HoraInicio TIME,
    HoraFin TIME,
    CupoMaximo INT,
    FOREIGN KEY (DNIInstructor) REFERENCES Empleados(DNI)
) ENGINE = InnoDB;

CREATE TABLE AsistenciasClase (
    IDClase   INT NOT NULL,
    DNISocio  VARCHAR(9) NOT NULL,
    PRIMARY KEY (IDClase, DNISocio),
    FOREIGN KEY (IDClase) REFERENCES Clases(IDClase),
    FOREIGN KEY (DNISocio) REFERENCES Socios(DNI)
) ENGINE = InnoDB;

CREATE TABLE HistorialMantenimiento (
    IDMantenimiento INT AUTO_INCREMENT PRIMARY KEY,
    IDInstalacion INT NOT NULL,
    FechaMantenimiento DATETIME NOT NULL,
    Comentario VARCHAR(255),
    FOREIGN KEY (IDInstalacion) REFERENCES Instalaciones(IDInstalacion)
) ENGINE = InnoDB;
