# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Formulario.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QGroupBox,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        font = QFont()
        font.setPointSize(11)
        Form.setFont(font)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 55, 16))
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)
        self.le_nif = QLineEdit(Form)
        self.le_nif.setObjectName(u"le_nif")
        self.le_nif.setEnabled(False)
        self.le_nif.setGeometry(QRect(110, 30, 188, 28))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 71, 16))
        self.label_2.setFont(font1)
        self.le_nombre = QLineEdit(Form)
        self.le_nombre.setObjectName(u"le_nombre")
        self.le_nombre.setEnabled(False)
        self.le_nombre.setGeometry(QRect(110, 70, 188, 28))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 130, 81, 16))
        self.label_3.setFont(font1)
        self.le_apellidos = QLineEdit(Form)
        self.le_apellidos.setObjectName(u"le_apellidos")
        self.le_apellidos.setEnabled(False)
        self.le_apellidos.setGeometry(QRect(110, 120, 188, 28))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(420, 30, 81, 16))
        self.label_4.setFont(font1)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(370, 20, 231, 121))
        self.groupBox.setFont(font1)
        self.cb_practica = QCheckBox(self.groupBox)
        self.cb_practica.setObjectName(u"cb_practica")
        self.cb_practica.setEnabled(False)
        self.cb_practica.setGeometry(QRect(10, 30, 101, 20))
        self.le_deporte = QLineEdit(self.groupBox)
        self.le_deporte.setObjectName(u"le_deporte")
        self.le_deporte.setEnabled(False)
        self.le_deporte.setGeometry(QRect(20, 70, 191, 22))
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 220, 141, 101))
        self.groupBox_2.setFont(font1)
        self.rb_mujer = QRadioButton(self.groupBox_2)
        self.buttonGroupSex = QButtonGroup(Form)
        self.buttonGroupSex.setObjectName(u"buttonGroupSex")
        self.buttonGroupSex.addButton(self.rb_mujer)
        self.rb_mujer.setObjectName(u"rb_mujer")
        self.rb_mujer.setEnabled(False)
        self.rb_mujer.setGeometry(QRect(10, 30, 95, 20))
        self.rb_hombre = QRadioButton(self.groupBox_2)
        self.buttonGroupSex.addButton(self.rb_hombre)
        self.rb_hombre.setObjectName(u"rb_hombre")
        self.rb_hombre.setEnabled(False)
        self.rb_hombre.setGeometry(QRect(10, 60, 95, 20))
        self.rb_hombre.setFont(font1)
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(370, 220, 251, 131))
        self.radioButton = QRadioButton(self.groupBox_3)
        self.buttonGroupTrabaja = QButtonGroup(Form)
        self.buttonGroupTrabaja.setObjectName(u"buttonGroupTrabaja")
        self.buttonGroupTrabaja.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(False)
        self.radioButton.setGeometry(QRect(10, 40, 95, 20))
        self.radioButton_2 = QRadioButton(self.groupBox_3)
        self.buttonGroupTrabaja.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setGeometry(QRect(10, 70, 95, 20))
        self.le_trabaja = QLineEdit(self.groupBox_3)
        self.le_trabaja.setObjectName(u"le_trabaja")
        self.le_trabaja.setGeometry(QRect(90, 50, 113, 22))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 430, 93, 28))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 430, 93, 28))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(390, 430, 93, 28))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"NIF", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Apellidos", None))
        self.label_4.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Deportes", None))
        self.cb_practica.setText(QCoreApplication.translate("Form", u"Practico", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Sexo", None))
        self.rb_mujer.setText(QCoreApplication.translate("Form", u"Mujer", None))
        self.rb_hombre.setText(QCoreApplication.translate("Form", u"Hombre", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Trabaja", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"No", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"Si", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Insertar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Modificar", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Borrar", None))
    # retranslateUi

