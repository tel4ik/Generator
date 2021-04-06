from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from View.Mainwindow import Ui_MainWindow
from Conroller.MainController import Controller


class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.myclose = True
        self.Controller = Controller()

        self.ui.checkBox_4.setText('ABCDEFG...')
        self.ui.checkBox_5.setText('1234...')
        self.ui.checkBox_11.setText('!@#$%^...')
        self.ui.length_pas.setText(str(1))

        self.ui.Slider_length.setMinimum(1)
        self.ui.Slider_length.setMaximum(25)
        # self.ui.Slider_length.setSingleStep(1)
        self.ui.Slider_length.setTickInterval(1)
        self.ui.Slider_length.valueChanged.connect(self.output_length)

        self.ui.Btn_run.clicked.connect(self.password_generate)

        self.show()

    def password_generate(self):
        struct = []
        if self.ui.checkBox_4.isChecked():
            struct.append(1)
        if self.ui.checkBox_5.isChecked():
            struct.append(0)
        if self.ui.checkBox_11.isChecked():
            struct.append(2)
        length = int(self.ui.length_pas.text())
        self.ui.View_pasword.setText(str(self.Controller.create_pas(length=length, struct=struct)))

    def output_length(self):
        length = self.ui.Slider_length.value()
        self.ui.length_pas.setText(str(length))
