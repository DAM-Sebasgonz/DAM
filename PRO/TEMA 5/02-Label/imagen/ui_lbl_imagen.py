# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lbl_imagen.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(544, 356)
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Etiqueta imagen", None))
        
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 60, 320, 210))
        self.label.setText("")

        # código para caargar la imagen

        self.pixmap = QPixmap('02-Label/imagen/Logo.png')
        if not self.pixmap.isNull():
            # Escalar manteniendo el aspect ratio
            pixmap_escalado = self.pixmap.scaled(
                200, 100,  # ancho, alto
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation)
            self.label.setPixmap(pixmap_escalado)
        else:
            self.label.setText("No se pudo cargar la imagen")
            self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    # setupUi


