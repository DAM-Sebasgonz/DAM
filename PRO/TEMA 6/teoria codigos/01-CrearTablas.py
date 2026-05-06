import psycopg2
import os
from psycopg2 import Error
os.environ["PGCLIENTENCODING"] = "utf-8"

try:
    # Conexion a PostgreSQL
    connection = psycopg2.connect(
        user="usrpostgre",
        password="1234",
        host="localhost",
        port="5432",
        database="sistemareservasaerea"
    )

    # Forzar codificacion UTF-8
    connection.set_client_encoding('UTF8')

    cursor = connection.cursor()

    # tabla persona
    query_persona = '''CREATE TABLE persona (
                       nif VARCHAR(10) PRIMARY KEY,
                       nombre_completo VARCHAR(100) NOT NULL,
                       sexo CHAR(1) CHECK (sexo IN ('M', 'F', 'O')), 
                       edad INTEGER CHECK (edad > 0 AND edad <= 120) );'''
               
    cursor.execute(query_persona)
    connection.commit()

    # tabla aerolinea
    query_aerolinea = '''CREATE TABLE aerolinea (
                         codigo_identificacion VARCHAR(5) PRIMARY KEY,
                         nombre VARCHAR(100) NOT NULL,
                         pais VARCHAR(60) NOT NULL);'''

    cursor.execute(query_aerolinea)
    connection.commit()

    # tabla vuelo
    query_vuelo = '''CREATE TABLE vuelo (
                     id_vuelo VARCHAR(7) PRIMARY KEY,  
                     destino VARCHAR(100) NOT NULL,
                     nro_plazas_totales INTEGER CHECK (nro_plazas_totales > 0),
                     fecha_salida DATE NOT NULL,
                     hora_salida TIME NOT NULL,
                     codigo_aerolinea VARCHAR(5) NOT NULL,
                     CONSTRAINT fk_vuelo_aerolinea FOREIGN KEY (codigo_aerolinea)
                        REFERENCES aerolinea(codigo_identificacion)
                        ON DELETE RESTRICT ON UPDATE CASCADE);'''

    cursor.execute(query_vuelo)
    connection.commit()

    # tabla reserva
    query_reserva =  '''CREATE TABLE reserva (
                        nif_persona VARCHAR(10),
                        id_vuelo VARCHAR(7),
                        fecha_reserva DATE,
                        fecha_pago DATE,
                        estado VARCHAR(15) CHECK (estado IN ('reservado', 'pagado', 'utilizado', 'no_usado')) DEFAULT 'reservado',
                        PRIMARY KEY (nif_persona, id_vuelo), 
                        CONSTRAINT fk_reserva_persona FOREIGN KEY (nif_persona)
                            REFERENCES persona(nif) ON DELETE CASCADE ON UPDATE CASCADE,
                        CONSTRAINT fk_reserva_vuelo FOREIGN KEY (id_vuelo)
                            REFERENCES vuelo(id_vuelo) ON DELETE CASCADE ON UPDATE CASCADE,
                        CONSTRAINT check_fecha_pago CHECK (fecha_pago IS NULL OR fecha_pago >= fecha_reserva) );'''

    cursor.execute(query_reserva)
    connection.commit()

    print("Las tablas han sido creadas satisfactoriamente")

except (Exception, Error) as error:
    print("Error al intentar conectar con PostgreSQL:", error)

finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("Conexion cerrada")

