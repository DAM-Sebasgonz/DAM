-- Muestra el listado de las categorias que tienen asociados mas de 4 productos

select c.nombre, count(p.id) as NumProductos
from categorias C join productos p
	on C.id = p.categoria_id
group by C.id
having NumProductos > 4
order by NumProductos DESC;

-- Muestra el listado de clientes que no han saldado el importe de alguno de los pedidos que haya realizado

select 