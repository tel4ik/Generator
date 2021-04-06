# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerWPJxAm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(700, 500))
        font = QFont()
        font.setPointSize(5)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(600, 400))
        font1 = QFont()
        font1.setPointSize(10)
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Btn_run = QPushButton(self.frame)
        self.Btn_run.setObjectName(u"Btn_run")
        self.Btn_run.setGeometry(QRect(190, 330, 201, 28))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(11)
        self.Btn_run.setFont(font2)
        self.Btn_run.setStyleSheet(u"QPushButton{\n"
"	border: 0;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 85, 255);\n"
"}")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(220, 150, 129, 172))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_13 = QCheckBox(self.frame_2)
        self.checkBox_13.setObjectName(u"checkBox_13")
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(10)
        self.checkBox_13.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox_13)

        self.checkBox_12 = QCheckBox(self.frame_2)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox_12)

        self.checkBox_11 = QCheckBox(self.frame_2)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox_11)

        self.checkBox_5 = QCheckBox(self.frame_2)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox_5)

        self.checkBox_4 = QCheckBox(self.frame_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font3)

        self.verticalLayout.addWidget(self.checkBox_4)

        self.View_pasword = QTextEdit(self.frame)
        self.View_pasword.setObjectName(u"View_pasword")
        self.View_pasword.setGeometry(QRect(90, 70, 451, 31))
        self.View_pasword.setFont(font3)
        self.View_pasword.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.View_pasword.setReadOnly(True)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(170, 100, 251, 46))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Slider_length = QSlider(self.frame_3)
        self.Slider_length.setObjectName(u"Slider_length")
        self.Slider_length.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.Slider_length)

        self.length_pas = QLabel(self.frame_3)
        self.length_pas.setObjectName(u"length_pas")

        self.horizontalLayout_2.addWidget(self.length_pas)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
        self.Btn_run.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.length_pas.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

