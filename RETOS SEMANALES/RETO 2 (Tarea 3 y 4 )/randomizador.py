import random
import mysql.connector

palabras_clave = ['incompetentes', 'denuncia', 'vergüenza', 'lento']

# Función conectar_bd()
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='Hermes IT Support',
            user='root',
            password='1234'
        )
        if conexion.is_connected():
            mensaje = 'Conexión exitosa a la base de datos'
            print(mensaje)
            return conexion
    except mysql.connector.Error as ejecucion_fallida:
        mensaje = f'Error al conectar a la base de datos: {ejecucion_fallida}'
        print(mensaje)
        return None

def modificar_descripciones_aleatoriamente():
    conexion = conectar_bd()
    if not conexion:
        print("No se pudo iniciar el proceso sin conexión a la base de datos.")
        return

    try:
        cursor = conexion.cursor()
        
        cursor.execute("SELECT CodigoTicket FROM Ticket;")
        tickets = cursor.fetchall() 
        
        tickets_modificados = 0

        for (codigo_ticket,) in tickets:
            if random.random() < 0.10: 
                palabra_aleatoria = random.choice(palabras_clave)
                
                query_update = """
                    UPDATE Ticket 
                    SET Descripcion = CONCAT(Descripcion, ' ', %s) 
                    WHERE CodigoTicket = %s;
                """
                cursor.execute(query_update, (palabra_aleatoria, codigo_ticket))
                
                tickets_modificados += 1
        
        conexion.commit()
        print(f"Proceso completado. Se evaluaron {len(tickets)} tickets y se modificaron {tickets_modificados}.")

    except mysql.connector.Error as error:
        print(f"Error durante la actualización de los tickets: {error}")
        conexion.rollback()
        
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión a MySQL cerrada correctamente.")

if __name__ == "__main__":
    modificar_descripciones_aleatoriamente()