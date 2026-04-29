-- Crear la base de datos
CREATE DATABASE ComplejoDeportivo;
USE ComplejoDeportivo;

-- Tabla 1: Socios
CREATE TABLE Socios (
    DNI VARCHAR(9) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellidos VARCHAR(100) NOT NULL,
    FechaNacimiento DATE,
    Telefono VARCHAR(15),
    Email VARCHAR(100),
    FechaAlta DATE DEFAULT CURRENT_DATE
);

-- Tabla 2: Empleados
CREATE TABLE Empleados (
    DNI VARCHAR(9) PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellidos VARCHAR(100) NOT NULL,
    Puesto VARCHAR(50),
    FechaContrato DATE,
    Salario DECIMAL(10,2)
);

-- Tabla 3: Instalaciones
CREATE TABLE Instalaciones (
    IDInstalacion INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Tipo VARCHAR(50),
    Capacidad INT,
    Estado ENUM('Disponible', 'Mantenimiento', 'Ocupada') DEFAULT 'Disponible'
);

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
);

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
);
