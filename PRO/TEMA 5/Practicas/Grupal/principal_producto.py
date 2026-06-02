import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from producto_ui import Ui_Form

# Diccionario con los precios base de los productos
preciosBase = {
    "Camiseta": 20,
    "Sudadera": 40,
    "Chandal": 55,
}

# Lista compartida para simular la cesta de la compra. Máximo 3 elementos.
listaCesta = [] 
# Usamos una lista para el importe total para poder pasarlo por referencia a la otra ventana
importeTotal = [0.0] 

class VentanaProducto(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(VentanaProducto, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Tienda Deportiva")

        # Se crean y configuran los botones "Añadir" y "Ver cesta" que faltaban en el diseño
        self.botonAnadir = QPushButton("Añadir", self)
        self.botonAnadir.setGeometry(80, 440, 93, 28)
        self.botonAnadir.setEnabled(False)

        self.botonVerCesta = QPushButton("Ver cesta", self)
        self.botonVerCesta.setGeometry(190, 440, 93, 28)
        self.botonVerCesta.setEnabled(False)

        self.resize(312, 490)

        # Estado inicial: Controles de precios siempre deshabilitados
        self.lePrecioFinal.setEnabled(False)
        self.leImporte.setEnabled(False)

        # Conexión de eventos (Señales a Slots)
        self.comboBox.currentIndexChanged.connect(self.alCambiarProducto)
        self.pbCalcularPrecio.clicked.connect(self.calcularPrecio)
        self.botonAnadir.clicked.connect(self.anadirProducto)
        self.botonVerCesta.clicked.connect(self.abrirCesta)

        self.ventanaCesta = None

    def alCambiarProducto(self, indice):
        # Si el índice es mayor a 0, significa que se seleccionó un producto válido
        productoValido = indice > 0
        
        # Habilitamos o deshabilitamos los controles según la selección
        self.rbS.setEnabled(productoValido)
        self.rbM.setEnabled(productoValido)
        self.rbL.setEnabled(productoValido)
        self.rbXL.setEnabled(productoValido)
        self.cbEstampado.setEnabled(productoValido)
        self.cbEnvioRapido.setEnabled(productoValido)
        self.cbEnvolturaRegalo.setEnabled(productoValido)
        self.pbCalcularPrecio.setEnabled(productoValido)
        self.botonAnadir.setEnabled(productoValido)
        
        # Si se vuelve a la opción vacía, reiniciamos visualmente los controles
        if not productoValido:
            self.reiniciarControles()

    def calcularPrecio(self):
        # Obtenemos el texto del producto seleccionado
        nombreProducto = self.comboBox.currentText()
        # Buscamos su precio base en el diccionario, por defecto 0
        precioCalculado = preciosBase.get(nombreProducto, 0)
        
        # Sumamos los extras seleccionados
        if self.cbEstampado.isChecked():
            precioCalculado += 5
        if self.cbEnvioRapido.isChecked():
            precioCalculado += 10
        if self.cbEnvolturaRegalo.isChecked():
            precioCalculado += 3
            
        # Actualizamos el campo de Precio final del producto
        self.lePrecioFinal.setText(str(precioCalculado))

    def anadirProducto(self):
        nombreProducto = self.comboBox.currentText()
        
        # Determinamos la talla seleccionada
        tallaSeleccionada = ""
        if self.rbS.isChecked():
            tallaSeleccionada = "S"
        elif self.rbM.isChecked(): 
            tallaSeleccionada = "M"
        elif self.rbL.isChecked(): 
            tallaSeleccionada = "L"
        elif self.rbXL.isChecked():
            tallaSeleccionada = "XL"

        # Comprobamos los extras
        tieneEstampado = self.cbEstampado.isChecked()
        tieneEnvio = self.cbEnvioRapido.isChecked()
        tieneEnvoltura = self.cbEnvolturaRegalo.isChecked()

        # Obtenemos el precio calculado. Si el usuario no dio a "Calcular", lo sacamos del base.
        textoPrecio = self.lePrecioFinal.text()
        precioFinalProducto = float(textoPrecio) if textoPrecio else preciosBase.get(nombreProducto, 0)

        # Creamos el diccionario que representa el nuevo producto
        nuevoProducto = {
            "producto": nombreProducto,
            "talla": tallaSeleccionada,
            "estampado": tieneEstampado,
            "envio": tieneEnvio,
            "envoltura": tieneEnvoltura,
            "precio": precioFinalProducto,
        }

        # Lógica para evitar productos repetidos y límite de 3
        productoExistente = False
        for indice, item in enumerate(listaCesta):
            if item["producto"] == nombreProducto:
                # Si ya existe el producto, se reemplaza el anterior por el nuevo
                listaCesta[indice] = nuevoProducto
                productoExistente = True
                break
        
        if not productoExistente:
            # Si no existe y hay espacio, se añade
            if len(listaCesta) < 3:
                listaCesta.append(nuevoProducto)

        # Recalculamos el importe total sumando los precios de lo que hay en la cesta
        importeTotal[0] = sum(articulo["precio"] for articulo in listaCesta)
        
        # Actualizamos el campo de importe total en la ventana principal
        self.leImporte.setText(str(importeTotal[0]))

        # Reiniciamos la ventana a su estado inicial tras añadir el producto
        self.reiniciarVentana()
        
        # Activamos el botón "Ver cesta" porque ya hay al menos un producto
        self.botonVerCesta.setEnabled(len(listaCesta) > 0)

    def abrirCesta(self):
        # Importamos aquí para evitar referencias circulares
        from principal_cesta import VentanaCestaCompra
        
        self.ventanaCesta = VentanaCestaCompra(listaCesta, importeTotal)
        self.ventanaCesta.show()

    def reiniciarControles(self):
        # Desactivamos temporalmente la exclusividad de los RadioButtons para poder deseleccionarlos
        self.rbS.setAutoExclusive(False)
        self.rbM.setAutoExclusive(False)
        self.rbL.setAutoExclusive(False)
        self.rbXL.setAutoExclusive(False)
        
        self.rbS.setChecked(False)
        self.rbM.setChecked(False)
        self.rbL.setChecked(False)
        self.rbXL.setChecked(False)
        
        # Volvemos a activar la exclusividad
        self.rbS.setAutoExclusive(True)
        self.rbM.setAutoExclusive(True)
        self.rbL.setAutoExclusive(True)
        self.rbXL.setAutoExclusive(True)
        
        # Desmarcamos los extras y limpiamos el campo del precio individual
        self.cbEstampado.setChecked(False)
        self.cbEnvioRapido.setChecked(False)
        self.cbEnvolturaRegalo.setChecked(False)
        self.lePrecioFinal.setText("")

    def reiniciarVentana(self):
        # Devuelve la ventana a su estado original deshabilitando todo
        self.comboBox.setCurrentIndex(0)
        self.reiniciarControles()
        self.rbS.setEnabled(False)
        self.rbM.setEnabled(False)
        self.rbL.setEnabled(False)
        self.rbXL.setEnabled(False)
        self.cbEstampado.setEnabled(False)
        self.cbEnvioRapido.setEnabled(False)
        self.cbEnvolturaRegalo.setEnabled(False)
        self.pbCalcularPrecio.setEnabled(False)
        self.botonAnadir.setEnabled(False)

def main():
    aplicacion = QApplication(sys.argv)
    ventanaPrincipal = VentanaProducto()
    ventanaPrincipal.show()
    sys.exit(aplicacion.exec())

if __name__ == '__main__':
    main()