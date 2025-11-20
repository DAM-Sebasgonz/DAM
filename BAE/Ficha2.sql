CREATE TABLE DetallePedido (
    id_pedido     INT,
    id_producto   INT,
    cantidad      INT NOT NULL,
    precio_unit   DECIMAL(8,2) NOT NULL,
    PRIMARY KEY (__________, __________),
    CONSTRAINT fk_det_pedido
        FOREIGN KEY (id_pedido)
        REFERENCES Pedido(__________)
        ON DELETE ________
        ON UPDATE ________,
    CONSTRAINT fk_det_producto
        FOREIGN KEY (id_producto)
        REFERENCES Producto(id_producto)
        ON DELETE ________
        ON UPDATE ________
);
