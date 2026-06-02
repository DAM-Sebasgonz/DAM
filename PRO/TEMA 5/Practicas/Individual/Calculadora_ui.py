import sys
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton, QStatusBar, QWidget

class UiCalculadora(object):
    def configurarInterfaz(self, ventanaPrincipal):
        # Configuración básica de la ventana principal
        if not ventanaPrincipal.objectName():
            ventanaPrincipal.setObjectName(u"Calculadora")
        ventanaPrincipal.resize(491, 600)
        
        # Widget central que contendrá todos los botones y la pantalla
        self.widgetCentral = QWidget(ventanaPrincipal)
        self.widgetCentral.setObjectName(u"widgetCentral")
        
        # --- DEFINICIÓN DE LA PANTALLA (Visor) ---
        self.pantallaVisor = QLineEdit(self.widgetCentral)
        self.pantallaVisor.setObjectName(u"pantallaVisor")
        self.pantallaVisor.setGeometry(QRect(10, 10, 471, 111))
        # Hacemos que sea de solo lectura para obligar a usar los botones
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
        
        # Configuraciones finales de la ventana
        ventanaPrincipal.setCentralWidget(self.widgetCentral)
        self.barraEstado = QStatusBar(ventanaPrincipal)
        ventanaPrincipal.setStatusBar(self.barraEstado)
        ventanaPrincipal.setWindowTitle("Calculadora")

class CalculadoraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Inicializamos la interfaz gráfica creada arriba
        self.ui = UiCalculadora()
        self.ui.configurarInterfaz(self)
        
        # Establecemos el valor inicial en el visor
        self.ui.pantallaVisor.setText("0")
        
        # Conectamos las señales (clicks) de los botones numéricos a la función agregarCaracter
        # Usamos 'lambda' para poder pasar el número específico como argumento a la función
        self.ui.boton0.clicked.connect(lambda: self.agregarCaracter("0"))
        self.ui.boton1.clicked.connect(lambda: self.agregarCaracter("1"))
        self.ui.boton2.clicked.connect(lambda: self.agregarCaracter("2"))
        self.ui.boton3.clicked.connect(lambda: self.agregarCaracter("3"))
        self.ui.boton4.clicked.connect(lambda: self.agregarCaracter("4"))
        self.ui.boton5.clicked.connect(lambda: self.agregarCaracter("5"))
        self.ui.boton6.clicked.connect(lambda: self.agregarCaracter("6"))
        self.ui.boton7.clicked.connect(lambda: self.agregarCaracter("7"))
        self.ui.boton8.clicked.connect(lambda: self.agregarCaracter("8"))
        self.ui.boton9.clicked.connect(lambda: self.agregarCaracter("9"))
        
        # Conectamos las señales de los botones de operaciones
        self.ui.botonSuma.clicked.connect(lambda: self.agregarCaracter("+"))
        self.ui.botonResta.clicked.connect(lambda: self.agregarCaracter("-"))
        self.ui.botonMultiplicacion.clicked.connect(lambda: self.agregarCaracter("*"))
        self.ui.botonDivision.clicked.connect(lambda: self.agregarCaracter("/"))
        
        # Conectamos los botones de control especiales (Borrar e Igual) a sus respectivas funciones
        self.ui.botonBorrar.clicked.connect(self.borrarUltimoCaracter)
        self.ui.botonIgual.clicked.connect(self.calcularResultado)

    def agregarCaracter(self, caracter):
        """Añade el número u operador al visor controlando el estado actual."""
        textoActual = self.ui.pantallaVisor.text()
        
        # Si la pantalla está en '0' o viene de un 'Error', reemplazamos el texto
        if textoActual == "0" or textoActual == "Error":
            # Solo reemplazamos si es un número o un signo negativo (para números negativos)
            if caracter.isdigit() or caracter == "-":
                self.ui.pantallaVisor.setText(caracter)
            else:
                # Si el usuario pulsa un operador (ej: '+'), lo concatenamos al '0'
                self.ui.pantallaVisor.setText("0" + caracter)
        else:
            # En cualquier otro caso, simplemente concatenamos el nuevo carácter
            self.ui.pantallaVisor.setText(textoActual + caracter)

    def borrarUltimoCaracter(self):
        """Borra el último dígito introducido. Si se queda vacío, muestra un 0."""
        textoActual = self.ui.pantallaVisor.text()
        
        # Si había un error, borrarlo restablece la calculadora a '0'
        if textoActual == "Error":
            self.ui.pantallaVisor.setText("0")
            return
            
        # Cortamos el último carácter usando slicing de Python
        nuevoTexto = textoActual[:-1]
        
        # Si al borrar nos quedamos sin texto, colocamos el '0' por defecto
        if len(nuevoTexto) == 0:
            self.ui.pantallaVisor.setText("0")
        else:
            self.ui.pantallaVisor.setText(nuevoTexto)

    def calcularResultado(self):
        """Evalúa la operación matemática de la pantalla y maneja posibles excepciones."""
        expresion = self.ui.pantallaVisor.text()
        
        try:
            # Reemplazamos la división normal '/' por la división entera '//' de Python
            # para cumplir con el requisito de no trabajar con decimales.
            expresionProcesada = expresion.replace("/", "//")
            
            # Evaluamos la expresión matemática. 'eval' entiende los dobles signos automáticamente (ej: +-)
            resultado = eval(expresionProcesada)
            
            # Mostramos el resultado convertido de nuevo a texto
            self.ui.pantallaVisor.setText(str(resultado))
            
        except ZeroDivisionError:
            # Capturamos la división por 0 para mostrar "Error"
            self.ui.pantallaVisor.setText("Error")
        except Exception:
            # Capturamos cualquier otro fallo (como sintaxis incorrecta: "5++*2")
            self.ui.pantallaVisor.setText("Error")

# =====================================================================
# EJECUCIÓN DE LA APLICACIÓN
# =====================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CalculadoraPrincipal()
    ventana.show()
    sys.exit(app.exec())