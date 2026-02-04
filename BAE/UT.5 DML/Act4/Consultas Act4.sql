-- ¿Cuántas obras hay en el museo del Prado?

SELECT M.id_museos, COUNT(O.id_obras) AS cantidad
FROM obras O
JOIN museos M
ON O.id_museos = M.id_museos
WHERE M.nombre = 'El Prado'
GROUP BY M.id_museos;

-- ¿Cuántas obras ha creado Pablo Picasso?

Select a.id_autor, count(o.id_obras) as cantidad
from obra_autor O
JOIN autores A
on a.id_autor = o.id_autor
where nombre = "Picasso"
group by a.id_autor;

-- Título de las obras que hay en el museo Reina Sofía, ordenado por título

SELECT nombre, titulo
FROM museos M JOIN obras O
ON M.id_museos = O.id_museos
WHERE nombre = 'Reina SofÃa'
ORDER BY(titulo);

-- Nombre y dirección de los museos de España, ordenado por nombre

SELECT nombre, direccion
FROM museos
WHERE pais = 'España'
ORDER BY nombre ASC;

-- Título de la obra y autor de aquellas obras de autores extranjeros que se encuentran en España, ordenado por autores



-- ¿Cuántas obras las han realizado autores españoles?

SELECT a.id_autor, COUNT(oa.id_obras) AS cantidad
FROM autores a
JOIN obra_autor oa 
ON a.id_autor = oa.id_autor
WHERE a.nacionalidad = 'Española'
GROUP BY a.id_autor;

-- ¿Cuántos museos hay?

Select count(id_museos) as cantidad_museos
from museos;

-- ¿Cuántas obras hay en cada museo?

Select id_museos, count(id_obras) as cantidad_obras_museos








