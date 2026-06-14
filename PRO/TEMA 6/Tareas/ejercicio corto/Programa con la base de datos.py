import psycopg2
from psycopg2 import Error
from getpass import getpass

print("Base de datos\n")

try:
    contrasenia = getpass("Contraseña de usrpostgre: ")

    conexion = psycopg2.connect(
        user="usrpostgre",
        password=contrasenia,
        host="localhost",
        port="5432",
        database="postgres"
    )
    cursor = conexion.cursor()

    consultaCrearBd = "CREATE DATABASE ejercicio01"

    try:
        cursor.execute(consultaCrearBd)
        print("Base de datos 'ejercicio01' creada con éxito.")
    except (Exception, Error):
        print("La base de datos 'ejercicio01' ya existía o no se pudo crear.")

    cursor.close()
    conexion.close()

except (Exception, Error) as error:
    print("Error inicial en el servidor:", error)
    exit()


try:
    conexion = psycopg2.connect(
        user="usrpostgre",
        password=contrasenia,
        host="localhost",
        port="5432",
        database="ejercicio01"
    )
    cursor = conexion.cursor()

    consultaTablaEmpleados = """
        CREATE TABLE Empleados (
            nif VARCHAR(9) PRIMARY KEY,
            nombre_completo VARCHAR(100) NOT NULL,
            direccion VARCHAR(200),
            municipio VARCHAR(100),
            estado_civil VARCHAR(20),
            nro_hijos INTEGER
        )
    """
    cursor.execute(consultaTablaEmpleados)

    consultaTablaEmpresas = """
        CREATE TABLE Empresas (
            cif VARCHAR(10) PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            fecha_creacion DATE,
            municipio VARCHAR(100)
        )
    """
    cursor.execute(consultaTablaEmpresas)

    consultaTablaTrabajan = """
        CREATE TABLE Trabajan (
            nif_empleado VARCHAR(9) REFERENCES Empleados(nif),
            cif_empresa VARCHAR(10) REFERENCES Empresas(cif),
            fecha_inicio DATE,
            salario_paga NUMERIC(10,2),
            tipo_trabajo VARCHAR(50),
            PRIMARY KEY (nif_empleado, cif_empresa, fecha_inicio)
        )
    """
    cursor.execute(consultaTablaTrabajan)

    conexion.commit()
    print("Tablas de la base de datos creadas correctamente.")

    consultaInsParo = "INSERT INTO Empresas VALUES ('9999', 'Paro', '2000-01-01', 'General')"
    cursor.execute(consultaInsParo)

    consultaInsEmpresa1 = "INSERT INTO Empresas VALUES ('A12345678', 'Tech Solutions SL', '2010-05-15', 'Santa Cruz')"
    cursor.execute(consultaInsEmpresa1)
    consultaInsEmpresa2 = "INSERT INTO Empresas VALUES ('B87654321', 'Consultores Asociados', '2015-03-20', 'La Laguna')"
    cursor.execute(consultaInsEmpresa2)
    consultaInsEmpresa3 = "INSERT INTO Empresas VALUES ('C11111111', 'Comercial del Norte', '2008-11-10', 'Los Realejos')"
    cursor.execute(consultaInsEmpresa3)

    consultaInsEmpleado1 = "INSERT INTO Empleados VALUES ('12345678A', 'Juan Pérez García', 'Calle Mayor 1', 'Santa Cruz', 'Soltero', 0)"
    cursor.execute(consultaInsEmpleado1)
    consultaInsEmpleado2 = "INSERT INTO Empleados VALUES ('87654321B', 'María López Díaz', 'Avenida 2', 'La Laguna', 'Casado', 2)"
    cursor.execute(consultaInsEmpleado2)
    consultaInsEmpleado3 = "INSERT INTO Empleados VALUES ('11111111C', 'Carlos Rodríguez', 'Plaza 3', 'Los Realejos', 'Soltero', 1)"
    cursor.execute(consultaInsEmpleado3)
    consultaInsEmpleado4 = "INSERT INTO Empleados VALUES ('22222222D', 'Ana González', 'Calle 4', 'Puerto de la Cruz', 'Casado', 3)"
    cursor.execute(consultaInsEmpleado4)
    consultaInsEmpleado5 = "INSERT INTO Empleados VALUES ('33333333E', 'Pedro Sánchez', 'Avenida 5', 'Santa Cruz', 'Divorciado', 1)"
    cursor.execute(consultaInsEmpleado5)

    consultaInsRelacion1 = "INSERT INTO Trabajan VALUES ('12345678A', 'A12345678', '2020-01-10', 2500.00, 'Desarrollador')"
    cursor.execute(consultaInsRelacion1)
    consultaInsRelacion2 = "INSERT INTO Trabajan VALUES ('87654321B', 'B87654321', '2019-06-15', 2200.00, 'Analista')"
    cursor.execute(consultaInsRelacion2)
    consultaInsRelacion3 = "INSERT INTO Trabajan VALUES ('11111111C', 'C11111111', '2021-02-20', 1800.00, 'Vendedor')"
    cursor.execute(consultaInsRelacion3)
    consultaInsRelacion4 = "INSERT INTO Trabajan VALUES ('22222222D', 'A12345678', '2018-09-01', 2800.00, 'Project Manager')"
    cursor.execute(consultaInsRelacion4)
    consultaInsRelacion5 = "INSERT INTO Trabajan VALUES ('33333333E', '9999', '2023-01-01', 0.00, 'En búsqueda activa')"
    cursor.execute(consultaInsRelacion5)

    conexion.commit()
    print("Datos iniciales cargados con éxito.")

    cursor.close()
    conexion.close()

except (Exception, Error) as error:
    print("Error al estructurar o rellenar la base de datos:", error)
    exit()
    
