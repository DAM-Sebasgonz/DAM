# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CestaCompra.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        self.labelTitulo = QLabel(Form)
        self.labelTitulo.setObjectName(u"labelTitulo")
        self.labelTitulo.setGeometry(QRect(210, 30, 221, 51))
        self.label1 = QLabel(Form)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(30, 140, 31, 31))
        self.label2 = QLabel(Form)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(30, 200, 31, 51))
        self.label3 = QLabel(Form)
        self.label3.setObjectName(u"label3")
        self.label3.setGeometry(QRect(30, 270, 31, 51))
        self.labelSeleccion = QLabel(Form)
        self.labelSeleccion.setObjectName(u"labelSeleccion")
        self.labelSeleccion.setGeometry(QRect(70, 110, 55, 16))
        self.cbSeleccion1 = QCheckBox(Form)
        self.cbSeleccion1.setObjectName(u"cbSeleccion1")
        self.cbSeleccion1.setGeometry(QRect(90, 150, 21, 20))
        self.cbSeleccion2 = QCheckBox(Form)
        self.cbSeleccion2.setObjectName(u"cbSeleccion2")
        self.cbSeleccion2.setGeometry(QRect(90, 220, 21, 20))
        self.cbSeleccion3 = QCheckBox(Form)
        self.cbSeleccion3.setObjectName(u"cbSeleccion3")
        self.cbSeleccion3.setGeometry(QRect(90, 290, 21, 20))
        self.labelProducto = QLabel(Form)
        self.labelProducto.setObjectName(u"labelProducto")
        self.labelProducto.setGeometry(QRect(170, 110, 55, 16))
        self.leProducto1 = QLineEdit(Form)
        self.leProducto1.setObjectName(u"leProducto1")
        self.leProducto1.setGeometry(QRect(140, 150, 111, 22))
        self.leProducto2 = QLineEdit(Form)
        self.leProducto2.setObjectName(u"leProducto2")
        self.leProducto2.setGeometry(QRect(140, 220, 113, 22))
        self.leProducto3 = QLineEdit(Form)
        self.leProducto3.setObjectName(u"leProducto3")
        self.leProducto3.setGeometry(QRect(140, 290, 113, 22))
        self.labelTalla = QLabel(Form)
        self.labelTalla.setObjectName(u"labelTalla")
        self.labelTalla.setGeometry(QRect(280, 110, 55, 16))
        self.leTalla1 = QLineEdit(Form)
        self.leTalla1.setObjectName(u"leTalla1")
        self.leTalla1.setGeometry(QRect(270, 150, 51, 22))
        self.leTalla2 = QLineEdit(Form)
        self.leTalla2.setObjectName(u"leTalla2")
        self.leTalla2.setGeometry(QRect(270, 220, 51, 22))
        self.leTalla3 = QLineEdit(Form)
        self.leTalla3.setObjectName(u"leTalla3")
        self.leTalla3.setGeometry(QRect(270, 290, 51, 22))
        self.cbEstampado1 = QCheckBox(Form)
        self.cbEstampado1.setObjectName(u"cbEstampado1")
        self.cbEstampado1.setGeometry(QRect(370, 150, 21, 20))
        self.cbEstampado2 = QCheckBox(Form)
        self.cbEstampado2.setObjectName(u"cbEstampado2")
        self.cbEstampado2.setGeometry(QRect(370, 220, 21, 20))
        self.labelEstampado = QLabel(Form)
        self.labelEstampado.setObjectName(u"labelEstampado")
        self.labelEstampado.setGeometry(QRect(350, 110, 71, 16))
        self.cbEstampado3 = QCheckBox(Form)
        self.cbEstampado3.setObjectName(u"cbEstampado3")
        self.cbEstampado3.setGeometry(QRect(370, 290, 21, 20))
        self.labelEnvio = QLabel(Form)
        self.labelEnvio.setObjectName(u"labelEnvio")
        self.labelEnvio.setGeometry(QRect(440, 110, 71, 16))
        self.cbEnvio2 = QCheckBox(Form)
        self.cbEnvio2.setObjectName(u"cbEnvio2")
        self.cbEnvio2.setGeometry(QRect(470, 220, 21, 20))
        self.cbEnvio3 = QCheckBox(Form)
        self.cbEnvio3.setObjectName(u"cbEnvio3")
        self.cbEnvio3.setGeometry(QRect(470, 290, 21, 20))
        self.cbEnvio1 = QCheckBox(Form)
        self.cbEnvio1.setObjectName(u"cbEnvio1")
        self.cbEnvio1.setGeometry(QRect(470, 150, 21, 20))
        self.cbEnvoltura2 = QCheckBox(Form)
        self.cbEnvoltura2.setObjectName(u"cbEnvoltura2")
        self.cbEnvoltura2.setGeometry(QRect(570, 220, 21, 20))
        self.labelEnvoltura = QLabel(Form)
        self.labelEnvoltura.setObjectName(u"labelEnvoltura")
        self.labelEnvoltura.setGeometry(QRect(530, 110, 101, 16))
        self.cbEnvoltura3 = QCheckBox(Form)
        self.cbEnvoltura3.setObjectName(u"cbEnvoltura3")
        self.cbEnvoltura3.setGeometry(QRect(570, 290, 21, 20))
        self.cbEnvoltura1 = QCheckBox(Form)
        self.cbEnvoltura1.setObjectName(u"cbEnvoltura1")
        self.cbEnvoltura1.setGeometry(QRect(570, 150, 21, 20))
        self.pbEliminar = QPushButton(Form)
        self.pbEliminar.setObjectName(u"pbEliminar")
        self.pbEliminar.setGeometry(QRect(140, 370, 93, 28))
        self.pbVaciarCesta = QPushButton(Form)
        self.pbVaciarCesta.setObjectName(u"pbVaciarCesta")
        self.pbVaciarCesta.setGeometry(QRect(270, 370, 93, 28))
        self.pbComprar = QPushButton(Form)
        self.pbComprar.setObjectName(u"pbComprar")
        self.pbComprar.setGeometry(QRect(400, 370, 93, 28))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelTitulo.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\"\n"
