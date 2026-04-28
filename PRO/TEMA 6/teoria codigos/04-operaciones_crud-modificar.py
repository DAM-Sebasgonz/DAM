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
    
    # modificación de datos en la tabla mobile
    query_modificar = """UPDATE mobile SET price = 1500 WHERE id = 1"""
    cursor.execute(query_modificar)
    connection.commit()
    count = cursor.rowcount
    print(f"{count} Registro modificado satisfactoriamente")

    # obtener resutado de inserción (ejecución select de la tabla)
    cursor.execute("SELECT * from mobile")
    registro = cursor.fetchall()
    print("Result ", registro)
except (Exception, Error) as error:
    print("Error...al intentar conectar con PostgreSQL", error)
finally:
    if (connection):
        # cursor.close()
        connection.close()
        print("La conexión con PostgreSQL está cerrada")
