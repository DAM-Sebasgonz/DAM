-- Top 5 clientes por gasto en 2025

select cli.nombre, pa.pais
from clientes C
join pedidos P
On cli.nombre = 
where estado != "cancelado"
limit 5

-- Clientes que nunca han comprado

select c.nombre
from pedidos p
join clientes c
on p.id_cliente = c.id_cliente
where pedidos = "cancelado"

-- clientes de españa o portugal que hicieron pedidos pagados en 2025

select c.nombre, c.pais
from pedidos P
join clientes C
on P.id_cliente = C.id_cliente
where C.pais = "España" and "Portugal"

-- Nº de productos vendidos por cada categoria, siempre y cuando ese total sea inferior a 5 usar having

select cat.nombre, count(c.cantidad) as cantidad_pro
from categorias CA
join productos PR
on CA.

-- importe total vendido en 2025 segun la modalidad de pago

select p.metodo, p.fecha_pago ,sum(importe) as cantidad
from pagos P
where Year(p.fecha_pago) = 2025
group by p.metodo
