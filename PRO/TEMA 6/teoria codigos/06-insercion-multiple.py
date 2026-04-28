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
    
    # inserción de datos en la tabla mobile

    query_insertar = """ INSERT INTO mobile (id, model, price) 
                         VALUES (%s,%s,%s);"""
    
    records = [(4, 'LG', 800), (5, 'One Plus 6', 950)]

    result = cursor.executemany(query_insertar, records)
    connection.commit()
    
    count = cursor.rowcount
    print(f"{count} Registros insertados satisfactoriamente")
    
except (Exception, Error) as error:
    print("Error...al intentar conectar con PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("La conexión con PostgreSQL está cerrada")
