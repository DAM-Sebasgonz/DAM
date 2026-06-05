import sys
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton, QStatusBar, QWidget

class UiCalculadora(object):
    def configurarInterfaz(self, ventanaPrincipal):
        if not ventanaPrincipal.objectName():
            ventanaPrincipal.setObjectName(u"Calculadora")
        ventanaPrincipal.resize(491, 600)
        
        self.widgetCentral = QWidget(ventanaPrincipal)
        self.widgetCentral.setObjectName(u"widgetCentral")
        
        # --- DEFINICIÓN DE LA PANTALLA (Visor) ---
        self.pantallaVisor = QLineEdit(self.widgetCentral)
        self.pantallaVisor.setObjectName(u"pantallaVisor")
        self.pantallaVisor.setGeometry(QRect(10, 10, 471, 111))
        self.pantallaVisor.setReadOnly(True)
        
        # --- DEFINICIÓN DE BOTONES NUMÉRICOS ---
        self.boton1 = QPushButton(self.widgetCentral)
        self.boton1.setGeometry(QRect(40, 160, 81, 71))
        self.boton1.setText("1")
        
        self.boton2 = QPushButton(self.widgetCentral)
        self.boton2.setGeometry(QRect(150, 160, 81, 71))
        self.boton2.setText("2")
        
        self.boton3 = QPushButton(self.widgetCentral)
        self.boton3.setGeometry(QRect(260, 160, 81, 71))
        self.boton3.setText("3")
        
        self.boton4 = QPushButton(self.widgetCentral)
        self.boton4.setGeometry(QRect(40, 250, 81, 71))
        self.boton4.setText("4")
        
        self.boton5 = QPushButton(self.widgetCentral)
        self.boton5.setGeometry(QRect(150, 250, 81, 71))
        self.boton5.setText("5")
        
        self.boton6 = QPushButton(self.widgetCentral)
        self.boton6.setGeometry(QRect(260, 250, 81, 71))
        self.boton6.setText("6")
        
        self.boton7 = QPushButton(self.widgetCentral)
        self.boton7.setGeometry(QRect(40, 340, 81, 71))
        self.boton7.setText("7")
        
        self.boton8 = QPushButton(self.widgetCentral)
        self.boton8.setGeometry(QRect(150, 340, 81, 71))
        self.boton8.setText("8")
        
        self.boton9 = QPushButton(self.widgetCentral)
        self.boton9.setGeometry(QRect(260, 340, 81, 71))
        self.boton9.setText("9")
        
        self.boton0 = QPushButton(self.widgetCentral)
        self.boton0.setGeometry(QRect(150, 430, 81, 71))
        self.boton0.setText("0")
        
        # --- DEFINICIÓN DE BOTONES DE OPERACIONES Y CONTROL ---
        self.botonSuma = QPushButton(self.widgetCentral)
        self.botonSuma.setGeometry(QRect(370, 160, 81, 71))
        self.botonSuma.setText("+")
        
        self.botonResta = QPushButton(self.widgetCentral)
        self.botonResta.setGeometry(QRect(370, 250, 81, 71))
        self.botonResta.setText("-")
        
        self.botonMultiplicacion = QPushButton(self.widgetCentral)
        self.botonMultiplicacion.setGeometry(QRect(370, 340, 81, 71))
        self.botonMultiplicacion.setText("*")
        
        self.botonDivision = QPushButton(self.widgetCentral)
        self.botonDivision.setGeometry(QRect(370, 430, 81, 71))
        self.botonDivision.setText("/")
        
        self.botonIgual = QPushButton(self.widgetCentral)
        self.botonIgual.setGeometry(QRect(260, 430, 81, 71))
        self.botonIgual.setText("=")
        
        self.botonBorrar = QPushButton(self.widgetCentral)
        self.botonBorrar.setGeometry(QRect(40, 430, 81, 71))
        self.botonBorrar.setText("<")
        
        ventanaPrincipal.setCentralWidget(self.widgetCentral)
        self.barraEstado = QStatusBar(ventanaPrincipal)
        ventanaPrincipal.setStatusBar(self.barraEstado)
        ventanaPrincipal.setWindowTitle("Calculadora")


class CalculadoraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = UiCalculadora()
        self.ui.configurarInterfaz(self)
        
        self.ui.pantallaVisor.setText("0")
        
        # Conectamos todos los botones de numeros y operadores al mismo metodo
        # dentro del metodo usamos sender() para saber cual se pulso
        self.ui.boton0.clicked.connect(self.agregarCaracter)
        self.ui.boton1.clicked.connect(self.agregarCaracter)
        self.ui.boton2.clicked.connect(self.agregarCaracter)
        self.ui.boton3.clicked.connect(self.agregarCaracter)
        self.ui.boton4.clicked.connect(self.agregarCaracter)
        self.ui.boton5.clicked.connect(self.agregarCaracter)
        self.ui.boton6.clicked.connect(self.agregarCaracter)
        self.ui.boton7.clicked.connect(self.agregarCaracter)
        self.ui.boton8.clicked.connect(self.agregarCaracter)
        self.ui.boton9.clicked.connect(self.agregarCaracter)
        
        self.ui.botonSuma.clicked.connect(self.agregarCaracter)
        self.ui.botonResta.clicked.connect(self.agregarCaracter)
        self.ui.botonMultiplicacion.clicked.connect(self.agregarCaracter)
        self.ui.botonDivision.clicked.connect(self.agregarCaracter)
        
        self.ui.botonBorrar.clicked.connect(self.borrarUltimoCaracter)
        self.ui.botonIgual.clicked.connect(self.calcularResultado)

    def agregarCaracter(self):
        # sender() nos devuelve el boton que disparo la señal
        # con text() leemos lo que pone en el boton: "1", "+", etc.
        caracter = self.sender().text()
        textoActual = self.ui.pantallaVisor.text()
        
        if textoActual == "0" or textoActual == "Error":
            if caracter.isdigit() or caracter == "-":
                self.ui.pantallaVisor.setText(caracter)
            else:
                self.ui.pantallaVisor.setText("0" + caracter)
        else:
            self.ui.pantallaVisor.setText(textoActual + caracter)

    def borrarUltimoCaracter(self):
        textoActual = self.ui.pantallaVisor.text()
        
        if textoActual == "Error":
            self.ui.pantallaVisor.setText("0")
            return
            
        nuevoTexto = textoActual[:-1]
        
        if len(nuevoTexto) == 0:
            self.ui.pantallaVisor.setText("0")
        else:
            self.ui.pantallaVisor.setText(nuevoTexto)

    def calcularResultado(self):
        expresion = self.ui.pantallaVisor.text()
        
        try:
            expresionProcesada = expresion.replace("/", "//")
            resultado = eval(expresionProcesada)
            self.ui.pantallaVisor.setText(str(resultado))
            
        except ZeroDivisionError:
            self.ui.pantallaVisor.setText("Error")
        except Exception:
            self.ui.pantallaVisor.setText("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CalculadoraPrincipal()
    ventana.show()
    sys.exit(app.exec())