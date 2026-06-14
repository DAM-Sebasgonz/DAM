import sys
from PyQt6.QtWidgets import (
    QApplication, QInputDialog, QLineEdit, QMessageBox, QTableWidgetItem
)
from conexion_bd import GestorBD
from ventana_ui import VentanaReservas


class ControladorReservas:
    def __init__(self, ventana: VentanaReservas, bd: GestorBD):
        self.v  = ventana   
        self.bd = bd        
        self._conectar_senales()

    def _conectar_senales(self):
        v = self.v

        v.btn_per_insertar.clicked.connect(self.insertar_persona)
        v.btn_per_modificar.clicked.connect(self.modificar_persona)
        v.btn_per_borrar.clicked.connect(self.borrar_persona)
        v.btn_per_listar.clicked.connect(self.listar_personas)

        v.btn_ae_ins.clicked.connect(self.insertar_aerolinea)

        v.btn_vu_insertar.clicked.connect(self.insertar_vuelo)
        v.btn_vu_modificar.clicked.connect(self.modificar_vuelo)
        v.btn_vu_borrar.clicked.connect(self.borrar_vuelo)
        v.btn_vu_listar.clicked.connect(self.listar_vuelos)

        v.btn_res_insertar.clicked.connect(self.insertar_reserva)
        v.btn_res_modificar.clicked.connect(self.modificar_reserva)
        v.btn_res_borrar.clicked.connect(self.borrar_reserva)
        v.btn_res_listar.clicked.connect(self.listar_reservas)

        v.btn_inf_pasajeros.clicked.connect(self.inf_pasajeros_vuelo)
        v.btn_inf_historial.clicked.connect(self.inf_veces_viajado)
        v.btn_inf_lider.clicked.connect(self.inf_aerolinea_lider)

        v.closeEvent = self._on_close





    def _aviso(self, titulo: str, mensaje: str):
        QMessageBox.warning(self.v, titulo, mensaje)

    def _info(self, titulo: str, mensaje: str):
        QMessageBox.information(self.v, titulo, mensaje)

    def _rellenar_tabla(self, tabla, filas):
        tabla.setRowCount(0)
        for i, fila in enumerate(filas):
            tabla.insertRow(i)
            for j, valor in enumerate(fila):
                tabla.setItem(i, j, QTableWidgetItem(str(valor) if valor is not None else ""))

    def insertar_persona(self):
        nif    = self.v.txt_per_nif.text().strip()
        nombre = self.v.txt_per_nombre.text().strip()
        sexo   = self.v.cmb_per_sexo.currentText()
        edad   = str(self.v.txt_per_edad.value())

        if not nif or not nombre:
            self._aviso("Aviso", "El NIF y el nombre son obligatorios.")
            return

        try:
            self.bd.insertar_persona(nif, nombre, sexo, edad)
            self._info("Éxito", "Persona registrada correctamente.")
            self.listar_personas()
        except Exception as e:
            self.bd.hacer_rollback()
            self._aviso("Error", f"No se pudo insertar: {e}")

    def modificar_persona(self):
        nif    = self.v.txt_per_nif.text().strip()
        nombre = self.v.txt_per_nombre.text().strip()
        edad   = str(self.v.txt_per_edad.value())

        if not nif:
            self._aviso("Aviso", "Introduzca el NIF de la persona a modificar.")
            return

        try:
            if self.bd.modificar_persona(nif, nombre, edad):
                self._info("Éxito", "Datos actualizados.")
                self.listar_personas()
            else:
                self._aviso("Aviso", "No se encontró ningún registro con ese NIF.")
        except Exception as e:
            self.bd.hacer_rollback()
            self._aviso("Error", f"Error al modificar: {e}")

    def borrar_persona(self):
        nif = self.v.txt_per_nif.text().strip()

        if not nif:
            self._aviso("Aviso", "Introduzca el NIF de la persona a borrar.")
            return

        try:
            if self.bd.borrar_persona(nif):
                self._info("Éxito", "Persona eliminada.")
                self.listar_personas()
            else:
                self._aviso("Aviso", "El NIF no existe en la base de datos.")
        except Exception as e:
            self.bd.hacer_rollback()
            self._aviso("Error", f"No se pudo borrar: {e}")

    def listar_personas(self):
        try:
            filas = self.bd.obtener_personas()
            self._rellenar_tabla(self.v.tabla_personas, filas)
        except Exception as e:
            self._aviso("Error", f"Error al leer personas: {e}")


    def insertar_aerolinea(self):
        cod  = self.v.txt_ae_cod.text().strip()
        nom  = self.v.txt_ae_nom.text().strip()
        pais = self.v.txt_ae_pais.text().strip()

        if not cod or not nom or not pais:
            self._aviso("Aviso", "Rellene todos los campos de la aerolínea.")
            return

        try:
            self.bd.insertar_aerolinea(cod, nom, pais)
            self._info("Éxito", "Aerolínea registrada.")
        except Exception as e:
            self.bd.hacer_rollback()
            self._aviso("Error", f"Error al registrar aerolínea: {e}")


    def insertar_vuelo(self):
        id_vu  = self.v.txt_vu_id.text().strip()
        dest   = self.v.txt_vu_dest.text().strip()
        plazas = str(self.v.txt_vu_plazas.value())
        fecha  = self.v.txt_vu_fecha.date().toString("yyyy-MM-dd")
        hora   = self.v.txt_vu_hora.time().toString("HH:mm:ss")
        aero   = self.v.txt_vu_aero.text().strip()

        if not id_vu or not dest or not aero:
            self._aviso("Aviso", "El ID, destino y código de aerolínea son obligatorios.")
            return

        try:
            self.bd.insertar_vuelo(id_vu, dest, plazas, fecha, hora, aero)
            self._info("Éxito", "Vuelo registrado.")
            self.listar_vuelos()
        except Exception as e:
            self.bd.hacer_rollback()
            self._aviso("Error", f"Error al insertar vuelo: {e}")

    def modificar_vuelo(self):
        id_vu  = self.v.txt_vu_id.text().strip()
        dest   = self.v.txt_vu_dest.text().strip()
        # Solo se envía plazas si el spinbox tiene un valor mayor que 0
        plazas = str(self.v.txt_vu_plazas.value()) if self.v.txt_vu_plazas.value() > 0 else None

        if not id_vu:
            self._aviso("Aviso", "Introduzca el ID del vuelo a modificar.")
            return

        try:
            if self.bd.modificar_vuelo(id_vu, dest, plazas):
                self._info("Éxito", "Vuelo actualizado.")
                self.listar_vuelos()
            else:
                self._aviso("Aviso", "No se modificó ningún campo.")
        except Exception as e:
            self.bd.hacer_rollback()
            self._aviso("Error", f"Error al modificar vuelo: {e}")

    def borrar_vuelo(self):
        id_vu = self.v.txt_vu_id.text().strip()

        if not id_vu:
            self._aviso("Aviso", "Introduzca el ID del vuelo a borrar.")
            return

        try:
            if self.bd.borrar_vuelo(id_vu):
                self._info("Éxito", "Vuelo eliminado.")
                self.listar_vuelos()
            else:
                self._aviso("Aviso", "El ID no existe en la base de datos.")
        except Exception as e:
            self.bd.hacer_rollback()
            self._aviso("Error", f"Error al borrar vuelo: {e}")

    def listar_vuelos(self):
        try:
            filas = self.bd.obtener_vuelos()   # corregido: era obtener_vuegos
            self._rellenar_tabla(self.v.tabla_vuelos, filas)
        except Exception as e:
            self._aviso("Error", f"Error al leer vuelos: {e}")


    def insertar_reserva(self):
        nif   = self.v.txt_res_nif.text().strip()
        vuelo = self.v.txt_res_vuelo.text().strip()
        f_res = self.v.txt_res_fres.date().toString("yyyy-MM-dd")
        f_pago = (self.v.txt_res_fpago.date().toString("yyyy-MM-dd")
                  if self.v.chk_pagado.isChecked() else None)
        estado = self.v.cmb_res_est.currentText()

        if not nif or not vuelo:
            self._aviso("Aviso", "El NIF y el ID de vuelo son obligatorios.")
            return

        try:
            self.bd.insertar_reserva(nif, vuelo, f_res, f_pago, estado)
            self._info("Éxito", "Reserva creada.")
            self.listar_reservas()
        except Exception as e:
            self.bd.hacer_rollback()
            self._aviso("Error", f"Error al crear reserva: {e}")

    def modificar_reserva(self):
        nif    = self.v.txt_res_nif.text().strip()
        vuelo  = self.v.txt_res_vuelo.text().strip()
        estado = self.v.cmb_res_est.currentText()
        f_pago = (self.v.txt_res_fpago.date().toString("yyyy-MM-dd")
                  if self.v.chk_pagado.isChecked() else None)

        if not nif or not vuelo:
            self._aviso("Aviso", "Introduzca el NIF y el ID de vuelo.")
            return

        try:
            self.bd.modificar_reserva(nif, vuelo, estado, f_pago)
            self._info("Éxito", "Estado de reserva modificado.")
            self.listar_reservas()
        except Exception as e:
            self.bd.hacer_rollback()
            self._aviso("Error", f"Error al modificar reserva: {e}")

    def borrar_reserva(self):
        nif   = self.v.txt_res_nif.text().strip()
        vuelo = self.v.txt_res_vuelo.text().strip()

        if not nif or not vuelo:
            self._aviso("Aviso", "Introduzca el NIF y el ID de vuelo.")
            return

        try:
            if self.bd.borrar_reserva(nif, vuelo):
                self._info("Éxito", "Reserva cancelada.")
                self.listar_reservas()
            else:
                self._aviso("Aviso", "No se encontró la reserva indicada.")
        except Exception as e:
            self.bd.hacer_rollback()
            self._aviso("Error", f"Error al anular reserva: {e}")

    def listar_reservas(self):
        try:
            filas = self.bd.obtener_reservas()
            self._rellenar_tabla(self.v.tabla_reservas, filas)
        except Exception as e:
            self._aviso("Error", f"Error al leer reservas: {e}")

    def inf_pasajeros_vuelo(self):
        id_vuelo, ok = QInputDialog.getText(
            self.v, "Consulta — Pasajeros", "ID del vuelo:")
        if not ok or not id_vuelo.strip():
            return

        try:
            filas = self.bd.reporte_pasajeros_vuelo(id_vuelo.strip())
            self.v.tabla_reportes.setColumnCount(3)
            self.v.tabla_reportes.setHorizontalHeaderLabels(
                ["NIF", "Nombre completo", "Edad"])
            self.v.lbl_consulta_activa.setText(
                f"Pasajeros del vuelo {id_vuelo.strip()} — {len(filas)} resultado(s)")
            self._rellenar_tabla(self.v.tabla_reportes, filas)
        except Exception as e:
            self._aviso("Error", f"Error en la consulta: {e}")

    def inf_veces_viajado(self):
        nif, ok = QInputDialog.getText(
            self.v, "Consulta — Historial", "NIF de la persona:")
        if not ok or not nif.strip():
            return

        try:
            total = self.bd.reporte_viajes_persona(nif.strip())
            self.v.tabla_reportes.setColumnCount(2)
            self.v.tabla_reportes.setHorizontalHeaderLabels(
                ["NIF", "Viajes totales"])
            self.v.lbl_consulta_activa.setText(
                f"Historial de viajes para NIF {nif.strip()}")
            self._rellenar_tabla(self.v.tabla_reportes,
                                 [(nif.strip(), total)])
        except Exception as e:
            self._aviso("Error", f"Error en la consulta: {e}")

    def inf_aerolinea_lider(self):
        try:
            fila = self.bd.reporte_aerolinea_lider()
            self.v.tabla_reportes.setColumnCount(3)
            self.v.tabla_reportes.setHorizontalHeaderLabels(
                ["Código", "Compañía aérea", "Pasajeros únicos"])
            self.v.lbl_consulta_activa.setText("Aerolínea con más pasajeros únicos")
            self._rellenar_tabla(self.v.tabla_reportes, [fila] if fila else [])
        except Exception as e:
            self._aviso("Error", f"Error en la consulta: {e}")
            

    def _on_close(self, event):
        self.bd.desconectar()
        event.accept()


def main():
    app = QApplication(sys.argv)

    password, ok = QInputDialog.getText(
        None,
        "Autenticación",
        "Contraseña de usrpostgre:",
        QLineEdit.EchoMode.Password
    )

    if not ok or not password:
        sys.exit()

    bd = GestorBD(password)

    if not bd.conectar():
        QMessageBox.critical(
            None,
            "Error de conexión",
            "No se pudo conectar a PostgreSQL con esa contraseña."
        )
        sys.exit()

    ventana     = VentanaReservas()
    controlador = ControladorReservas(ventana, bd)  
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