"                    font-size:14pt; font-weight:600;\">Cesta de la\n"
"                    compra</span></p></body></html>", None))
        self.label1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\"\n"
"                    font-size:14pt;\n"
"                    font-weight:600;\">1</span></p></body></html>", None))
        self.label2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\"\n"
"                    font-size:14pt;\n"
"                    font-weight:600;\">2</span></p></body></html>", None))
        self.label3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\"\n"
"                    font-size:14pt;\n"
"                    font-weight:600;\">3</span></p></body></html>", None))
        self.labelSeleccion.setText(QCoreApplication.translate("Form", u"Selecci\u00f3n", None))
        self.cbSeleccion1.setText("")
        self.cbSeleccion2.setText("")
        self.cbSeleccion3.setText("")
        self.labelProducto.setText(QCoreApplication.translate("Form", u"Producto", None))
        self.labelTalla.setText(QCoreApplication.translate("Form", u"Talla", None))
        self.cbEstampado1.setText("")
        self.cbEstampado2.setText("")
        self.labelEstampado.setText(QCoreApplication.translate("Form", u"Estampado", None))
        self.cbEstampado3.setText("")
        self.labelEnvio.setText(QCoreApplication.translate("Form", u"Env\u00edo r\u00e1pido", None))
        self.cbEnvio2.setText("")
        self.cbEnvio3.setText("")
        self.cbEnvio1.setText("")
        self.cbEnvoltura2.setText("")
        self.labelEnvoltura.setText(QCoreApplication.translate("Form", u"Envoltura regalo", None))
        self.cbEnvoltura3.setText("")
        self.cbEnvoltura1.setText("")
        self.pbEliminar.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.pbVaciarCesta.setText(QCoreApplication.translate("Form", u"Vaciar cesta", None))
        self.pbComprar.setText(QCoreApplication.translate("Form", u"Comprar", None))
    # retranslateUi

