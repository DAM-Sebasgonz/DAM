SELECT nombre,direccion,extension
FROM polideportivos
ORDER BY extension ASC
LIMIT 1;

select nombre, direccion
from polideportivos
where extension = (select min(extension) from polideportivos);

-- 10.- Cuánto dinero costaría alquilar todas las pistas del polideportivo cuyo id es 23. 

SELECT sum(precio) 
from pistas
WHERE id=23
