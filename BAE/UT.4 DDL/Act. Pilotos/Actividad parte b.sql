CREATE USER 'sebastian_1'@'localhost' IDENTIFIED BY '12345';
CREATE USER 'sebastian_2'@'localhost' IDENTIFIED BY '12345';

GRANT INSERT, DELETE ON Formula1.* TO 'sebastian_1'@'localhost';

GRANT SELECT, INSERT, UPDATE ON Formula1.CARRERAS TO 'sebastian_2'@'localhost';
GRANT SELECT, INSERT, UPDATE ON Formula1.RESULTADOS TO 'sebastian_2'@'localhost';

SHOW GRANTS FOR 'sebastian_1'@'localhost';
SHOW GRANTS FOR 'sebastian_2'@'localhost';

CREATE USER 'auxiliar'@'localhost' IDENTIFIED BY '12345';
GRANT SELECT (Nombre, Pais, Tipo) ON Formula1.CIRCUITOS TO 'auxiliar'@'localhost';

ALTER USER 'sebastian_1'@'localhost' IDENTIFIED BY 'xxx333';

FLUSH PRIVILEGES;

SHOW GRANTS FOR 'sebastian_1'@'localhost';
SHOW GRANTS FOR 'sebastian_2'@'localhost';
SHOW GRANTS FOR 'auxiliar'@'localhost';