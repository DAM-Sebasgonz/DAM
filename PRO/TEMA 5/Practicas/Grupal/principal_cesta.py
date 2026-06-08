import sys
import json
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton
from CestaCompra_ui import Ui_Form

class VentanaCestaCompra(QWidget, Ui_Form):
    def __init__(self, listaProductos, totalCompra, parent=None):
        super(VentanaCestaCompra, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Cesta de la compra")

        self.listaProductos = listaProductos
        self.totalCompra = totalCompra

        self.botonCerrar = QPushButton("Cerrar", self)
        self.botonCerrar.setGeometry(500, 370, 93, 28)
        self.botonCerrar.setVisible(False)

        self.actualizarVistaCesta()

        self.pbEliminar.clicked.connect(self.eliminarSeleccionados)
        self.pbVaciarCesta.clicked.connect(self.vaciarCesta)
        self.pbComprar.clicked.connect(self.procesarCompra)
        self.botonCerrar.clicked.connect(self.close)

    def obtenerFilas(self):
        return [
            {
                "producto": self.leProducto1, "talla": self.leTalla1,
                "estampado": self.cbEstampado1, "envio": self.cbEnvio1,
                "envoltura": self.cbEnvoltura1, "seleccion": self.cbSeleccion1,
            },
            {
                "producto": self.leProducto2, "talla": self.leTalla2,
                "estampado": self.cbEstampado2, "envio": self.cbEnvio2,
                "envoltura": self.cbEnvoltura2, "seleccion": self.cbSeleccion2,
            },
            {
                "producto": self.leProducto3, "talla": self.leTalla3,
                "estampado": self.cbEstampado3, "envio": self.cbEnvio3,
                "envoltura": self.cbEnvoltura3, "seleccion": self.cbSeleccion3,
            },
        ]

    def actualizarVistaCesta(self):
        coleccionFilas = self.obtenerFilas()

        for fila in coleccionFilas:
            fila["producto"].setText("")
            fila["talla"].setText("")
            fila["estampado"].setChecked(False)
            fila["envio"].setChecked(False)
            fila["envoltura"].setChecked(False)
            fila["seleccion"].setChecked(False)
            fila["seleccion"].setEnabled(False)

        for indice, articulo in enumerate(self.listaProductos):
            filaVisual = coleccionFilas[indice]
            filaVisual["producto"].setText(articulo["producto"])
            filaVisual["talla"].setText(articulo["talla"])
            filaVisual["estampado"].setChecked(articulo["estampado"])
            filaVisual["envio"].setChecked(articulo["envio"])
            filaVisual["envoltura"].setChecked(articulo["envoltura"])
            filaVisual["seleccion"].setEnabled(True)

    def eliminarSeleccionados(self):
        coleccionFilas = self.obtenerFilas()

        indicesAEliminar = [indice for indice, fila in enumerate(coleccionFilas) if fila["seleccion"].isChecked()]

        for indice in sorted(indicesAEliminar, reverse=True):
            if indice < len(self.listaProductos):
                del self.listaProductos[indice]
                
        self.totalCompra[0] = sum(articulo["precio"] for articulo in self.listaProductos)

        self.actualizarVistaCesta()

        if len(self.listaProductos) == 0:
            self.vaciarCesta()

    def vaciarCesta(self):
        self.listaProductos.clear()
        self.totalCompra[0] = 0.0

        self.actualizarVistaCesta()

        self.pbEliminar.setEnabled(False)
        self.pbVaciarCesta.setEnabled(False)
        self.pbComprar.setEnabled(False)
        self.botonCerrar.setVisible(True)

    def procesarCompra(self):
        importeFinal = self.totalCompra[0]

        ventanaMensaje = QMessageBox(self)
        ventanaMensaje.setWindowTitle("Confirmar compra")
        ventanaMensaje.setText(f"El monto total de la compra es: {importeFinal:.2f} €\n¿Desea continuar?")
        ventanaMensaje.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ventanaMensaje.setDefaultButton(QMessageBox.Cancel)
        
        respuestaUsuario = ventanaMensaje.exec()

        if respuestaUsuario == QMessageBox.Ok:
            datosCompra = {
                "productos": self.listaProductos[:],
                "importe_total": importeFinal,
            }
            with open("compra.json", "w", encoding="utf-8") as archivoJson:
                json.dump(datosCompra, archivoJson, ensure_ascii=False, indent=4)

            self.vaciarCesta()

def main():
    aplicacion = QApplication(sys.argv)
    listaPrueba = []
    montoPrueba = [0.0]
    ventanaCesta = VentanaCestaCompra(listaPrueba, montoPrueba)
    ventanaCesta.show()
    sys.exit(aplicacion.exec())

if __name__ == '__main__':
    main()