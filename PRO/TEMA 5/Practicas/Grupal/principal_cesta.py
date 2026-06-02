import sys
import json
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton
from CestaCompra_ui import Ui_Form

class VentanaCestaCompra(QWidget, Ui_Form):
    def __init__(self, listaProductos, totalCompra, parent=None):
        super(VentanaCestaCompra, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Cesta de la compra")

        # Recibimos la cesta y el importe desde la ventana principal
        self.listaProductos = listaProductos
        self.totalCompra = totalCompra

        # Botón Cerrar 
        self.botonCerrar = QPushButton("Cerrar", self)
        self.botonCerrar.setGeometry(500, 370, 93, 28)
        self.botonCerrar.setVisible(False)

        # Cargamos los datos visualmente al iniciar la ventana
        self.actualizarVistaCesta()

        # Conexión de eventos
        self.pbEliminar.clicked.connect(self.eliminarSeleccionados)
        self.pbVaciarCesta.clicked.connect(self.vaciarCesta)
        self.pbComprar.clicked.connect(self.procesarCompra)
        self.botonCerrar.clicked.connect(self.close)

    def obtenerFilas(self):
        # Agrupamos los elementos de la interfaz por filas para manejarlos fácilmente sobre ellos
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
        
        # 1. Limpiamos visualmente todas las filas
        for fila in coleccionFilas:
            fila["producto"].setText("")
            fila["talla"].setText("")
            fila["estampado"].setChecked(False)
            fila["envio"].setChecked(False)
            fila["envoltura"].setChecked(False)
            fila["seleccion"].setChecked(False)
            fila["seleccion"].setEnabled(False) # Se deshabilita por defecto

        # 2. Rellenamos las filas con los datos de los productos que estén en la lista
        for indice, articulo in enumerate(self.listaProductos):
            filaVisual = coleccionFilas[indice]
            filaVisual["producto"].setText(articulo["producto"])
            filaVisual["talla"].setText(articulo["talla"])
            filaVisual["estampado"].setChecked(articulo["estampado"])
            filaVisual["envio"].setChecked(articulo["envio"])
            filaVisual["envoltura"].setChecked(articulo["envoltura"])
            filaVisual["seleccion"].setEnabled(True) # Activamos el campo de selección

    def eliminarSeleccionados(self):
        coleccionFilas = self.obtenerFilas()
        
        # Buscamos qué índices tienen el checkbox de "selección" marcado
        indicesAEliminar = [indice for indice, fila in enumerate(coleccionFilas) if fila["seleccion"].isChecked()]
        
        # Eliminamos de la lista iterando en orden inverso para no desfasar los índices al borrar
        for indice in sorted(indicesAEliminar, reverse=True):
            if indice < len(self.listaProductos):
                del self.listaProductos[indice]
                
        # Recalculamos el importe total tras la eliminación
        self.totalCompra[0] = sum(articulo["precio"] for articulo in self.listaProductos)
        
        # Volvemos a pintar la cesta, esto causará que los elementos restantes se "desplacen hacia arriba"
        self.actualizarVistaCesta()
        
        # Si nos quedamos sin elementos, procedemos a vaciar del todo la cesta visualmente
        if len(self.listaProductos) == 0:
            self.vaciarCesta()

    def vaciarCesta(self):
        # Limpiamos los datos en memoria
        self.listaProductos.clear()
        self.totalCompra[0] = 0.0
        
        # Limpiamos visualmente
        self.actualizarVistaCesta()
        
        # Inhabilitamos botones y mostramos el de Cerrar
        self.pbEliminar.setEnabled(False)
        self.pbVaciarCesta.setEnabled(False)
        self.pbComprar.setEnabled(False)
        self.botonCerrar.setVisible(True)

    def procesarCompra(self):
        importeFinal = self.totalCompra[0]
        
        # Cuadro de diálogo para confirmar compra
        ventanaMensaje = QMessageBox(self)
        ventanaMensaje.setWindowTitle("Confirmar compra")
        ventanaMensaje.setText(f"El monto total de la compra es: {importeFinal:.2f} €\n¿Desea continuar?")
        ventanaMensaje.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ventanaMensaje.setDefaultButton(QMessageBox.Cancel)
        
        respuestaUsuario = ventanaMensaje.exec()

        if respuestaUsuario == QMessageBox.Ok:
            # Si acepta, generamos el JSON con los datos de compra
            datosCompra = {
                "productos": self.listaProductos[:],
                "importe_total": importeFinal,
            }
            with open("compra.json", "w", encoding="utf-8") as archivoJson:
                json.dump(datosCompra, archivoJson, ensure_ascii=False, indent=4)

            # Limpiamos la cesta y actualizamos la interfaz finalizando el programa
            self.vaciarCesta()

def main():
    aplicacion = QApplication(sys.argv)
    # Lista y monto simulados para probar la ventana independientemente
    listaPrueba = []
    montoPrueba = [0.0]
    ventanaCesta = VentanaCestaCompra(listaPrueba, montoPrueba)
    ventanaCesta.show()
    sys.exit(aplicacion.exec())

if __name__ == '__main__':
    main()