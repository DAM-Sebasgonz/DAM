CREATE DATABASE IF NOT EXISTS alquiler_coches;
USE alquiler_coches;

-- ===========================
--        Sucursales
-- ===========================
CREATE TABLE Sucursal (
    id_sucursal INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL,
    direccion VARCHAR(150),
    telefono VARCHAR(20),
    ciudad VARCHAR(80)
);

-- ===========================
--      Área Cliente
-- ===========================
CREATE TABLE Area_Cliente (
    id_area_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL,
    descripcion TEXT
);

-- ===========================
--      Área Empresa
-- ===========================
CREATE TABLE Area_Empresa (
    id_area_empresa INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL,
    descripcion TEXT
);

-- ===========================
--         Empleados
-- ===========================
CREATE TABLE Empleado (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(60) NOT NULL,
    apellidos VARCHAR(80),
    dni VARCHAR(12) UNIQUE,
    telefono VARCHAR(20),
    email VARCHAR(80),
    id_area_cliente INT NULL,
    id_area_empresa INT NULL,
    id_sucursal INT NULL,
    puesto VARCHAR(80),
    fecha_contratacion DATE,
    FOREIGN KEY (id_area_cliente) REFERENCES Area_Cliente(id_area_cliente),
    FOREIGN KEY (id_area_empresa) REFERENCES Area_Empresa(id_area_empresa),
    FOREIGN KEY (id_sucursal) REFERENCES Sucursal(id_sucursal)
);

-- ===========================
--          Clientes
-- ===========================
CREATE TABLE Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(12) UNIQUE,
    nombre VARCHAR(60),
    apellidos VARCHAR(80),
    telefono VARCHAR(20),
    email VARCHAR(80),
    direccion VARCHAR(150),
    fecha_registro DATE
);

-- ===========================
--         Vehiculos
-- ===========================
CREATE TABLE Vehiculo (
    id_vehiculo INT AUTO_INCREMENT PRIMARY KEY,
    matricula VARCHAR(15) UNIQUE,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    anio SMALLINT,
    tipo VARCHAR(30),
    estado VARCHAR(20),
    precio_dia DECIMAL(10,2),
    id_sucursal INT,
    FOREIGN KEY (id_sucursal) REFERENCES Sucursal(id_sucursal)
);

-- ===========================
--     Talleres Asociados
-- ===========================
CREATE TABLE Taller (
    id_taller INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    direccion VARCHAR(150),
    telefono VARCHAR(20),
    ciudad VARCHAR(80)
);

-- ===========================
--        Mantenimiento
-- ===========================
CREATE TABLE Mantenimiento (
    id_mantenimiento INT AUTO_INCREMENT PRIMARY KEY,
    id_vehiculo INT,
    id_taller INT,
    fecha DATE,
    descripcion TEXT,
    coste DECIMAL(10,2),
    FOREIGN KEY (id_vehiculo) REFERENCES Vehiculo(id_vehiculo),
    FOREIGN KEY (id_taller) REFERENCES Taller(id_taller)
);

-- ===========================
--          Seguro
-- ===========================
CREATE TABLE Seguro (
    id_seguro INT AUTO_INCREMENT PRIMARY KEY,
    id_vehiculo INT,
    aseguradora VARCHAR(80),
    tipo VARCHAR(40),
    fecha_inicio DATE,
    fecha_fin DATE,
    cobertura_detalle TEXT,
    FOREIGN KEY (id_vehiculo) REFERENCES Vehiculo(id_vehiculo)
);

-- ===========================
--          Contrato
-- ===========================
CREATE TABLE Contrato (
    id_contrato INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_vehiculo INT,
    id_sucursal_recogida INT,
    id_sucursal_devolucion INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    precio_total DECIMAL(10,2),
    estado VARCHAR(20),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_vehiculo) REFERENCES Vehiculo(id_vehiculo),
    FOREIGN KEY (id_sucursal_recogida) REFERENCES Sucursal(id_sucursal),
    FOREIGN KEY (id_sucursal_devolucion) REFERENCES Sucursal(id_sucursal)
);

-- ===========================
--    Entrega y Devolucion
-- ===========================
CREATE TABLE Entrega_Devolucion (
    id_entrega_devolucion INT AUTO_INCREMENT PRIMARY KEY,
    id_contrato INT UNIQUE,
    fecha_entrega DATETIME,
    km_entrega INT,
    combustible_entrega DECIMAL(4,2),
    fecha_devolucion DATETIME,
    km_devolucion INT,
    combustible_devolucion DECIMAL(4,2),
    daños TEXT,
    FOREIGN KEY (id_contrato) REFERENCES Contrato(id_contrato)
);

-- ===========================
--            Pago
-- ===========================
CREATE TABLE Pago (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_contrato INT,
    fecha_pago DATE,
    monto DECIMAL(10,2),
    metodo VARCHAR(20),
    FOREIGN KEY (id_contrato) REFERENCES Contrato(id_contrato)
);

