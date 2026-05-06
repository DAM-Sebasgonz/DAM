import psycopg2
from datetime import date
from getpass import getpass

def insertar_datos_ejemplo():
    conn = psycopg2.connect(
        host="localhost",
        database="sistemareservasaerea",
        user="usrpostgre",
        password=getpass("Introduzca la contraseña: "),
    )
    conn.autocommit = True # para activar el autocommit y no hacerlo manualmente
    cur = conn.cursor()

    # Insertar personas
    personas = [
        ('12345678A', 'Juan Pérez', 'M', 30),
        ('23456789B', 'María López', 'F', 25),
        ('34567890C', 'Carlos Ruiz', 'M', 40),
        ('45678901D', 'Ana García', 'F', 35),
    ]

    query_personas = """INSERT INTO persona (nif, nombre_completo, sexo, edad) 
                        VALUES (%s, %s, %s, %s) 
                        ON CONFLICT (nif) DO NOTHING"""
    
    cur.executemany(query_personas,personas)

    # Insertar aerolíneas

    aerolineas = [
        ('IB', 'Iberia', 'España'),
        ('BA', 'British Airways', 'Reino Unido'),
        ('AF', 'Air France', 'Francia'),
        ('LH', 'Lufthansa', 'Alemania'),
    ]

    query_aerolineas = """INSERT INTO aerolinea (codigo_identificacion, nombre, pais) 
                        VALUES (%s, %s, %s) 
                        ON CONFLICT (codigo_identificacion) DO NOTHING;"""

    cur.executemany(query_aerolineas, aerolineas)

    # Insertar vuelos (id_vuelo VARCHAR(7))
    
    vuelos = [
        ('IB1234', 'Madrid', 150, date(2025, 12, 25), '08:30:00', 'IB'),
        ('BA5678', 'Londres', 200, date(2025, 12, 26), '10:00:00', 'BA'),
        ('AF9012', 'París', 180, date(2025, 12, 27), '12:15:00', 'AF'),
        ('LH3456', 'Berlín', 120, date(2025, 12, 28), '14:45:00', 'LH'),
        ('IB7890', 'Nueva York', 300, date(2025, 12, 29), '20:00:00', 'IB'),
    ]

    query_vuelos = """INSERT INTO vuelo (id_vuelo, destino, nro_plazas_totales, fecha_salida, hora_salida, codigo_aerolinea) 
                      VALUES (%s, %s, %s, %s, %s, %s) 
                      ON CONFLICT (id_vuelo) DO NOTHING;"""

    cur.executemany(query_vuelos, vuelos)

    # Insertar reservas (fecha_reserva y fecha_pago son DATE)
    reservas = [
        ('12345678A', 'IB1234', date(2025, 11, 1), date(2025, 11, 2), 'pagado'),
        ('12345678A', 'BA5678', date(2025, 11, 5), None, 'reservado'),
        ('23456789B', 'IB1234', date(2025, 11, 3), date(2025, 11, 4), 'pagado'),
        ('23456789B', 'AF9012', date(2025, 11, 10), date(2025, 11, 10), 'utilizado'),
        ('34567890C', 'LH3456', date(2025, 11, 8), None, 'reservado'),
        ('34567890C', 'IB7890', date(2025, 11, 12), date(2025, 11, 13), 'pagado'),
        ('45678901D', 'BA5678', date(2025, 11, 7), date(2025, 11, 8), 'utilizado'),
        ('45678901D', 'AF9012', date(2025, 11, 9), None, 'no_usado'),
    ]

    query_reservas = """INSERT INTO reserva (nif_persona, id_vuelo, fecha_reserva, fecha_pago, estado) 
                      VALUES (%s, %s, %s, %s, %s)
                      ON CONFLICT (nif_persona, id_vuelo) DO NOTHING;"""

    cur.executemany(query_reservas, reservas)

    cur.close()
    conn.close()
    print("Datos de ejemplo insertados correctamente.")

if __name__ == "__main__":
    insertar_datos_ejemplo()