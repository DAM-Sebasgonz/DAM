import psycopg2
from datetime import date
from getpass import getpass

# Configuración de conexión

def conectar():
    return psycopg2.connect(user="usrpostgre",
                            password=getpass("Introduzca la contraseña: "),
                            host="localhost",
                            port="5432",
                            database="sistemareservasaerea")

def mostrar_menu():
    print("\n" + "=" * 50)
    print("SISTEMA DE GESTIÓN DE RESERVAS AÉREAS")
    print("=" * 50)
    print("1. Insertar persona")
    print("2. Insertar aerolínea")
    print("3. Insertar vuelo")
    print("4. Insertar reserva")
    print("5. Modificar persona")
    print("6. Modificar vuelo")
    print("7. Modificar reserva")
    print("8. Consultar personas")
    print("9. Consultar vuelos")
    print("10. Consultar reservas")
    print("11. Borrar persona")
    print("12. Borrar vuelo")
    print("13. Borrar reserva")
    print("14. CONSULTAS ESPECIALES")
    print("0. Salir")
    print("=" * 50)

def menu_consultas_especiales():
    print("\n--- CONSULTAS ESPECIALES ---")
    print("1. Personas que viajan en un vuelo determinado")
    print("2. Cuántas veces ha viajado una persona (por NIF)")
    print("3. Aerolínea que ha llevado a más personas")
    print("0. Volver al menú principal")
    op = input("Seleccione consulta: ")
    return op

# ==================== CRUD PERSONA ====================

def insertar_persona(conn):
    nif = input("NIF: ")
    nombre = input("Nombre completo: ")
    sexo = input("Sexo (M/F/O): ")
    edad = input("Edad: ")
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO persona (nif, nombre_completo, sexo, edad) VALUES (%s, %s, %s, %s)", (nif, nombre, sexo, edad))
        conn.commit()
        print("Persona insertada correctamente.")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    else:
        cur.close()

def modificar_persona(conn):
    nif = input("NIF de la persona a modificar: ")
    nuevo_nombre = input("Nuevo nombre completo (dejar vacío para no cambiar): ")
    nueva_edad = input("Nueva edad (dejar vacío para no cambiar): ")
    try:
        cur = conn.cursor()
        if nuevo_nombre:
            cur.execute("UPDATE persona SET nombre_completo = %s WHERE nif = %s", (nuevo_nombre, nif))
        n_reg_afectados = cur.rowcount
        if n_reg_afectados > 0:
            if nueva_edad:
                cur.execute("UPDATE persona SET edad = %s WHERE nif = %s", (nueva_edad, nif))
                conn.commit()
            print(f"Persona del {nif} ha modificada correctamente.")
        else:
            print(f"El nif {nif} no se encuentra en la BD.")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    else:
        cur.close()

