INSERT INTO Pedidos (usuario_id, fecha)
VALUES (
    (SELECT id FROM Usuarios WHERE email = 'lucia.torres@example.com'),
    '2025-03-20'
);

-- Se sobreenentiende que id es autoincremental, por lo que no es necesario especificarlo en la inserción.

INSERT INTO Productos (nombre, descripcion, precio, stock, categoria_id)
VALUES ('Webcam Logitech HD',NULL,49.99,14,
(SELECT id FROM Categorias WHERE nombre = 'Periféricos')
);

INSERT INTO Opiniones (producto_id, usuario_id, calificacion, comentario)
VALUES (
    (SELECT id FROM Productos WHERE nombre = 'Mouse Gaming Razer DeathAdder'),
    (SELECT id FROM Usuarios WHERE nombre = 'Felipe Mendez'),
    5,
    'Muy preciso y cómodo'
);

INSERT INTO Pagos (pedido_id, fecha_pago, pago)
VALUES (50, '2025-03-16', 60.00);

INSERT INTO Detalles_Pedido (pedido_id, producto_id, cantidad, precio)
SELECT 
49,
p.id,
2,
p.precio * 2
FROM Productos p
JOIN Categorias c ON p.categoria_id = c.id
WHERE c.nombre = 'Almacenamiento'
ORDER BY p.precio ASC
LIMIT 1;

-- Ejercicios de update

UPDATE Productos
SET precio = precio * 1.08
WHERE categoria_id = (SELECT id FROM Categorias WHERE nombre = 'Laptops');

UPDATE Productos
SET stock = stock + 5
WHERE stock < 10;

UPDATE Usuarios
SET rol = 'admin'
WHERE email = 'carmen.cruz@example.com';

UPDATE Productos
SET stock = stock - 2
WHERE nombre = 'SSD Samsung 500GB';

UPDATE Opiniones
SET comentario = 'Muy buen teclado para uso diario'
WHERE usuario_id = 25 AND producto_id = 10;

UPDATE Productos
SET precio = precio * 1.05
WHERE id IN (
SELECT producto_id
FROM Opiniones
GROUP BY producto_id
HAVING AVG(calificacion) >= 4.5
);

UPDATE Productos
SET precio = precio * 0.90
WHERE id NOT IN (
    SELECT DISTINCT producto_id FROM Opiniones
);

-- Ejercicios de delete

DELETE FROM Opiniones
WHERE usuario_id = 23 AND producto_id = 9;

DELETE FROM Pagos
WHERE pedido_id = 50 AND fecha_pago = '2025-01-22';

DELETE FROM Pagos
WHERE pedido_id IN (
SELECT p.id
FROM Pedidos p
JOIN Usuarios u ON p.usuario_id = u.id
WHERE u.email = 'gabriel.roman@example.com'
);


