-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS SistemaSanitario;
USE SistemaSanitario;

-- Tabla de Pacientes
CREATE TABLE Pacientes (
    dni_paciente VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    genero ENUM('M', 'F', 'Otro') NOT NULL,
    telefono VARCHAR(20)
);

-- Tabla de Médicos
CREATE TABLE Medicos (
    dni_medico VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100),
    telefono VARCHAR(20),
    fecha_alta DATE NOT NULL
);

-- Tabla de Citas
CREATE TABLE Citas (
    id_cita INT AUTO_INCREMENT PRIMARY KEY,
    dni_paciente VARCHAR(9) NOT NULL,
    dni_medico VARCHAR(9) NOT NULL,
    fecha_hora DATETIME NOT NULL,
    motivo TEXT,
    estado ENUM('Programada', 'Realizada', 'Cancelada') DEFAULT 'Programada',
    FOREIGN KEY (dni_paciente) REFERENCES Pacientes(dni_paciente),
    FOREIGN KEY (dni_medico) REFERENCES Medicos(dni_medico)
);

-- Tabla de Diagnósticos
CREATE TABLE Diagnosticos (
    id_diagnostico INT AUTO_INCREMENT PRIMARY KEY,
    id_cita INT NOT NULL,
    descripcion TEXT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_cita) REFERENCES Citas(id_cita)
);

-- Tabla de Tratamientos
CREATE TABLE Tratamientos (
    id_tratamiento INT AUTO_INCREMENT PRIMARY KEY,
    id_diagnostico INT NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    observaciones TEXT,
    FOREIGN KEY (id_diagnostico) REFERENCES Diagnosticos(id_diagnostico)
);
