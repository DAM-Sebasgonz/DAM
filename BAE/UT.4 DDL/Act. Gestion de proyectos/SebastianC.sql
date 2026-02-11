CREATE USER 'user_Sebastian'@'localhost' IDENTIFIED BY '12345';

GRANT INSERT, DELETE ON Proyectos.* TO 'user_Sebastian'@'localhost';

CREATE USER 'po_Sebastian'@'localhost' ;

GRANT SELECT (FechaAsignación, FechasLimite) ON Proyectos.Tareas TO 'po_Sebastian'@'localhost';

GRANT UPDATE (PorcentajeAvance) ON Proyectos.Avances_Tareas TO 'po_Sebastian'@'localhost';

FLUSH PRIVILEGES;