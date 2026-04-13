# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prueba_MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # información sobre la ventana
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)

        # contenedor de los controles

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        # label
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 151, 31))
        # combobox
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(160, 30, 171, 41))
        # radiobutton_1
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(90, 140, 100, 20))

        # radiobutton_2
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(90, 190, 100, 20))
        # checkBox_1
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(350, 120, 87, 20))
        # checkBox_2
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(350, 170, 87, 20))
        # pushButton_1
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 320, 113, 32))
        # pushButton_2
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 320, 113, 32))
        # pushButton_3
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(380, 320, 113, 32))
        # lineEdit
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(450, 30, 113, 21))
        # textEdit
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(480, 110, 104, 79))
        
        # centrar el contenedor en la ventana
        MainWindow.setCentralWidget(self.centralwidget)

        # barra de menú
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 24))
        MainWindow.setMenuBar(self.menubar)

        # barra de estado
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        # a partir de aquí hacer los cambios a los controles

        self.radioButton.setText('Masculino')

        # indica la forma como se conectan las señales con los controles

        QMetaObject.connectSlotsByName(MainWindow)
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