def consultar_personas(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM persona ORDER BY nif")
    rows = cur.fetchall()
    print("\n--- LISTA DE PERSONAS ---")
    for row in rows:
        print(f"NIF: {row[0]}, Nombre: {row[1]}, Sexo: {row[2]}, Edad: {row[3]}")
    cur.close()

def borrar_persona(conn):
    nif = input("NIF de la persona a borrar: ")
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM persona WHERE nif = %s", (nif,))
        conn.commit()
        n_reg_afectados = cur.rowcount
        if n_reg_afectados > 0:
            print(f"Persona con NIF {nif} borrada (y sus reservas asociadas por CASCADE).")
        else:
            print(f"\nPersona con NIF {nif} NO se encuentra en la BD")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    else:
        cur.close()

# ==================== CRUD AEROLÍNEA ====================

def insertar_aerolinea(conn):
    cod = input("Código identificación: ")
    nombre = input("Nombre: ")
    pais = input("País: ")
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO aerolinea (codigo_identificacion, nombre, pais) VALUES (%s, %s, %s)", (cod, nombre, pais) )
        conn.commit()
        print("Aerolínea insertada correctamente.")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    else:
        cur.close()

def modificar_aerolinea(conn):
    cod_aerolinea = input("Código de la aerolínea: ")
    nuevo_nombre = input("Nuevo nombre aerolinea (dejar vacío para no cambiar): ")
    nuevo_pais = input("Nueva país sede (dejar vacío para no cambiar): ")
    try:
        cur = conn.cursor()
        if nuevo_nombre:
            cur.execute("UPDATE aerolinea SET nombre = %s WHERE nif = %s", (nuevo_nombre, cod_aerolinea))
        n_reg_afectados = cur.rowcount
        if n_reg_afectados > 0:
            if nuevo_pais:
                cur.execute("UPDATE aerolinea SET pais = %s WHERE nif = %s", (nuevo_pais, cod_aerolinea))
                conn.commit()
            print(f"La Aerolinea de {cod_aerolinea} ha sido modificada correctamente.")
        else:
            print(f"La Aerolínea de código {cod_aerolinea} no se encuentra en la BD.")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    else:
        cur.close()

def consultar_aerolineas(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM aerolinea ORDER BY cod_identificacion")
    rows = cur.fetchall()
    print("\n--- LISTA DE PERSONAS ---")
    for row in rows:
        print(f"NIF: {row[0]}, Nombre: {row[1]}, Sexo: {row[2]}, Edad: {row[3]}")
    cur.close()

def borrar_aerolinea(conn):
    cod_aerolinea = input("Código de la aerolínea: ")
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM aerolinea WHERE nif = %s", (cod_aerolinea,))
        conn.commit()
        n_reg_afectados = cur.rowcount
        if n_reg_afectados > 0:
            print(f"La Aerolínea con código {cod_aerolinea} ha sido borrada (y sus reservas asociadas por CASCADE).")
        else:
            print(f"\nLa Aerolínea con código {cod_aerolinea} NO se encuentra en la BD")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    else:
        cur.close()

# ==================== CRUD VUELO ====================

def insertar_vuelo(conn):
    id_vuelo = input("ID Vuelo (VARCHAR(7)): ")
    destino = input("Destino: ")
    plazas = input("Número de plazas totales: ")
    fecha_salida = input("Fecha salida (AAAA-MM-DD): ")
    hora_salida = input("Hora salida (HH:MM:SS): ")
    cod_aerolinea = input("Código aerolínea: ")
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO vuelo (id_vuelo, destino, nro_plazas_totales, fecha_salida, hora_salida, codigo_aerolinea) VALUES (%s, %s, %s, %s, %s, %s)",
            (id_vuelo, destino, plazas, fecha_salida, hora_salida, cod_aerolinea)
        )
        conn.commit()
        print("Vuelo insertado correctamente.")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    else:
        cur.close()

def modificar_vuelo(conn):
    id_vuelo = input("ID del vuelo a modificar: ")
    nuevo_destino = input("Nuevo destino (dejar vacío para no cambiar): ")
    nuevas_plazas = input("Nuevas plazas (dejar vacío para no cambiar): ")
    try:
        cur = conn.cursor()
        if nuevo_destino:
            cur.execute("UPDATE vuelo SET destino = %s WHERE id_vuelo = %s", (nuevo_destino, id_vuelo))
        n_reg_afectados = cur.rowcount
        if n_reg_afectados > 0:
            if nuevas_plazas:
                cur.execute("UPDATE vuelo SET nro_plazas_totales = %s WHERE id_vuelo = %s", (nuevas_plazas, id_vuelo))
            conn.commit()
            print(f"El vuelo con id {id_vuelo} ha sido modificado correctamente.")
        else:
            print(f"El vuelo con id {id_vuelo} no está en la BD.")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    else:
        cur.close()

def consultar_vuelos(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM vuelo ORDER BY fecha_salida")
    rows = cur.fetchall()
    print("\n--- LISTA DE VUELOS ---")
    for row in rows:
        print(f"ID: {row[0]}, Destino: {row[1]}, Plazas: {row[2]}, Fecha: {row[3]}, Hora: {row[4]}, Aerolínea: {row[5]}")
    cur.close()

def borrar_vuelo(conn):
    id_vuelo = input("ID del vuelo a borrar: ")
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM vuelo WHERE id_vuelo = %s", (id_vuelo,))
        conn.commit()
        n_reg_afectados = cur.rowcount
        if n_reg_afectados > 0:
            print(f"Vuelo {id_vuelo} ha sido borrado (y sus reservas asociadas por CASCADE).")
        else:
            print(f"El vuelo con id {id_vuelo} no se encuentra en la BD.")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    else:
        cur.close()

# ==================== CRUD RESERVA ====================

def insertar_reserva(conn):
    nif = input("NIF persona: ")
    id_vuelo = input("ID Vuelo: ")
    fecha_reserva = input("Fecha reserva (AAAA-MM-DD): ")
    fecha_pago = input("Fecha pago (AAAA-MM-DD, dejar vacío si NULL): ")
    estado = input("Estado (reservado/pagado/utilizado/no_usado): ")
    fecha_pago = fecha_pago if fecha_pago else None
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO reserva (nif_persona, id_vuelo, fecha_reserva, fecha_pago, estado) VALUES (%s, %s, %s, %s, %s)",
            (nif, id_vuelo, fecha_reserva, fecha_pago, estado)
        )
        conn.commit()
        print("Reserva insertada correctamente.")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    else:
        cur.close()

def modificar_reserva(conn):
    nif = input("NIF persona de la reserva: ")
    id_vuelo = input("ID Vuelo de la reserva: ")
    nuevo_estado = input("Nuevo estado (dejar vacío para no cambiar): ")
    nueva_fecha_pago = input("Nueva fecha pago (AAAA-MM-DD, dejar vacío para no cambiar): ")
    try:
        cur = conn.cursor()
        if nuevo_estado:
            cur.execute("UPDATE reserva SET estado = %s WHERE nif_persona = %s AND id_vuelo = %s",
                        (nuevo_estado, nif, id_vuelo))
            n_reg_afectados = cur.rowcount
            if n_reg_afectados > 0:
                if nueva_fecha_pago:
                    cur.execute("UPDATE reserva SET fecha_pago = %s WHERE nif_persona = %s AND id_vuelo = %s",
                                (nueva_fecha_pago, nif, id_vuelo))
            conn.commit()
            print("Reserva ha sido modificada correctamente.")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    else:
        cur.close()

def consultar_reservas(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM reserva ORDER BY fecha_reserva")
    rows = cur.fetchall()
    print("\n--- LISTA DE RESERVAS ---")
    for row in rows:
        print(f"Persona: {row[0]}, Vuelo: {row[1]}, Fecha Reserva: {row[2]}, Fecha Pago: {row[3]}, Estado: {row[4]}")
    cur.close()

def borrar_reserva(conn):
    nif = input("NIF persona de la reserva: ")
    id_vuelo = input("ID Vuelo de la reserva: ")
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM reserva WHERE nif_persona = %s AND id_vuelo = %s", (nif, id_vuelo))
        conn.commit()
        n_reg_afectados = cur.rowcount
        if n_reg_afectados > 0:
            print("Reserva borrada correctamente.")
        else:
            print(f"La Reserva con nif {nif} e id vuelo {id_vuelo} no se encuentra en la BD.")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()
    else:
        cur.close()

# ==================== CONSULTAS ESPECIALES ====================

def personas_en_vuelo(conn):
    id_vuelo = input("ID del vuelo: ")
    cur = conn.cursor()
    cur.execute("""
        SELECT p.nif, p.nombre_completo, p.edad
        FROM persona p
        JOIN reserva r ON p.nif = r.nif_persona
        WHERE r.id_vuelo = %s
    """, (id_vuelo,))
    rows = cur.fetchall()
    if rows:
        print(f"\n--- PERSONAS QUE VIAJAN EN EL VUELO {id_vuelo} ---")
        for row in rows:
            print(f"NIF: {row[0]}, Nombre: {row[1]}, Edad: {row[2]}")
    else:
        print(f"No hay personas en el vuelo {id_vuelo}")
    cur.close()

def veces_viajado_por_persona(conn):
    nif = input("NIF de la persona: ")
    cur = conn.cursor()
    cur.execute("""
        SELECT COUNT(*) 
        FROM reserva 
        WHERE nif_persona = %s
    """, (nif,))
    count = cur.fetchone()[0]
    print(f"La persona con NIF {nif} ha viajado {count} veces.")
    cur.close()

def aerolinea_mas_personas(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT a.codigo_identificacion, a.nombre, COUNT(DISTINCT r.nif_persona) as num_personas
        FROM aerolinea a
        JOIN vuelo v ON a.codigo_identificacion = v.codigo_aerolinea
        JOIN reserva r ON v.id_vuelo = r.id_vuelo
        GROUP BY a.codigo_identificacion, a.nombre
        ORDER BY num_personas DESC
        LIMIT 1
    """)
    row = cur.fetchone()
    if row:
        print(f"\n--- AEROLÍNEA CON MÁS PERSONAS ---")
        print(f"Código: {row[0]}, Nombre: {row[1]}, Número de personas distintas: {row[2]}")
    else:
        print("No hay datos suficientes para determinar la aerolínea con más personas.")
    cur.close()

# ==================== PROGRAMA PRINCIPAL ====================
def main():
    conn = conectar()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            insertar_persona(conn)
        elif opcion == "2":
            insertar_aerolinea(conn)
        elif opcion == "3":
            insertar_vuelo(conn)
        elif opcion == "4":
            insertar_reserva(conn)
        elif opcion == "5":
            modificar_persona(conn)
        elif opcion == "6":
            modificar_vuelo(conn)
        elif opcion == "7":
            modificar_reserva(conn)
        elif opcion == "8":
            consultar_personas(conn)
        elif opcion == "9":
            consultar_vuelos(conn)
        elif opcion == "10":
            consultar_reservas(conn)
        elif opcion == "11":
            borrar_persona(conn)
        elif opcion == "12":
            borrar_vuelo(conn)
        elif opcion == "13":
            borrar_reserva(conn)
        elif opcion == "14":
            while True:
                subop = menu_consultas_especiales()
                if subop == "1":
                    personas_en_vuelo(conn)
                elif subop == "2":
                    veces_viajado_por_persona(conn)
                elif subop == "3":
                    aerolinea_mas_personas(conn)
                elif subop == "0":
                    break
                else:
                    print("Opción no válida")
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
    
    conn.close()

if __name__ == "__main__":
    main()