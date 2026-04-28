-- 1

INSERT INTO citas (dni_paciente, dni_medico, fecha_hora, motivo, estado)
values
((select dni_paciente from pacientes where nombre ="Ana" AND apellidos = "López García"), 
(select dni_medico from medicos where nombre = "Javier" AND apellidos = "Hernandez Soto"),
"2026-04-22 10:30:00"
"Revision de resultados"
"Programada");

-- 2

insert into Diagnosticos (id_cita, descripcion, fecha)
values((
select c.id_cita 
from citas C
join pacientes p on c.dni_paciente = p.dni_cliente
join medicos m  on c.dni_medico = m.dni_medico
where p.nombre = "Luis" and p.apellidos = "Martin Perez" and m.especialidad = "Medicina Familiar" and c.fecha_hora = '2026-03-01 10:15:00'
),"Bronquitis en revisión. Se recomienda continuar control clinico", "2026-03-01");

-- 3
/*
insert into Diagnosticos (id_cita, descripcion, fecha)
select c.id_cita,
"Pendiente de revision."*/


-- 4

update citas
set estado = 'Cancelada'
where id_cita = (select id_cita
from (
select c.id_cita
from citas c
join pacientes p on c.dni_paciente = p.dni_paciente
where p.nombre = 'Ana' and p.apellidos = 'López García' and c.estado    = 'Programada'
order by c.fecha_hora asc
limit 1
) as subconsulta
);

-- 5

update tratamiento t
join diagnosticos d  
on t.id_diagnostico = d.id_diagnostico
join citas c  
on d.id_cita = c.id_cita
join pacientes p 
on c.dni_paciente = p.dni_paciente
set t.observaciones = "Revisión prioritaria"
where p.apellidos like "%García%";


-- 6
/*
update citas 
set fecha_hora = DATE_ADD(fecha_hora, INTERVAL 7 DAY)
where estado = "programada" and motivo like %Revisión% 
and dni_paciente in (
select distinct ) */

-- 7 

delete from Citas
where fecha_hora > NOW()
and dni_paciente in (
select dni_paciente
from Pacientes
where telefono is null);







