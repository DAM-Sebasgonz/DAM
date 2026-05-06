-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS ComplejoDeportivo;
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
    CONSTRAINT fk_reserva_socio FOREIGN KEY (DNISocio) 
        REFERENCES Socios(DNI) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_reserva_inst FOREIGN KEY (IDInstalacion) 
        REFERENCES Instalaciones(IDInstalacion) ON DELETE CASCADE ON UPDATE CASCADE
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
    CONSTRAINT fk_clase_instruc FOREIGN KEY (DNIInstructor) 
        REFERENCES Empleados(DNI) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB;

-- Tabla 6: Asistencias
CREATE TABLE AsistenciasClase (
    IDClase INT NOT NULL,
    DNISocio VARCHAR(9) NOT NULL,
    PRIMARY KEY (IDClase, DNISocio),
    CONSTRAINT fk_asist_clase FOREIGN KEY (IDClase) 
        REFERENCES Clases(IDClase) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_asist_socio FOREIGN KEY (DNISocio) 
        REFERENCES Socios(DNI) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB;

-- Tabla 7: Historial
CREATE TABLE HistorialMantenimiento (
    IDMantenimiento INT AUTO_INCREMENT PRIMARY KEY,
    IDInstalacion INT NOT NULL,
    FechaMantenimiento DATETIME NOT NULL,
    Comentario VARCHAR(255),
    CONSTRAINT fk_mant_inst FOREIGN KEY (IDInstalacion) 
        REFERENCES Instalaciones(IDInstalacion) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB;