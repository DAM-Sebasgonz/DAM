import os
import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_label import Ui_formEtiqueta

class ClaseVentana(QWidget, Ui_formEtiqueta):
    def __init__(self, parent=None):
        super(ClaseVentana, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv) # o [] si no hay paso de argumentos
    window = ClaseVentana()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
