import psycopg2
from psycopg2 import Error
from getpass import getpass

try:
    # Conectamos a la BD prueba con el usuario usrpostgre
    connection = psycopg2.connect(user="usrpostgre",
                                  password=getpass("Introduzca la contraseña: "),
                                  host="localhost",
                                  port="5432",
                                  database="prueba")

    cursor = connection.cursor()
    
    # borrado de datos en la tabla mobile

    query_insertar = """Delete from mobile where id = %s"""
    records = [(5,), (4,), (3,)]

    result = cursor.executemany(query_insertar, records)
   
    connection.commit()
    
    count = cursor.rowcount
    print(f"{count} Registros borrados satisfactoriamente")

    # tener en cuenta que el número de registro que se borran es distinto
    # al número de tuplas que hay en la lista (la tercera tupla no está en la tabla)
    # y no por ello da un error (el error es de lógica no de funcionamiento del algoritmo)

except (Exception, Error) as error:
    print("Error...al intentar conectar con PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("La conexión con PostgreSQL está cerrada")
