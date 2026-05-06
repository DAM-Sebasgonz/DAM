import psycopg2
from psycopg2 import Error
from getpass import getpass
import datetime

try:
    # Conectamos a la BD prueba con el usuario usrpostgre
    connection = psycopg2.connect(user="usrpostgre",
                                  password=getpass("Introduzca la contraseña: "),
                                  host="localhost",
                                  port="5432",
                                  database="prueba")

    query = """INSERT INTO item (item_Id, item_name, purchase_time, price) 
                VALUES (%s, %s, %s, %s);"""
    item_purchase_time = datetime.datetime.now()  
    item_tuple = (15, "Keyboard", item_purchase_time, 150)         
    # Creamos el cursor y ejecutamos la consulta 
    cursor = connection.cursor()
    cursor.execute(query, item_tuple)
    # consolidamos la modificación de la BD
    connection.commit()
    count = cursor.rowcount
    print(f"{count} Registro insertado satisfactoriamente")
    
    # Leer PostgreSQL  timestamp en Python datetime
    cursor.execute("SELECT purchase_time from item where item_id = 15")
    purchase_datetime = cursor.fetchone()
    print("Item Purchase date is  ", purchase_datetime[0].date())
    print("Item Purchase time is  ", purchase_datetime[0].time())

except (Exception, Error) as error:
    print("Error...al intentar conectar con PostgreSQL", error)
else:
    if (connection):
        cursor.close()
        connection.close()
        print("La conexión con PostgreSQL está cerrada")
