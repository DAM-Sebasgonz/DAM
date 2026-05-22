from datetime import datetime, timedelta
import mysql.connector
from faker import Faker
import random

fake = Faker('es_ES')

# Función escribir_log(mensaje)
def escribir_log(mensaje):
    ahora = datetime.now()
    linea = ahora.strftime("[%Y-%m-%d %H:%M:%S] ") + 'INFO: ' + mensaje
    with open('seed_log.txt', 'a', encoding='utf-8') as archivo_log:
        archivo_log.write(linea + '\n')


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
            escribir_log(mensaje)
            return conexion
    except mysql.connector.Error as ejecucion_fallida:
        mensaje = f'Error al conectar a la base de datos: {ejecucion_fallida}'
        print(mensaje)
        escribir_log(mensaje)
        return None


# Función generar_catalogos()
def generar_catalogos(conexion):
    cursor = conexion.cursor()

    categorias = ['Hardware', 'Software', 'Redes', 'Seguridad']
    for nombre in categorias:
        cursor.execute(
            "INSERT INTO Categoria (NombreCategoria, Descripcion) VALUES (%s, %s)",
            (nombre, f'Incidencias de tipo {nombre}')
        )

    estados = [
        ('Abierto', 1),
        ('En Proceso', 2),
        ('Cerrado', 3),
        ('Archivado', 4)
    ]
    for nombre, orden in estados:
        cursor.execute(
            "INSERT INTO Estado (NombreEstado, OrdenVisualizacion) VALUES (%s, %s)",
            (nombre, orden)
        )

    prioridades = [('Baja', 1), ('Media', 2), ('Alta', 3), ('Critica', 4)]
    for nombre, nivel in prioridades:
        cursor.execute(
            "INSERT INTO Prioridad (NombrePrioridad, Nivel) VALUES (%s, %s)",
            (nombre, nivel)
        )

    conexion.commit()

    cursor.execute("SELECT IdCategoria FROM Categoria")
    ids_categorias = [fila[0] for fila in cursor.fetchall()]

    cursor.execute("SELECT IdEstado, NombreEstado FROM Estado")
    filas_estados = cursor.fetchall()
    ids_estados = {nombre: id_est for id_est, nombre in filas_estados}

    cursor.execute("SELECT IdPrioridad FROM Prioridad")
    ids_prioridades = [fila[0] for fila in cursor.fetchall()]

    escribir_log('Catálogos de Categoria, Estado y Prioridad generados con éxito')
    return ids_categorias, ids_estados, ids_prioridades


# Función generar_departamentos_y_operadores()
def generar_departamentos_y_operadores(conexion):
    cursor = conexion.cursor()
    ids_operadores = []
    ids_departamentos = []

    nombres_dep = ['Soporte Nivel 1', 'Soporte Nivel 2', 'Redes', 'Seguridad']

    query_dep = "INSERT INTO Departamento (NombreDep, Ubicacion) VALUES (%s, %s)"
    for nombre in nombres_dep:
        ubicacion = f'Planta {random.randint(1, 4)}'
        cursor.execute(query_dep, (nombre, ubicacion))
        ids_departamentos.append(cursor.lastrowid)

    query_op = "INSERT INTO Operador (Nombre, CorreoCorporativo, IdDepartamento, FechaIngreso) VALUES (%s, %s, %s, %s)"
    correos_usados = set()
    for _ in range(10):
        nombre = fake.name()
        correo = fake.company_email()
        while correo in correos_usados:
            correo = fake.company_email()
        correos_usados.add(correo)
        id_dep = random.choice(ids_departamentos)
        fecha_ingreso = fake.date_between(start_date='-5y', end_date='today')
        cursor.execute(query_op, (nombre, correo, id_dep, fecha_ingreso))
        ids_operadores.append(cursor.lastrowid)

    conexion.commit()
    escribir_log('4 Departamentos generados con éxito')
    escribir_log('10 Operadores generados con éxito')
    return ids_operadores, ids_departamentos

