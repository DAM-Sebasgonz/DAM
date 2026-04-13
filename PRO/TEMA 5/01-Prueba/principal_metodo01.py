# Este código carga directamente el fichero .ui generado por
# QT Designer para mostrar la ventana contenido en el fichero 
# XML generado

import os
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
basedir = os.path.dirname(__file__)

def mainwindow_setup(w):
    w.setWindowTitle("Ventana Prueba")

def main():
    app = QApplication(sys.argv) # o [] si no hay paso de argumentos
    window = loader.load(os.path.join(basedir,"prueba.ui"), None)
    mainwindow_setup(window)
    window.show()
    app.exec()

if __name__ == '__main__':
    main()

