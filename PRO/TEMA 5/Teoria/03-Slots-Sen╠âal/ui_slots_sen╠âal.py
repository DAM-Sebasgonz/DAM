# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'slots_señal.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget, QMessageBox)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(277, 172)
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        
        self.pushMostrar = QPushButton(Form)
        self.pushMostrar.setObjectName(u"pushMostrar")
        self.pushMostrar.setGeometry(QRect(60, 70, 151, 32))
        self.pushMostrar.setText(QCoreApplication.translate("Form", u"Mostrar Ventana", None))

        # para conectar el método clicked con el código a ejecutar
        self.pushMostrar.clicked.connect(self.btnMostrar)

    # setupUi

    def btnMostrar(self):
        ventDialogo = QMessageBox()
        ventDialogo.setText('Haz hecho clic en el botón')
        ventDialogo.exec()
