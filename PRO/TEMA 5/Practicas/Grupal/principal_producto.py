import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from producto_ui import Ui_Form

preciosBase = {
    "Camiseta": 20,
    "Sudadera": 40,
    "Chandal": 55,
}

listaCesta = [] 

class VentanaProducto(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(VentanaProducto, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Tienda Deportiva")
        
        self.importeTotal = 0.0
        # A ver podiamos haberlo hecho de dos maneras una con una variable global (del tipo importeTotal = [0.0]) o con una herencia de la clase VentanaProducto.

        # Nos olvidamos de poner los botones Añadir y Ver cesta en el QTdesigner así que los pusimos aquí
        self.botonAnadir = QPushButton("Añadir", self)
        self.botonAnadir.setGeometry(80, 440, 93, 28)
        self.botonAnadir.setEnabled(False)

        self.botonVerCesta = QPushButton("Ver cesta", self)
        self.botonVerCesta.setGeometry(190, 440, 93, 28)
        self.botonVerCesta.setEnabled(False)

        self.resize(312, 490)

        self.lePrecioFinal.setEnabled(False)
        self.leImporte.setEnabled(False)

        self.comboBox.currentIndexChanged.connect(self.alCambiarProducto)
        self.pbCalcularPrecio.clicked.connect(self.calcularPrecio)
        self.botonAnadir.clicked.connect(self.anadirProducto)
        self.botonVerCesta.clicked.connect(self.abrirCesta)

        self.ventanaCesta = None

    def alCambiarProducto(self, indice):
        productoValido = indice > 0

        self.rbS.setEnabled(productoValido)
        self.rbM.setEnabled(productoValido)
        self.rbL.setEnabled(productoValido)
        self.rbXL.setEnabled(productoValido)
        self.cbEstampado.setEnabled(productoValido)
        self.cbEnvioRapido.setEnabled(productoValido)
        self.cbEnvolturaRegalo.setEnabled(productoValido)
        self.pbCalcularPrecio.setEnabled(productoValido)
        self.botonAnadir.setEnabled(productoValido)

        if not productoValido:
            self.reiniciarControles()

    def calcularPrecio(self):
        nombreProducto = self.comboBox.currentText()
        precioCalculado = preciosBase.get(nombreProducto, 0)

        if self.cbEstampado.isChecked():
            precioCalculado += 5
        if self.cbEnvioRapido.isChecked():
            precioCalculado += 10
        if self.cbEnvolturaRegalo.isChecked():
            precioCalculado += 3

        self.lePrecioFinal.setText(str(precioCalculado))

    def anadirProducto(self):
        nombreProducto = self.comboBox.currentText()
        
        tallaSeleccionada = ""
        if self.rbS.isChecked():
            tallaSeleccionada = "S"
        elif self.rbM.isChecked(): 
            tallaSeleccionada = "M"
        elif self.rbL.isChecked(): 
            tallaSeleccionada = "L"
        elif self.rbXL.isChecked():
            tallaSeleccionada = "XL"

        tieneEstampado = self.cbEstampado.isChecked()
        tieneEnvio = self.cbEnvioRapido.isChecked()
        tieneEnvoltura = self.cbEnvolturaRegalo.isChecked()

        textoPrecio = self.lePrecioFinal.text()
        precioFinalProducto = float(textoPrecio) if textoPrecio else preciosBase.get(nombreProducto, 0)

        nuevoProducto = {
            "producto": nombreProducto,
            "talla": tallaSeleccionada,
            "estampado": tieneEstampado,
            "envio": tieneEnvio,
            "envoltura": tieneEnvoltura,
            "precio": precioFinalProducto,
        }

        productoExistente = False
        for indice, item in enumerate(listaCesta):
            if item["producto"] == nombreProducto:
                listaCesta[indice] = nuevoProducto
                productoExistente = True
                break
        
        if not productoExistente:
            if len(listaCesta) < 3:
                listaCesta.append(nuevoProducto)

        self.importeTotal = sum(articulo["precio"] for articulo in listaCesta)
        self.leImporte.setText(str(self.importeTotal))
        self.reiniciarVentana()
        self.botonVerCesta.setEnabled(len(listaCesta) > 0)

    def abrirCesta(self):
        from principal_cesta import VentanaCestaCompra
        self.ventanaCesta = VentanaCestaCompra(listaCesta, self.importeTotal, ventanaPadre = self)
        self.ventanaCesta.show()

    def reiniciarControles(self):
        self.rbS.setAutoExclusive(False)
        self.rbM.setAutoExclusive(False)
        self.rbL.setAutoExclusive(False)
        self.rbXL.setAutoExclusive(False)
        
        self.rbS.setChecked(False)
        self.rbM.setChecked(False)
        self.rbL.setChecked(False)
        self.rbXL.setChecked(False)
        
        self.rbS.setAutoExclusive(True)
        self.rbM.setAutoExclusive(True)
        self.rbL.setAutoExclusive(True)
        self.rbXL.setAutoExclusive(True)
        
        self.cbEstampado.setChecked(False)
        self.cbEnvioRapido.setChecked(False)
        self.cbEnvolturaRegalo.setChecked(False)

        self.lePrecioFinal.setText("")

    def reiniciarVentana(self):
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