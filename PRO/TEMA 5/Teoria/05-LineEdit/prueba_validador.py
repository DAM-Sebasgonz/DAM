import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QLabel
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

class VentanaValidacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Validadores y Máscaras en QLineEdit")
        self.setGeometry(100, 100, 400, 200)

        # Widget central y layout vertical
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # 1. Ejemplo con QIntValidator (solo números del 0 al 999)
        lbl1 = QLabel("Edad (0-999) - Validador entero:")
        self.edit_edad = QLineEdit()
        validador_int = QIntValidator(0, 999)
        self.edit_edad.setValidator(validador_int)
        layout.addWidget(lbl1)
        layout.addWidget(self.edit_edad)

        # 2. Ejemplo con expresión regular (solo letras mayúsculas y minúsculas)
        lbl2 = QLabel("Nombre (solo letras) - Validador Regex:")
        self.edit_nombre = QLineEdit()
        regex = QRegularExpression("^[A-Za-záéíóúüñÁÉÍÓÚÜÑ]+$")
        validador_regex = QRegularExpressionValidator(regex)
        self.edit_nombre.setValidator(validador_regex)
        layout.addWidget(lbl2)
        layout.addWidget(self.edit_nombre)

        # 3. Ejemplo con InputMask para teléfono fijo (9 dígitos, formato XXX-XXX-XXX)
        lbl3 = QLabel("Teléfono (formato 999-999-999) - InputMask:")
        self.edit_telefono = QLineEdit()
        self.edit_telefono.setInputMask("999-999-999")  # 9 dígitos con guiones fijos
        layout.addWidget(lbl3)
        layout.addWidget(self.edit_telefono)

        # 4. Ejemplo con InputMask para fecha (DD/MM/AAAA)
        lbl4 = QLabel("Fecha (DD/MM/AAAA) - InputMask:")
        self.edit_fecha = QLineEdit()
        self.edit_fecha.setInputMask("00/00/0000")
        layout.addWidget(lbl4)
        layout.addWidget(self.edit_fecha)

        # Mostramos texto actual (solo para depuración, usando QLabel)
        self.lbl_info = QLabel("Prueba a escribir en cada campo...")
        layout.addWidget(self.lbl_info)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaValidacion()
    ventana.show()
    sys.exit(app.exec())