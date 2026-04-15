
-- 1.- Devuelve un listado con los datos de todas las alumnas que se han matriculado alguna vez
-- en el Grado en Ingeniería Informática (Plan 2015)

SELECT DISTINCT p.*
FROM persona p
JOIN alumno_se_matricula_asignatura m 
	ON p.id = m.id_alumno
JOIN asignatura a 
	ON m.id_asignatura = a.id
JOIN grado g 
	ON a.id_grado = g.id
WHERE p.sexo = 'M';

-- 2.- Devuelve un listado de los profesores junto con el nombre del departamento al que están
-- vinculados. El listado debe devolver cuatro columnas, primer apellido, segundo apellido,
-- nombre y nombre del departamento. El resultado estará ordenado alfabéticamente de menor a
 -- mayor por los apellidos y el nombre. 
 
SELECT p.apellido1, p.apellido2, p.nombre, p.nombre, d.nombre as nombre_departamento
from persona P
join profesor PF
on p.id = pf.id_profesor
join departamento D
on pf.id_departamento = d.id
order by apellido1 asc;
    

 
 