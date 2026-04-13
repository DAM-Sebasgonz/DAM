# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pushButton_02.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(553, 190)
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 46, 113, 32))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Normal", None))
        
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 50, 171, 21))
        
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 100, 171, 21))
        
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 97, 113, 32))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(True)
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Toggle", None))
        
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(360, 100, 171, 21))
        
        #código generado para ordenar el tabIndex de los controles

        QWidget.setTabOrder(self.pushButton, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)

        # nuestro código 

        self.pushButton.clicked.connect(self.botonNormalPresionado)
        self.pushButton_2.clicked.connect(self.botonTogglePresionado)
        self.pushButton_2.toggled.connect(self.botonToggleConEstado)

    # setupUi

    def botonNormalPresionado(self):
        self.lineEdit.setText('Clic en botón normal')

    def botonTogglePresionado(self):
        self.lineEdit_2.setText('Tb se reconoce el clic')
        pass

    def botonToggleConEstado(self):
        if self.pushButton_2.isChecked():
            self.lineEdit_3.setText('Estado actual ACTIVADO')
            self.pushButton_2.setChecked(True)
        else:
            self.lineEdit_3.setText('Estado actual No ACTIVADO')
            self.pushButton_2.setChecked(False)
