# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'label.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_formEtiqueta(object):
    def setupUi(self, formEtiqueta):
        if not formEtiqueta.objectName():
            formEtiqueta.setObjectName(u"formEtiqueta")
        formEtiqueta.resize(400, 300)
        formEtiqueta.setWindowTitle(QCoreApplication.translate("formEtiqueta", u"Form", None))

        self.lbl01 = QLabel(formEtiqueta)
        self.lbl01.setObjectName(u"lbl01")
        self.lbl01.setGeometry(QRect(50, 20, 131, 20))
        self.lbl01.setMargin(0)
        self.lbl01.setText(QCoreApplication.translate("formEtiqueta", u"uno", None))
        
        font = QFont()
        font.setPointSize(17)
        self.lbl02 = QLabel(formEtiqueta)
        self.lbl02.setObjectName(u"lbl02")
        self.lbl02.setGeometry(QRect(50, 50, 131, 16))
        self.lbl02.setFont(font)
        self.lbl02.setText(QCoreApplication.translate("formEtiqueta", u"dos", None))
        
        self.lbl03 = QLabel(formEtiqueta)
        self.lbl03.setObjectName(u"lbl03")
        self.lbl03.setGeometry(QRect(50, 80, 131, 16))
        self.lbl03.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.lbl03.setText(QCoreApplication.translate("formEtiqueta", u"tres", None))
        
        self.lbl04 = QLabel(formEtiqueta)
        self.lbl04.setObjectName(u"lbl04")
        self.lbl04.setGeometry(QRect(50, 110, 141, 31))
        self.lbl04.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl04.setText(QCoreApplication.translate("formEtiqueta", u"cuatro", None))
        
        self.lbl05 = QLabel(formEtiqueta)
        self.lbl05.setObjectName(u"lbl05")
        self.lbl05.setGeometry(QRect(50, 150, 131, 16))
        self.lbl05.setStyleSheet(u"color:red")
        self.lbl05.setText(QCoreApplication.translate("formEtiqueta", u"cinco", None))
        
        self.lbl06 = QLabel(formEtiqueta)
        self.lbl06.setObjectName(u"lbl06")
        self.lbl06.setEnabled(False)
        self.lbl06.setGeometry(QRect(50, 180, 131, 16))
        self.lbl06.setText(QCoreApplication.translate("formEtiqueta", u"seis", None))
       
        self.lbl07 = QLabel(formEtiqueta)
        self.lbl07.setObjectName(u"lbl07")
        self.lbl07.setGeometry(QRect(260, 210, 91, 16))
        self.lbl07.setText(QCoreApplication.translate("formEtiqueta", u"siete", None))
         
        self.lbl08 = QLabel(formEtiqueta)
        self.lbl08.setObjectName(u"lb08")
        self.lbl08.setGeometry(QRect(50, 250, 131, 16))
        self.lbl08.setText(QCoreApplication.translate("formEtiqueta", u"ocho", None))

# el código agregado

        self.lbl07.setVisible(False)
        self.lbl08.setText(self.lbl07.text())

    # setupUi
