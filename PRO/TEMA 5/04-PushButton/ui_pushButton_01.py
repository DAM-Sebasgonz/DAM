# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pushButton_01.ui'
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
        Form.resize(609, 310)
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        
        self.btn_01 = QPushButton(Form)
        self.btn_01.setObjectName(u"btn_01")
        self.btn_01.setGeometry(QRect(50, 40, 113, 32))
        self.btn_01.setText(QCoreApplication.translate("Form", u"Bot\u00f3n 01", None))
        
        self.btn_ico = QPushButton(Form)
        self.btn_ico.setObjectName(u"btn_ico")
        self.btn_ico.setGeometry(QRect(50, 100, 113, 32))
        self.btn_ico.setText("")
        icon = QIcon()
        icon.addFile(u"04-PushButton/python.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_ico.setIcon(icon)

        self.btn_03 = QPushButton(Form)
        self.btn_03.setObjectName(u"btn_03")
        self.btn_03.setGeometry(QRect(50, 160, 113, 32))
        self.btn_03.setText(QCoreApplication.translate("Form", u"Bot\u00f3n 03", None))
        
        self.btn_04 = QPushButton(Form)
        self.btn_04.setObjectName(u"btn_04")
        self.btn_04.setEnabled(False)
        self.btn_04.setGeometry(QRect(50, 220, 113, 32))
        self.btn_04.setText(QCoreApplication.translate("Form", u"Bot\u00f3n 04", None))
        
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QRect(210, 120, 351, 31))
        font = QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Aqu\u00ed aparecer\u00e1 el nombre del bot\u00f3n", None))
        
        # nuestro código

        self.btn_01.clicked.connect(self.textoBoton)
        self.btn_01.clicked.connect(lambda:self.cualBoton(self.btn_01))

        self.btn_ico.clicked.connect(self.textoBoton)
        self.btn_ico.clicked.connect(lambda:self.cualBoton(self.btn_ico))

        self.btn_03.clicked.connect(self.textoBoton)
        self.btn_03.clicked.connect(lambda:self.cualBoton(self.btn_03))
        
        self.btn_04.clicked.connect(self.textoBoton)
        self.btn_04.clicked.connect(lambda:self.cualBoton(self.btn_04))

    # setupUi

    def textoBoton(self):
        self.lineEdit.setText('Ha presionado el ')
        
    def cualBoton(self,b):
        self.lineEdit.setText(self.lineEdit.text() + b.text())
        if b == self.btn_03:
            if self.btn_04.isEnabled():
                self.btn_04.setEnabled(False)
            else:
                self.btn_04.setEnabled(True)
