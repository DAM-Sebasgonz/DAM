import psycopg2
from psycopg2 import Error

class GestorBD:
    def __init__(self, password):
        self.password = password
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = psycopg2.connect(
                user="usrpostgre",
                password=self.password,
                host="localhost",
                port="5432",
                database="sistemareservasaerea"
            )
            self.conexion.set_client_encoding('UTF8')
            return True
        except (Exception, Error):
            return False

    def desconectar(self):
        if self.conexion:
            self.conexion.close()

    def obtener_personas(self):
        cur = self.conexion.cursor()
        query = "SELECT * FROM persona ORDER BY nif"
        cur.execute(query)
        filas = cur.fetchall()
        cur.close()
        return filas

    def insertar_persona(self, nif, nombre, sexo, edad):
        cur = self.conexion.cursor()
        query = "INSERT INTO persona (nif, nombre_completo, sexo, edad) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (nif, nombre, sexo, edad))
        self.conexion.commit()
        cur.close()

    def modificar_persona(self, nif, nombre, edad):
        cur = self.conexion.cursor()
        modificado = False
        if nombre:
            query1 = "UPDATE persona SET nombre_completo = %s WHERE nif = %s"
            cur.execute(query1, (nombre, nif))
            if cur.rowcount > 0: modificado = True
        if edad:
            query2 = "UPDATE persona SET edad = %s WHERE nif = %s"
            cur.execute(query2, (edad, nif))
            if cur.rowcount > 0: modificado = True
        self.conexion.commit()
        cur.close()
        return modificado

    def borrar_persona(self, nif):
        cur = self.conexion.cursor()
        query = "DELETE FROM persona WHERE nif = %s"
        cur.execute(query, (nif,))
        self.conexion.commit()
        afectado = cur.rowcount > 0
        cur.close()
        return afectado

    def obtener_vuelos(self):
        cur = self.conexion.cursor()
        query = "SELECT * FROM vuelo ORDER BY fecha_salida"
        cur.execute(query)
        filas = cur.fetchall()
        cur.close()
        return filas

    def insertar_aerolinea(self, cod, nom, pais):
        cur = self.conexion.cursor()
        query = "INSERT INTO aerolinea (codigo_identificacion, nombre, pais) VALUES (%s, %s, %s)"
        cur.execute(query, (cod, nom, pais))
        self.conexion.commit()
        cur.close()

    def insertar_vuelo(self, id_vu, dest, plazas, fecha, hora, aero):
        cur = self.conexion.cursor()
        query = """
            INSERT INTO vuelo (id_vuelo, destino, nro_plazas_totales, fecha_salida, hora_salida, codigo_aerolinea) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (id_vu, dest, plazas, fecha, hora, aero))
        self.conexion.commit()
        cur.close()

    def modificar_vuelo(self, id_vu, dest, plazas):
        cur = self.conexion.cursor()
        afectado = False
        if dest:
            cur.execute("UPDATE vuelo SET destino = %s WHERE id_vuelo = %s", (dest, id_vu))
            if cur.rowcount > 0: afectado = True
        if plazas:
            cur.execute("UPDATE vuelo SET nro_plazas_totales = %s WHERE id_vuelo = %s", (plazas, id_vu))
            if cur.rowcount > 0: afectado = True
        self.conexion.commit()
        cur.close()
        return afectado

    def borrar_vuelo(self, id_vu):
        cur = self.conexion.cursor()
        query = "DELETE FROM vuelo WHERE id_vuelo = %s"
        cur.execute(query, (id_vu,))
        self.conexion.commit()
        afectado = cur.rowcount > 0
        cur.close()
        return afectado

    def obtener_reservas(self):
        cur = self.conexion.cursor()
        query = "SELECT * FROM reserva ORDER BY fecha_reserva"
        cur.execute(query)
        filas = cur.fetchall()
        cur.close()
        return filas

    def insertar_reserva(self, nif, vuelo, f_res, f_pago, estado):
        cur = self.conexion.cursor()
        query = "INSERT INTO reserva VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (nif, vuelo, f_res, f_pago, estado))
        self.conexion.commit()
        cur.close()

    def modificar_reserva(self, nif, vuelo, estado, f_pago):
        cur = self.conexion.cursor()
        query1 = "UPDATE reserva SET estado = %s WHERE nif_persona = %s AND id_vuelo = %s"
        cur.execute(query1, (estado, nif, vuelo))
        if cur.rowcount > 0 and f_pago:
            query2 = "UPDATE reserva SET fecha_pago = %s WHERE nif_persona = %s AND id_vuelo = %s"
            cur.execute(query2, (f_pago, nif, vuelo))
        self.conexion.commit()
        cur.close()

    def borrar_reserva(self, nif, vuelo):
        cur = self.conexion.cursor()
        query = "DELETE FROM reserva WHERE nif_persona = %s AND id_vuelo = %s"
        cur.execute(query, (nif, vuelo))
        self.conexion.commit()
        afectado = cur.rowcount > 0
        cur.close()
        return afectado

    def reporte_pasajeros_vuelo(self, id_vuelo):
        cur = self.conexion.cursor()
        query = """
            SELECT p.nif, p.nombre_completo, p.edad
            FROM persona p
            JOIN reserva r ON p.nif = r.nif_persona
            WHERE r.id_vuelo = %s
        """
        cur.execute(query, (id_vuelo,))
        filas = cur.fetchall()
        cur.close()
        return filas

    def reporte_viajes_persona(self, nif):
        cur = self.conexion.cursor()
        query = "SELECT COUNT(*) FROM reserva WHERE nif_persona = %s"
        cur.execute(query, (nif,))
        total = cur.fetchone()[0]
        cur.close()
        return total

    def reporte_aerolinea_lider(self):
        cur = self.conexion.cursor()
        query = """
            SELECT a.codigo_identificacion, a.nombre, COUNT(DISTINCT r.nif_persona) as num_personas
            FROM aerolinea a
            JOIN vuelo v ON a.codigo_identificacion = v.codigo_aerolinea
            JOIN reserva r ON v.id_vuelo = r.id_vuelo
            GROUP BY a.codigo_identificacion, a.nombre
            ORDER BY num_personas DESC
            LIMIT 1
        """
        cur.execute(query)
        fila = cur.fetchone()
        cur.close()
        return fila

    def hacer_rollback(self):
        if self.conexion:
            self.conexion.rollback()