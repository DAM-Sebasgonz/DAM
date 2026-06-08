# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'producto.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(312, 480)
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))

        self.labelProducto = QLabel(Form)
        self.labelProducto.setObjectName(u"labelProducto")
        self.labelProducto.setGeometry(QRect(120, 30, 61, 16))
        self.labelProducto.setText(QCoreApplication.translate("Form", u"Producto:", None))

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(80, 60, 131, 22))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Camiseta", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Sudadera", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Chandal", None))

        self.labelTalla = QLabel(Form)
        self.labelTalla.setObjectName(u"labelTalla")
        self.labelTalla.setGeometry(QRect(50, 100, 55, 16))
        self.labelTalla.setText(QCoreApplication.translate("Form", u"Talla:", None))

        self.rbS = QRadioButton(Form)
        self.rbS.setObjectName(u"rbS")
        self.rbS.setEnabled(False)
        self.rbS.setGeometry(QRect(50, 140, 41, 20))
        self.rbS.setText(QCoreApplication.translate("Form", u"S", None))

        self.rbM = QRadioButton(Form)
        self.rbM.setObjectName(u"rbM")
        self.rbM.setEnabled(False)
        self.rbM.setGeometry(QRect(100, 140, 41, 20))
        self.rbM.setText(QCoreApplication.translate("Form", u"M", None))

        self.rbL = QRadioButton(Form)
        self.rbL.setObjectName(u"rbL")
        self.rbL.setEnabled(False)
        self.rbL.setGeometry(QRect(150, 140, 41, 20))
        self.rbL.setText(QCoreApplication.translate("Form", u"L", None))

        self.rbXL = QRadioButton(Form)
        self.rbXL.setObjectName(u"rbXL")
        self.rbXL.setEnabled(False)
        self.rbXL.setGeometry(QRect(200, 140, 41, 20))
        self.rbXL.setText(QCoreApplication.translate("Form", u"XL", None))

        self.labelExtras = QLabel(Form)
        self.labelExtras.setObjectName(u"labelExtras")
        self.labelExtras.setGeometry(QRect(50, 180, 55, 16))
        self.labelExtras.setText(QCoreApplication.translate("Form", u"Extras:", None))

        self.cbEstampado = QCheckBox(Form)
        self.cbEstampado.setObjectName(u"cbEstampado")
        self.cbEstampado.setEnabled(False)
        self.cbEstampado.setGeometry(QRect(80, 210, 131, 20))
        self.cbEstampado.setText(QCoreApplication.translate("Form", u"Estampado (+5\u20ac)", None))

        self.cbEnvioRapido = QCheckBox(Form)
        self.cbEnvioRapido.setObjectName(u"cbEnvioRapido")
        self.cbEnvioRapido.setEnabled(False)
        self.cbEnvioRapido.setGeometry(QRect(80, 250, 141, 20))
        self.cbEnvioRapido.setText(QCoreApplication.translate("Form", u"Env\u00edo r\u00e1pido (+10\u20ac)", None))

        self.cbEnvolturaRegalo = QCheckBox(Form)
        self.cbEnvolturaRegalo.setObjectName(u"cbEnvolturaRegalo")
        self.cbEnvolturaRegalo.setEnabled(False)
        self.cbEnvolturaRegalo.setGeometry(QRect(80, 290, 161, 20))
        self.cbEnvolturaRegalo.setText(QCoreApplication.translate("Form", u"Envoltura regalo (+3\u20ac)", None))

        self.pbCalcularPrecio = QPushButton(Form)
        self.pbCalcularPrecio.setObjectName(u"pbCalcularPrecio")
        self.pbCalcularPrecio.setEnabled(False)
        self.pbCalcularPrecio.setGeometry(QRect(100, 330, 93, 28))
        self.pbCalcularPrecio.setText(QCoreApplication.translate("Form", u"Calcular precio", None))

        self.labelPrecioFinal = QLabel(Form)
        self.labelPrecioFinal.setObjectName(u"labelPrecioFinal")
        self.labelPrecioFinal.setGeometry(QRect(30, 380, 151, 16))

        self.labelImporte = QLabel(Form)
        self.labelImporte.setObjectName(u"labelImporte")
        self.labelImporte.setGeometry(QRect(30, 410, 141, 16))

        self.lePrecioFinal = QLineEdit(Form)
        self.lePrecioFinal.setObjectName(u"lePrecioFinal")
        self.lePrecioFinal.setEnabled(False)
        self.lePrecioFinal.setGeometry(QRect(190, 380, 91, 22))
        self.labelPrecioFinal.setText(QCoreApplication.translate("Form", u"Precio final producto (\u20ac)", None))

        self.leImporte = QLineEdit(Form)
        self.leImporte.setObjectName(u"leImporte")
        self.leImporte.setEnabled(False)
        self.leImporte.setGeometry(QRect(190, 410, 91, 22))
        self.labelImporte.setText(QCoreApplication.translate("Form", u"Importe del pedido (\u20ac)", None))