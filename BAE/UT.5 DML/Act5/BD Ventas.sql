DROP DATABASE IF EXISTS tienda_sql;
CREATE DATABASE tienda_sql CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;
USE tienda_sql;

-- =========================
-- TABLAS
-- =========================

CREATE TABLE clientes (
  id_cliente INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(80) NOT NULL,
  email VARCHAR(120) NOT NULL UNIQUE,
  pais VARCHAR(50) NOT NULL,
  ciudad VARCHAR(60) NOT NULL,
  fecha_alta DATE NOT NULL
);

CREATE TABLE categorias (
  id_categoria INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE productos (
  id_producto INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(80) NOT NULL,
  id_categoria INT NOT NULL,
  precio_lista DECIMAL(10,2) NOT NULL,
  activo TINYINT(1) NOT NULL DEFAULT 1,
  FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

CREATE TABLE pedidos (
  id_pedido INT PRIMARY KEY AUTO_INCREMENT,
  id_cliente INT NOT NULL,
  fecha_pedido DATE NOT NULL,
  estado ENUM('PAGADO','ENVIADO','CANCELADO') NOT NULL,
  FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE lineas_pedido (
  id_linea INT PRIMARY KEY AUTO_INCREMENT,
  id_pedido INT NOT NULL,
  id_producto INT NOT NULL,
  cantidad INT NOT NULL CHECK (cantidad > 0),
  precio_unitario DECIMAL(10,2) NOT NULL CHECK (precio_unitario >= 0),
  FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
  FOREIGN KEY (id_producto) REFERENCES productos(id_producto),
  UNIQUE (id_pedido, id_producto)
);

CREATE TABLE pagos (
  id_pago INT PRIMARY KEY AUTO_INCREMENT,
  id_pedido INT NOT NULL UNIQUE,
  metodo ENUM('TARJETA','BIZUM','PAYPAL','TRANSFERENCIA') NOT NULL,
  fecha_pago DATE NOT NULL,
  importe DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
);

-- Índices útiles
CREATE INDEX idx_pedidos_fecha ON pedidos(fecha_pedido);
CREATE INDEX idx_pedidos_cliente ON pedidos(id_cliente);
CREATE INDEX idx_lineas_producto ON lineas_pedido(id_producto);

-- =========================
-- DATOS
-- =========================

INSERT INTO categorias(nombre) VALUES
('Smartphones'),
('Portátiles'),
('Audio'),
('Accesorios');

INSERT INTO productos(nombre, id_categoria, precio_lista, activo) VALUES
('Móvil Orion X',            1, 699.00, 1),
('Móvil Nebula Mini',        1, 399.00, 1),
('Portátil Atlas 14',        2, 899.00, 1),
('Portátil Atlas 16 Pro',    2,1299.00, 1),
('Auriculares Sonik Pro',    3, 149.00, 1),
('Altavoz BoomGo',           3,  89.00, 1),
('Cargador 65W',             4,  35.00, 1),
('Funda Rugged',             4,  25.00, 1),
('Ratón SilentClick',        4,  19.00, 1),
('Teclado Mecánico K9',      4,  79.00, 1),
('Dock USB-C 8en1',          4,  59.00, 1),
('Auriculares Lite',         3,  39.00, 1);

INSERT INTO clientes(nombre, email, pais, ciudad, fecha_alta) VALUES
('Ana Martín',      'ana.martin@correo.com',     'España',    'Madrid',     '2024-02-10'),
('Luis García',     'luis.garcia@correo.com',    'España',    'Sevilla',    '2024-05-15'),
('Marta López',     'marta.lopez@correo.com',    'España',    'Valencia',   '2024-09-01'),
('Carlos Pérez',    'carlos.perez@correo.com',   'España',    'Bilbao',     '2025-01-12'),
('Sofía Romero',    'sofia.romero@correo.com',   'España',    'Barcelona',  '2025-03-03'),
('Hugo Díaz',       'hugo.diaz@correo.com',      'España',    'Granada',    '2025-04-18'),
('Paula Sánchez',   'paula.sanchez@correo.com',  'Portugal',  'Lisboa',     '2024-11-20'),
('João Silva',      'joao.silva@correo.com',     'Portugal',  'Oporto',     '2025-02-01'),
('Inês Costa',      'ines.costa@correo.com',     'Portugal',  'Braga',      '2025-06-30'),
('Marco Bianchi',   'marco.bianchi@correo.com',  'Italia',    'Milán',      '2024-03-22'),
('Giulia Conti',    'giulia.conti@correo.com',   'Italia',    'Roma',       '2025-02-14'),
('Luca Rinaldi',    'luca.rinaldi@correo.com',   'Italia',    'Turín',      '2025-08-09'),
('Elena Torres',    'elena.torres@correo.com',   'España',    'Zaragoza',   '2025-09-10'),
('David Núñez',     'david.nunez@correo.com',    'España',    'Málaga',     '2025-10-05'),
('Clara Vega',      'clara.vega@correo.com',     'España',    'Madrid',     '2025-11-01');

-- Pedidos (mezcla 2024-2026; muchos en 2025)
INSERT INTO pedidos(id_cliente, fecha_pedido, estado) VALUES
(1,'2024-11-25','PAGADO'),
(2,'2024-12-10','ENVIADO'),
(3,'2024-12-28','CANCELADO'),

(4,'2025-01-05','PAGADO'),
(5,'2025-01-20','ENVIADO'),
(6,'2025-02-02','PAGADO'),
(7,'2025-02-10','PAGADO'),
(8,'2025-02-18','CANCELADO'),
(9,'2025-03-07','ENVIADO'),
(10,'2025-03-12','PAGADO'),
(11,'2025-03-25','PAGADO'),
(12,'2025-04-03','ENVIADO'),
(1,'2025-04-18','PAGADO'),
(2,'2025-05-06','PAGADO'),
(3,'2025-05-22','ENVIADO'),
(4,'2025-06-02','PAGADO'),
(5,'2025-06-19','CANCELADO'),
(6,'2025-07-05','ENVIADO'),
(7,'2025-07-20','PAGADO'),
(8,'2025-08-11','PAGADO'),
(9,'2025-08-29','ENVIADO'),
(10,'2025-09-04','PAGADO'),
(11,'2025-09-17','CANCELADO'),
(12,'2025-10-02','PAGADO'),
(13,'2025-10-18','ENVIADO'),
(14,'2025-11-06','PAGADO'),
(15,'2025-11-20','PAGADO'),
(1,'2025-12-02','ENVIADO'),
(2,'2025-12-15','PAGADO'),
(5,'2025-12-28','CANCELADO'),

(4,'2026-01-08','PAGADO'),
(10,'2026-01-22','ENVIADO');

-- Líneas de pedido (UNIQUE por pedido+producto; cantidades/ precios para calcular totales)
-- Nota: precio_unitario puede ser igual a precio_lista o con pequeñas variaciones para simular descuentos

INSERT INTO lineas_pedido(id_pedido, id_producto, cantidad, precio_unitario) VALUES
-- 2024
(1, 7, 2, 35.00),
(1, 8, 1, 25.00),
(2, 5, 1, 149.00),
(2,11, 1, 59.00),
(3, 2, 1, 399.00),

-- 2025
(4, 1, 1, 689.00),
(4, 8, 1, 25.00),

(5, 3, 1, 879.00),
(5, 9, 1, 19.00),

(6, 2, 2, 389.00),
(6, 7, 2, 35.00),

(7, 5, 2, 139.00),
(7, 6, 1, 89.00),
(7,10, 1, 79.00),

(8, 4, 1,1299.00),

(9, 1, 1, 699.00),
(9, 7, 1, 35.00),
(9, 8, 2, 25.00),

(10, 6, 3, 85.00),
(10,12, 2, 35.00),

(11, 3, 1, 899.00),
(11,11, 1, 59.00),
(11, 9, 2, 19.00),

(12, 2, 1, 399.00),
(12, 8, 1, 25.00),

(13, 1, 1, 699.00),
(13, 5, 1, 149.00),

(14, 4, 1,1249.00),
(14,11, 1, 59.00),

(15, 3, 2, 859.00),
(15, 9, 2, 19.00),

(16, 5, 4, 129.00),
(16, 6, 2, 89.00),

(17, 1, 1, 699.00),

(18, 4, 1,1299.00),
(18,10, 1, 79.00),

(19, 2, 3, 379.00),
(19, 7, 3, 35.00),

(20, 3, 1, 899.00),
(20,11, 1, 59.00),

(21, 6, 2, 89.00),
(21,12, 4, 35.00),
(21, 8, 2, 25.00),

(22, 1, 2, 679.00),
(22, 7, 1, 35.00),

(23, 5, 1, 149.00),

(24, 4, 1,1299.00),
(24, 9, 1, 19.00),
(24,11, 1, 59.00),

(25, 2, 1, 399.00),
(25, 8, 2, 25.00),
(25, 7, 1, 35.00),

(26, 3, 1, 899.00),
(26,10, 1, 79.00),
(26, 9, 1, 19.00),

(27, 5, 3, 139.00),
(27, 6, 1, 89.00),

(28, 1, 1, 699.00),
(28,11, 1, 59.00),

(29, 4, 1,1299.00),
(29, 7, 2, 35.00),

(30, 2, 1, 399.00),

-- 2026
(31, 3, 1, 899.00),
(31,11, 1, 59.00),
(32, 6, 1, 89.00),
(32,12, 2, 39.00);

-- Pagos (solo para pedidos NO cancelados; el importe lo calculamos con sumatorio)
-- Para simplificar, fijamos importes coherentes con las líneas.
INSERT INTO pagos(id_pedido, metodo, fecha_pago, importe) VALUES
(1,'BIZUM','2024-11-25', 95.00),
(2,'TARJETA','2024-12-10', 208.00),

(4,'TARJETA','2025-01-05', 714.00),
(5,'PAYPAL','2025-01-20', 898.00),
(6,'BIZUM','2025-02-02',  848.00),
(7,'TARJETA','2025-02-10', 446.00),
(9,'TRANSFERENCIA','2025-03-07', 784.00),
(10,'PAYPAL','2025-03-12', 325.00),
(11,'TARJETA','2025-03-25', 996.00),
(12,'BIZUM','2025-04-03', 424.00),
(13,'TARJETA','2025-04-18', 848.00),
(14,'TARJETA','2025-05-06',1308.00),
(15,'PAYPAL','2025-05-22',1756.00),
(16,'TRANSFERENCIA','2025-06-02', 694.00),
(18,'TARJETA','2025-07-05',1378.00),
(19,'BIZUM','2025-07-20',1242.00),
(20,'PAYPAL','2025-08-11', 958.00),
(21,'TARJETA','2025-08-29', 368.00),
(22,'TRANSFERENCIA','2025-09-04',1393.00),
(23,'BIZUM','2025-10-02', 149.00),
(24,'TARJETA','2025-10-18',1377.00),
(25,'PAYPAL','2025-11-06', 484.00),
(26,'TARJETA','2025-11-20', 997.00),
(27,'BIZUM','2025-12-02', 506.00),
(28,'TRANSFERENCIA','2025-12-15', 758.00),

(31,'TARJETA','2026-01-08', 958.00),
(32,'PAYPAL','2026-01-22', 167.00);

