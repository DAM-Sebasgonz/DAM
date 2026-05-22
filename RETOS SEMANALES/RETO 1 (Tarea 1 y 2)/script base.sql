CREATE SCHEMA IF NOT EXISTS `Hermes IT support` DEFAULT CHARACTER SET utf8 ;
USE `Hermes IT support` ;

CREATE TABLE Cliente (
    IdCliente INT PRIMARY KEY AUTO_INCREMENT,
    NombreCompleto VARCHAR(200) NOT NULL,
    Email VARCHAR(150) NOT NULL UNIQUE,
    Telefono VARCHAR(20),
    FechaRegistro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_email (Email)
);

CREATE TABLE Categoria (
    IdCategoria INT PRIMARY KEY AUTO_INCREMENT,
    NombreCategoria VARCHAR(100) NOT NULL UNIQUE,
    Descripcion TEXT,
    Activa BOOLEAN DEFAULT TRUE
);

CREATE TABLE Estado (
    IdEstado INT PRIMARY KEY AUTO_INCREMENT,
    NombreEstado VARCHAR(50) NOT NULL UNIQUE,
    Descripcion VARCHAR(200),
    OrdenVisualizacion INT
);

CREATE TABLE Prioridad (
    IdPrioridad INT PRIMARY KEY AUTO_INCREMENT,
    NombrePrioridad VARCHAR(50) NOT NULL UNIQUE,
    Nivel INT NOT NULL,
    UNIQUE KEY uk_nivel (Nivel)
);

CREATE TABLE Departamento (
    IdDepartamento INT PRIMARY KEY AUTO_INCREMENT,
    NombreDep VARCHAR(100) NOT NULL,
    Ubicacion VARCHAR(200),
    Activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE Operador (
    IdEmpleado INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(200) NOT NULL,
    CorreoCorporativo VARCHAR(150) NOT NULL UNIQUE,
    IdDepartamento INT NOT NULL,
    FechaIngreso DATE,
    Activo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (IdDepartamento) REFERENCES Departamento(IdDepartamento) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE Ticket (
    CodigoTicket INT PRIMARY KEY AUTO_INCREMENT,
    Titulo VARCHAR(255) NOT NULL,
    Descripcion TEXT NOT NULL,
    FechaCreacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FechaCierre TIMESTAMP NULL,
    IdCliente INT NOT NULL,
    IdCategoria INT NOT NULL,
    IdEstado INT NOT NULL,
    IdPrioridad INT NOT NULL,
    IdEmpleado INT NULL, -- Agregado para asignar técnico
    FOREIGN KEY (IdCliente) REFERENCES Cliente(IdCliente),
    FOREIGN KEY (IdCategoria) REFERENCES Categoria(IdCategoria),
    FOREIGN KEY (IdEstado) REFERENCES Estado(IdEstado),
    FOREIGN KEY (IdPrioridad) REFERENCES Prioridad(IdPrioridad),
    FOREIGN KEY (IdEmpleado) REFERENCES Operador(IdEmpleado)
);

CREATE TABLE Mensaje (
    IdMensaje INT PRIMARY KEY AUTO_INCREMENT,
    Cuerpo TEXT NOT NULL,
    FechaHora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CodigoTicket INT NOT NULL,
    IdCliente INT NULL,
    IdEmpleado INT NULL,
    FOREIGN KEY (CodigoTicket) REFERENCES Ticket(CodigoTicket) ON DELETE CASCADE,
    FOREIGN KEY (IdCliente) REFERENCES Cliente(IdCliente),
    FOREIGN KEY (IdEmpleado) REFERENCES Operador(IdEmpleado)
);