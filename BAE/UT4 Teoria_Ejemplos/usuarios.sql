CREATE USER 'sebastian_1' IDENTIFIED BY '12345';
CREATE USER 'sebastian_2' IDENTIFIED BY '12345';

GRANT INSERT,DELETE ON pilotos.* TO 'sebastian_1'@'localhost';


GRANT SELECT, INSERT, UPDATE ON pilotos.Carreras TO 'sebastian_2'@'localhost';
GRANT SELECT, INSERT, UPDATE ON pilotos.Resultados TO 'sebastian_2'@'localhost';

SHOW GRANTS FOR 'sebastian_1';
SHOW GRANTS FOR 'sebastian_2';

CREATE USER 'auxiliar';

GRANT SELECT (Nombre, País, Tipo) ON pilotos.Circuitos TO 'auxiliar'@'localhost';

ALTER USER 'sebastian_1'@'localhost' IDENTIFIED BY 'xxx333';