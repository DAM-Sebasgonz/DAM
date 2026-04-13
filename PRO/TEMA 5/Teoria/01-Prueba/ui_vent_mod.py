# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vent_mod.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Ventana(object):
    def setupUi(self, Ventana):
        if not Ventana.objectName():
            Ventana.setObjectName(u"Ventana")
        Ventana.resize(509, 351)
        Ventana.setWindowTitle(QCoreApplication.translate("Ventana", u"Ventana de Prueba", None))

        self.label = QLabel(Ventana)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 80, 60, 16))
        self.label.setText(QCoreApplication.translate("Ventana", u"TextLabel", None))
        
        self.lineEdit = QLineEdit(Ventana)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(220, 80, 113, 21))
        
        self.label_2 = QLabel(Ventana)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 130, 80, 16))
        self.label_2.setText(QCoreApplication.translate("Ventana", u"Copia texto", None))
        
        self.lineEdit_2 = QLineEdit(Ventana)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(220, 130, 113, 21))
        
        self.pushButton = QPushButton(Ventana)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 200, 113, 32))
        self.pushButton.setText(QCoreApplication.translate("Ventana", u"Haz clic", None))

        # a partir de aquí podemos añadir nuestro código

    # setupUi

# a partir de aquí podemos añadir los métodos de la clase que 
