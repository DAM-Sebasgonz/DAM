-- 1) Creación de la base de datos
CREATE DATABASE IF NOT EXISTS CFGSDAM;
USE CFGSDAM;

-- 2) Tabla Estudiantes
CREATE TABLE IF NOT EXISTS Estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    dni VARCHAR(9) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL
);

-- 3) Tabla Cursos
CREATE TABLE IF NOT EXISTS Cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(100) NOT NULL,
    descripcion TEXT,
    horas INT NOT NULL,
    coste DECIMAL(10,2) NOT NULL
);

-- 4) Tabla Matriculas
CREATE TABLE IF NOT EXISTS Matriculas (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_curso INT NOT NULL,
    fecha_matricula DATE NOT NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'Activa',
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante),
    FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
);

-- 5) Inserción de datos de ejemplo en Estudiantes
INSERT INTO Estudiantes (nombre, apellidos, dni, email, fecha_nacimiento)
VALUES
    ('Juan', 'Pérez García', '12345678A', 'juan.perez@example.com', '2001-03-15'),
    ('María', 'López Ruiz', '23456789B', 'maria.lopez@example.com', '2000-11-20'),
    ('Carlos', 'Sánchez Díaz', '34567890C', 'carlos.sanchez@example.com', '2002-07-05'),
    ('Lucía', 'Martín Gómez', '45678901D', 'lucia.martin@example.com', '2001-01-28'),
    ('Ana', 'Fernández Torres', '56789012E', 'ana.fernandez@example.com', '2002-09-14');

-- 6) Inserción de datos de ejemplo en Cursos
INSERT INTO Cursos (nombre_curso, descripcion, horas, coste)
VALUES
    ('Programación en Python', 'Curso introductorio a la programación en Python.', 120, 350.00),
    ('Desarrollo de Apps Móviles', 'Construcción de apps para Android y iOS.', 150, 500.00),
    ('Bases de Datos MySQL', 'Diseño y administración de bases de datos relacionales.', 100, 300.00),
    ('Desarrollo Web con PHP', 'Introducción a la programación web con PHP y MySQL.', 120, 400.00),
    ('Gestión de Proyectos', 'Metodologías ágiles y gestión de equipos de desarrollo.', 80, 250.00);

-- 7) Inserción de datos de ejemplo en Matriculas
INSERT INTO Matriculas (id_estudiante, id_curso, fecha_matricula, estado)
VALUES
    (1, 1, '2025-02-01', 'Activa'),    -- Juan en "Programación en Python"
    (2, 3, '2025-02-10', 'Activa'),    -- María en "Bases de Datos MySQL"
    (3, 5, '2025-03-01', 'Activa'),    -- Carlos en "Gestión de Proyectos"
    (4, 2, '2025-03-05', 'Activa'),    -- Lucía en "Desarrollo de Apps Móviles"
    (5, 1, '2025-03-15', 'Activa'),    -- Ana en "Programación en Python"
    (2, 4, '2025-04-01', 'Activa');    -- María en "Desarrollo Web con PHP"
