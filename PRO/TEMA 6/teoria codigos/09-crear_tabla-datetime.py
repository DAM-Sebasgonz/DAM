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

    query = """CREATE TABLE item (item_id serial NOT NULL PRIMARY KEY, 
	           item_name VARCHAR (100) NOT NULL, 
	           purchase_time timestamp NOT NULL,
	           price INTEGER NOT NULL);"""
               
    # Creamos el cursor y ejecutamos la consulta 
    cursor = connection.cursor()
    cursor.execute(query)
    # consolidamos la modificación de la BD
    connection.commit()
    print("La tabla ha sido creada satisfactoriamente")
except (Exception, Error) as error:
    print("Error...al intentar conectar con PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("La conexión con PostgreSQL está cerrada")
