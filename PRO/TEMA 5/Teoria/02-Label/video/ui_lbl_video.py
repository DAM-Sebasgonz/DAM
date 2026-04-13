# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lbl_video.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QSize)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QMovie)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 210)
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Etiqueta video", None))


        # 1. Crear el QLabel que contendrá la animación
        self.label_animacion = QLabel(Form)
        self.label_animacion.setGeometry(QRect(60, 60, 150, 150)) # cambiar
        self.label_animacion.setText("")

        self.label_animacion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Crear QMovie con la ruta del GIF
        self.movie = QMovie("02-Label/video/python.gif") 
        
        # Verificar si se cargó correctamente
        if self.movie.isValid():
            
            # Para escalar el video QMovie no tiene método scale, 
            # necesitamos escalar el label
            # Establecer tamaño fijo para el label 
            self.label_animacion.setFixedSize(100, 100)
            
            # Escalar el GIF al tamaño del label
            self.movie.setScaledSize(self.label_animacion.size())
            
            # Asignar el movie al label
            self.label_animacion.setMovie(self.movie)
            
            # Iniciar la animación
            self.movie.start()
        else:
            self.label_animacion.setText("No se pudo cargar el GIF")
            self.label_animacion.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # setupUi
