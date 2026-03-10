-- 1

select P.nombre, P.departamento
from profesor P
join imparte I
on P.dni = I.DNIProf
join asignatura A
on A.CodAsig = I.CodAsig
where I.curso = "2021"
group by p.nombre;

-- 2

select A.*
from asignaturas A
join imparte I;

-- 3

select A.nombre, count(M.DNI) AS numero_alumnos
from asignatura A
join matricula M
on A.CodAsig = M.CodAsig
join alumnos P
on M.DNI = P.DNI
group by A.nombre;

-- 4

select A.nombre, avg(M.nota)
from asignatura A
join matricula M
on A.DNI = M.DNI
join imparte I
on M.CodAsig = I.Codasig
join profesor P
on P.DNI = I.DNIProf
join departamento D
on P.departamento = D.CodDep
where D.nombre = "Informatica y Comunicaciones";

-- 6

select A.nombre
from asignatura A
join imparte I
on a.CodAsig = I.CodAsig
join profesor P 
where I.Curso = "2022";

-- 7

select A.Nombre, C.siglas
from asignatura A
join matricula 
on A.CodAsig = C.CodAsig 
join Ciclo C
on A.CodCiclo = C.CodCF
where DNI is null; 

-- 8

select A.nombre, M.curso, count(P.DNI) as numero_alumnos
from asignatura A
join matricula M
on M.CodAsig = A.CodAsig
join alumnos P 
where P.bilingue = "S"
group by A.nombre, M.curso;

-- 9 

select A.nombre
from asignatura A
where A.NumHoras > avg(NumHoras)
group by A.nombre;