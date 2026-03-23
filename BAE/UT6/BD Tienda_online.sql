-- Para una tienda en línea de productos informáticos, se ha diseñado una base de datos relacional con 7 tablas 
-- principales. Este esquema permite gestionar usuarios (clientes y administradores), catálogo de productos, 
-- pedidos de clientes, detalles de cada pedido, categorías de productos, pagos que realizan los clientes para
-- abonar los pedidos y reseñas de clientes sobre los productos.
-- A continuación se presenta la estructura de las tablas.

-- RELACIONES ENTRE TABLAS:
-- Un Usuario puede realizar múltiples Pedidos (1:N). Cada pedido registra qué usuario lo realizó.
-- Cada Pedido puede contener varios Productos a través de la tabla de Detalles_Pedido (relación uno a muchos entre 
-- Pedidos y Detalles_Pedido).
-- Un Producto puede aparecer en muchos pedidos (a través de Detalles_Pedido); lo que implica que hay una relación
-- M:N entre Productos y Pedidos. La tabla Detalles_Pedido es la resultante de dicha relación.
-- Además, cada producto pertenece a una Categoría (1:N entre Categorias y Productos).
-- Los Usuarios pueden escribir Reseñas/opiniones de productos, pero sólo una reseña por producto (1:N entre Usuarios 
-- y Opiniones). Por supuesto, para un mismo producto cada usuario tiene su opinión. Relación M:N Usuarios - Productos.
-- Productos y Reseñas).
-- Un cliente puede abonar un pedido realizando varios pagos o bien de una sola vez. Si realiza varios pagos, éstos
-- deben efectuarse en fechas distintas.

CREATE SCHEMA IF NOT EXISTS tienda_online;
USE tienda_online;

-- TABLA USUARIOS: almacena los usuarios registrados (clientes y administradores).
CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(70) NOT NULL UNIQUE,
    password VARCHAR(10) NOT NULL,
    rol VARCHAR(10) NOT NULL CHECK (rol IN ('admin','cliente'))
)ENGINE = InnoDB;

-- TABLA CATEGORÍAS: Contiene las categorías de productos (por ejemplo: laptops, periféricos, componentes, etc.).
CREATE TABLE Categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
) ENGINE = InnoDB;

-- TABLA PRODUCTOS: Catálogo de productos de la tienda. Cada producto pertenece a una categoría (FK a Categorias).
CREATE TABLE Productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL CHECK (precio >= 0),
    stock INT UNSIGNED NOT NULL DEFAULT 0 CHECK (stock >= 0),
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES Categorias(id) 
        ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE = InnoDB;

-- TABLA PEDIDOS: Registra los pedidos/ventas realizados por los usuarios. Cada pedido está asociado a un usuario (FK a Usuarios).
CREATE TABLE Pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id) 
        ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE = InnoDB;

-- TABLA DETALLES_PEDIDO: Almacena el detalle de cada pedido (línea de pedido). Cada registro indica un producto
-- comprado en un pedido determinado, con su cantidad y precio unitario. Tiene FKs al pedido y al producto 
-- correspondientes.
CREATE TABLE Detalles_Pedido (
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL CHECK (cantidad > 0),
    precio DECIMAL(10,2) NOT NULL CHECK (precio >= 0),
    PRIMARY KEY (pedido_id, producto_id),
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(id) 
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES Productos(id) 
        ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE = InnoDB;

-- TABLA PAGOS: Registra los pagos que realizan los clientes de los pedidos que han realizado. Un cliente puede abonar
-- un pedido de varias veces. Por simplificar el modelo; un cliente sólo puede realizar un pago al día. También el usuario
-- puede abonar completamente el pedido en un solo pago.
CREATE TABLE Pagos (
    pedido_id INT NOT NULL,
    fecha_pago DATE NOT NULL,
    PRIMARY KEY (pedido_id, fecha_pago),
    pago DECIMAL(10,2) NOT NULL CHECK (pago >= 0),
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
) ENGINE = InnoDB;

-- TABLA OPINIONES: Guarda las reseñas u opiniones que los usuarios dejan sobre los productos, incluyendo una 
-- calificación numérica. Cada reseña referencia al producto y al usuario correspondiente. Se asegura que un mismo 
-- usuario no escriba más de una reseña por producto.
CREATE TABLE Opiniones (
    producto_id INT NOT NULL,
    usuario_id INT NOT NULL,
    calificacion TINYINT NOT NULL CHECK (calificacion BETWEEN 1 AND 5),
    comentario TEXT,
    PRIMARY KEY (producto_id, usuario_id),
    FOREIGN KEY (producto_id) REFERENCES Productos(id) 
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(id) 
        ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE = InnoDB;