# Función generar_clientes()
def generar_clientes(conexion):
    cursor = conexion.cursor()
    clientes_ids = []

    query_insertar = "INSERT INTO Cliente (NombreCompleto, Email, Telefono) VALUES (%s, %s, %s)"
    emails_usados = set()

    for _ in range(50):
        nombre = fake.name()
        email = fake.email()
        while email in emails_usados:
            email = fake.email()
        emails_usados.add(email)
        telefono = fake.phone_number()
        cursor.execute(query_insertar, (nombre, email, telefono))
        clientes_ids.append(cursor.lastrowid)

    conexion.commit()
    escribir_log('50 Clientes generados con éxito')
    return clientes_ids


# Función generar_tickets_y_mensajes()
def generar_tickets_y_mensajes(conexion, clientes_ids, operador_ids, ids_categorias, ids_estados, ids_prioridades):
    cursor = conexion.cursor()
    tickets_ids = []
    estados_cierre = {'Cerrado', 'Archivado'}

    query_ticket = (
        "INSERT INTO Ticket "
        "(Titulo, Descripcion, FechaCreacion, FechaCierre, IdCliente, IdCategoria, IdEstado, IdPrioridad, IdEmpleado) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    )
    query_mensaje = (
        "INSERT INTO Mensaje (Cuerpo, FechaHora, CodigoTicket, IdCliente, IdEmpleado) "
        "VALUES (%s, %s, %s, %s, %s)"
    )

    for _ in range(200):
        titulo = fake.sentence(nb_words=5)
        descripcion = fake.paragraph(nb_sentences=2)
        id_cliente = random.choice(clientes_ids)
        id_operador = random.choice(operador_ids)
        id_categoria = random.choice(ids_categorias)
        nombre_estado = random.choice(list(ids_estados.keys()))
        id_estado = ids_estados[nombre_estado]
        id_prioridad = random.choice(ids_prioridades)
        fecha_creacion = fake.date_time_between(start_date='-2y', end_date='now')

        if nombre_estado in estados_cierre:
            fecha_cierre = fecha_creacion + timedelta(days=random.randint(1, 240))
        else:
            fecha_cierre = None

        cursor.execute(query_ticket, (
            titulo, descripcion, fecha_creacion, fecha_cierre,
            id_cliente, id_categoria, id_estado, id_prioridad, id_operador
        ))
        id_ticket = cursor.lastrowid
        tickets_ids.append(id_ticket)

        for _ in range(random.randint(1, 3)):
            texto = fake.paragraph(nb_sentences=2)
            fecha_msg = fecha_creacion + timedelta(minutes=random.randint(10, 120))
            autor = random.choice(['cliente', 'operador'])
            if autor == 'cliente':
                cursor.execute(query_mensaje, (texto, fecha_msg, id_ticket, id_cliente, None))
            else:
                cursor.execute(query_mensaje, (texto, fecha_msg, id_ticket, None, id_operador))

    conexion.commit()
    escribir_log('200 Tickets y sus hilos de conversación generados con éxito')
    return tickets_ids



if __name__ == '__main__':
    escribir_log('--- Inicio de ejecución del seeder ---')
    conexion = conectar_bd()
    if conexion:
        try:
            ids_categorias, ids_estados, ids_prioridades = generar_catalogos(conexion)
            ids_operadores, ids_departamentos = generar_departamentos_y_operadores(conexion)
            clientes_ids = generar_clientes(conexion)
            generar_tickets_y_mensajes(conexion, clientes_ids, ids_operadores, ids_categorias, ids_estados, ids_prioridades)
            escribir_log('Inserción completada. 50 Clientes y 200 Tickets generados con éxito')
            print('Proceso finalizado con éxito. Revisa seed_log.txt para el detalle.')
        except mysql.connector.Error as err:
            mensaje = f'Error durante la generación de datos: {err}'
            print(mensaje)
            escribir_log(mensaje)
        finally:
            conexion.close()
    else:
        escribir_log('Proceso abortado: no se pudo establecer conexión con la base de datos')