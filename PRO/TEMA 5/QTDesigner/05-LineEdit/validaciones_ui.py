# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'validaciones.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(577, 469)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 211, 16))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 60, 113, 21))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 100, 251, 16))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(40, 130, 113, 21))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 170, 341, 16))
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(40, 200, 113, 21))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 240, 261, 16))
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(170, 200, 113, 21))
        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(420, 200, 113, 21))
        self.lineEdit_6 = QLineEdit(Form)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(40, 270, 113, 21))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 193, 113, 40))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 310, 261, 16))
        self.lineEdit_7 = QLineEdit(Form)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(40, 340, 113, 21))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 380, 311, 16))
        self.lineEdit_8 = QLineEdit(Form)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(40, 410, 113, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Edad - Validador Entero (0-999)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nombre - (s\u00f3lo letras) Expresion Regular", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Tel\u00e9fono (formato 999-999-999) M\u00e1scara de entrada", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Fecha (DD/MM/AAA) M\u00e1scara de entrada", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Limpiar", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"NIF/NIE (DD/MM/AAA) Expresi\u00f3n Regular", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"NIF/NIE (DD/MM/AAA) Expresi\u00f3n Regular Validado", None))
    # retranslateUi

