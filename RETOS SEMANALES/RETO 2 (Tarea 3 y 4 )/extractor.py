from datetime import datetime
import mysql.connector
import xml.etree.ElementTree as ET

# Función escribir_log(mensaje)
def escribir_log(mensaje):
    ahora = datetime.now()
    linea = ahora.strftime("[%Y-%m-%d %H:%M:%S] ") + 'INFO: ' + mensaje
    with open('extractor_log.txt', 'a', encoding='utf-8') as archivo_log:
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

# Función calcular_sla(fecha_creacion, fecha_cierre)
def calcular_sla(fecha_creacion, fecha_cierre):
    diferencia = (fecha_cierre - fecha_creacion).days
    if diferencia > 7:
        return diferencia - 7
    else:
        return None

# Función def analizar_sentimiento(mensajes)
def analizar_sentimiento(mensajes):
    palabras_clave = ['incompetentes', 'denuncia', 'vergüenza', 'lento']
    for mensaje in mensajes:
        for palabra in palabras_clave:
            if palabra in mensaje.lower():
                return True
    return False

# Función generar_xml_ticket()
def generar_xml_ticket(ticket, cliente, operador, mensajes):
    # Etiqueta raíz
    raiz = ET.Element('ticket')
    titulo = ET.SubElement(raiz, 'Titulo')
    titulo.text = str(ticket['Titulo'])
    descripcion = ET.SubElement(raiz, 'Descripcion')
    descripcion.text = str(ticket['Descripcion'])
    fechaCreacion = ET.SubElement(raiz, 'FechaCreacion')
    fechaCreacion.text = str(ticket['FechaCreacion'])
    fechaCierre = ET.SubElement(raiz, 'FechaCierre')
    fechaCierre.text = str(ticket['FechaCierre'])

    # Etiqueta cliente
    nodo_cliente = ET.SubElement(raiz, 'Cliente')
    nombre = ET.SubElement(nodo_cliente, 'NombreCliente')
    nombre.text = str(cliente['NombreCompleto'])
    email = ET.SubElement(nodo_cliente, 'Email')
    email.text = str(cliente['Email'])
    telefono = ET.SubElement(nodo_cliente, 'Telefono')
    telefono.text = str(cliente['Telefono'])
    fecharegistro = ET.SubElement(nodo_cliente, 'FechaRegistro')
    fecharegistro.text = str(cliente['FechaRegistro'])

    # Etiqueta operador
    nodo_operador = ET.SubElement(raiz, 'Operador')
    nombre = ET.SubElement(nodo_operador, 'NombreOperador')
    nombre.text = str(operador['Nombre'])
    email = ET.SubElement(nodo_operador, 'CorreoCorporativo')
    email.text = str(operador['CorreoCorporativo'])

    # Etiqueta historial
    nodo_historial = ET.SubElement(raiz, 'Historial')
    for mensaje in mensajes:
        nodo_mensaje = ET.SubElement(nodo_historial, 'Mensaje')
        cuerpo = ET.SubElement(nodo_mensaje, 'Cuerpo')
        cuerpo.text = str(mensaje['Cuerpo'])
        fecha = ET.SubElement(nodo_mensaje, 'FechaHora')
        fecha.text = str(mensaje['FechaHora'])

    retraso = calcular_sla(ticket['FechaCreacion'], ticket['FechaCierre'])
    if retraso:
        alerta = ET.SubElement(raiz, 'alerta_sla')
        alerta.text = f'{retraso} días de retraso'

    if analizar_sentimiento([m['Cuerpo'] for m in mensajes]):
        raiz.set('cliente_enfadado', 'si')
    ruta = f"ticket_{ticket['CodigoTicket']}.xml"
    ET.ElementTree(raiz).write(ruta, encoding='utf-8', xml_declaration=True)



if __name__ == '__main__':
    conexion = conectar_bd()

    cursor = conexion.cursor(dictionary=True)
    cursor.execute("""
        SELECT t.CodigoTicket, t.Titulo, t.Descripcion, t.FechaCreacion, t.FechaCierre,
        c.NombreCompleto, c.Email, c.Telefono, c.FechaRegistro,
        o.Nombre, o.CorreoCorporativo
        FROM Ticket t
        JOIN Cliente c ON t.IdCliente = c.IdCliente
        JOIN Operador o ON t.IdEmpleado = o.IdEmpleado
        JOIN Estado e ON t.IdEstado = e.IdEstado
        WHERE e.NombreEstado = 'Archivado'
    """)
    tickets = cursor.fetchall()
    contador = 0
    for ticket in tickets:
        cursor.execute("""
            SELECT Cuerpo, FechaHora 
            FROM Mensaje 
            WHERE CodigoTicket = %s
            ORDER BY FechaHora ASC
        """, (ticket['CodigoTicket'],))
        mensaje = cursor.fetchall()
        generar_xml_ticket(ticket, ticket, ticket, mensaje)
        contador += 1

    escribir_log(f'{contador} archivos XML generados con éxito')