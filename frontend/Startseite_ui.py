# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Startseite.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Startseite(object):
    def setupUi(self, Startseite):
        Startseite.setObjectName("Startseite")
        Startseite.resize(972, 860)
        Startseite.setMinimumSize(QtCore.QSize(880, 860))
        Startseite.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2 = QtWidgets.QWidget(Startseite)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.main_frame = QtWidgets.QFrame(self.frame_2)
        self.main_frame.setStyleSheet("background-color: rgb(52, 73, 94);")
        self.main_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.header_frame = QtWidgets.QFrame(self.main_frame)
        self.header_frame.setStyleSheet("background-color: rgb(52, 73, 94);")
        self.header_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.header_frame)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-size: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.home_Button = QtWidgets.QPushButton(self.frame)
        self.home_Button.setText("")
        self.home_Button.setObjectName("home_Button")
        self.horizontalLayout_2.addWidget(self.home_Button)
        self.label34 = QtWidgets.QLabel(self.frame)
        self.label34.setObjectName("label34")
        self.horizontalLayout_2.addWidget(self.label34)
        self.horizontalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.header_frame)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-size: 20px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.budget_label = QtWidgets.QLabel(self.frame_3)
        self.budget_label.setObjectName("budget_label")
        self.horizontalLayout_3.addWidget(self.budget_label)
        self.acc_Button = QtWidgets.QPushButton(self.frame_3)
        self.acc_Button.setText("")
        self.acc_Button.setObjectName("acc_Button")
        self.horizontalLayout_3.addWidget(self.acc_Button)
        self.shopping_Button = QtWidgets.QPushButton(self.frame_3)
        self.shopping_Button.setText("")
        self.shopping_Button.setObjectName("shopping_Button")
        self.horizontalLayout_3.addWidget(self.shopping_Button)
        self.horizontalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.header_frame, 0, QtCore.Qt.AlignTop)
        self.content_frame = QtWidgets.QFrame(self.main_frame)
        self.content_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.content_frame.setObjectName("content_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.content_frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_4 = QtWidgets.QFrame(self.content_frame)
        self.frame_4.setStyleSheet("QFrame#frame_4 {\n"
"    padding: 15px;\n"
"    background-color: rgb(52, 73, 94);\n"
"    border: 2px solid rgb(41, 128, 185);\n"
"    border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setStyleSheet("QFrame#frame_10{\n"
"    background-color: rgb(44, 62, 80);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.hersteller_label = QtWidgets.QLabel(self.frame_10)
        self.hersteller_label.setStyleSheet("QLabel#hersteller_label {\n"
"    background-color: none;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}")
        self.hersteller_label.setObjectName("hersteller_label")
        self.horizontalLayout_6.addWidget(self.hersteller_label)
        self.comboBox_hersteller = QtWidgets.QComboBox(self.frame_10)
        self.comboBox_hersteller.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"\n"
"")
        self.comboBox_hersteller.setEditable(False)
        self.comboBox_hersteller.setObjectName("comboBox_hersteller")
        self.horizontalLayout_6.addWidget(self.comboBox_hersteller)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setStyleSheet("QFrame#frame_9{\n"
"    background-color: rgb(44, 62, 80);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.typ_label = QtWidgets.QLabel(self.frame_9)
        self.typ_label.setStyleSheet("QLabel#typ_label {\n"
"    background-color: none;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}")
        self.typ_label.setObjectName("typ_label")
        self.verticalLayout_6.addWidget(self.typ_label)
        self.typ_comboBox = QtWidgets.QComboBox(self.frame_9)
        self.typ_comboBox.setStyleSheet("color: black;\n"
"background-color: white;")
        self.typ_comboBox.setObjectName("typ_comboBox")
        self.verticalLayout_6.addWidget(self.typ_comboBox)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.frame_14 = QtWidgets.QFrame(self.frame_4)
        self.frame_14.setStyleSheet("QFrame#frame_14{\n"
"    background-color: rgb(44, 62, 80);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.zustand_label = QtWidgets.QLabel(self.frame_14)
        self.zustand_label.setStyleSheet("QLabel#zustand_label {\n"
"    background-color: none;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}")
        self.zustand_label.setObjectName("zustand_label")
        self.horizontalLayout_9.addWidget(self.zustand_label)
        self.comboBox_zustand = QtWidgets.QComboBox(self.frame_14)
        self.comboBox_zustand.setStyleSheet("color: black;\n"
"background-color: white;")
        self.comboBox_zustand.setObjectName("comboBox_zustand")
        self.comboBox_zustand.addItem("")
        self.comboBox_zustand.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_zustand)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.frame_4)
        self.frame_13.setStyleSheet("QFrame#frame_13{\n"
"    background-color: rgb(44, 62, 80);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.baujahr_label = QtWidgets.QLabel(self.frame_13)
        self.baujahr_label.setStyleSheet("QLabel#baujahr_label {\n"
"    background-color: none;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}")
        self.baujahr_label.setObjectName("baujahr_label")
        self.horizontalLayout_10.addWidget(self.baujahr_label)
        self.baujahr_spinBox = QtWidgets.QSpinBox(self.frame_13)
        self.baujahr_spinBox.setStyleSheet("color: black;\n"
"background-color: white;")
        self.baujahr_spinBox.setMinimum(1860)
        self.baujahr_spinBox.setMaximum(2023)
        self.baujahr_spinBox.setObjectName("baujahr_spinBox")
        self.horizontalLayout_10.addWidget(self.baujahr_spinBox)
        self.verticalLayout_5.addWidget(self.frame_13)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setStyleSheet("QFrame#frame_12{\n"
"    background-color: rgb(44, 62, 80);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}")
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.leistung_label = QtWidgets.QLabel(self.frame_12)
        self.leistung_label.setStyleSheet("QLabel#leistung_label {\n"
"    background-color: none;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}")
        self.leistung_label.setObjectName("leistung_label")
        self.verticalLayout.addWidget(self.leistung_label)
        self.horizontalSlider_leistung = QtWidgets.QSlider(self.frame_12)
        self.horizontalSlider_leistung.setStyleSheet("QSlider#horizontalSlider_leistung {\n"
"    background-color: none;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}")
        self.horizontalSlider_leistung.setMaximum(860)
        self.horizontalSlider_leistung.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_leistung.setObjectName("horizontalSlider_leistung")
        self.verticalLayout.addWidget(self.horizontalSlider_leistung)
        self.leistung_anzeigt = QtWidgets.QLabel(self.frame_12)
        self.leistung_anzeigt.setStyleSheet("QLabel#leistung_anzeigt {\n"
"    background-color: none;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}")
        self.leistung_anzeigt.setText("")
        self.leistung_anzeigt.setAlignment(QtCore.Qt.AlignCenter)
        self.leistung_anzeigt.setObjectName("leistung_anzeigt")
        self.verticalLayout.addWidget(self.leistung_anzeigt)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setStyleSheet("QFrame#frame_11{\n"
"    background-color: rgb(44, 62, 80);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.km_label = QtWidgets.QLabel(self.frame_11)
        self.km_label.setStyleSheet("QLabel#km_label {\n"
"    background-color: none;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}")
        self.km_label.setObjectName("km_label")
        self.verticalLayout_2.addWidget(self.km_label)
        self.horizontalSlider_km = QtWidgets.QSlider(self.frame_11)
        self.horizontalSlider_km.setStyleSheet("QSlider#horizontalSlider_km {\n"
"    background-color: none;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}")
        self.horizontalSlider_km.setMaximum(100)
        self.horizontalSlider_km.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_km.setObjectName("horizontalSlider_km")
        self.verticalLayout_2.addWidget(self.horizontalSlider_km)
        self.km_anzeigt = QtWidgets.QLabel(self.frame_11)
        self.km_anzeigt.setStyleSheet("QLabel#km_anzeigt {\n"
"    background-color: none;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}")
        self.km_anzeigt.setText("")
        self.km_anzeigt.setAlignment(QtCore.Qt.AlignCenter)
        self.km_anzeigt.setObjectName("km_anzeigt")
        self.verticalLayout_2.addWidget(self.km_anzeigt)
        self.verticalLayout_5.addWidget(self.frame_11)
        self.frame_15 = QtWidgets.QFrame(self.frame_4)
        self.frame_15.setStyleSheet("QFrame#frame_15{\n"
"    background-color: rgb(44, 62, 80);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}")
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_15)
        self.label_3.setStyleSheet("QLabel#label_3 {\n"
"    background-color: none;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.frame_8 = QtWidgets.QFrame(self.frame_15)
        self.frame_8.setStyleSheet("QFrame#frame_8{\n"
"    background-color: rgb(44, 62, 80);\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.min_preis = QtWidgets.QComboBox(self.frame_8)
        self.min_preis.setStyleSheet("color: black;\n"
"background-color: white;")
        self.min_preis.setObjectName("min_preis")
        self.horizontalLayout_11.addWidget(self.min_preis)
        self.max_preis = QtWidgets.QComboBox(self.frame_8)
        self.max_preis.setStyleSheet("color: black;\n"
"background-color: white;")
        self.max_preis.setObjectName("max_preis")
        self.horizontalLayout_11.addWidget(self.max_preis)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.verticalLayout_5.addWidget(self.frame_15)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setStyleSheet("QFrame#frame_6{\n"
"    background-color: rgb(44, 62, 80);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bufferleer_button = QtWidgets.QPushButton(self.frame_6)
        self.bufferleer_button.setStyleSheet("QPushButton#bufferleer_button{\n"
"    border-radius: 15px;\n"
"    background-color: green;\n"
"    height: 35px;\n"
"    width: 100px;\n"
"    font-size: 16px;\n"
"    color: white;\n"
"}\n"
"QPushButton#bufferleer_button:hover {\n"
"    cursor: pointer;\n"
"    opacity: 0.7;\n"
"    background-color: rgb(39, 174, 96);\n"
"}\n"
"QPushButton#bufferleer_button:pressed {\n"
"    padding-left: 4px;\n"
"    padding-top: 4px;\n"
"}\n"
"")
        self.bufferleer_button.setObjectName("bufferleer_button")
        self.horizontalLayout_4.addWidget(self.bufferleer_button)
        self.such_infor_commit = QtWidgets.QPushButton(self.frame_6)
        self.such_infor_commit.setStyleSheet("QPushButton#such_infor_commit{\n"
"    border-radius: 15px;\n"
"    background-color: green;\n"
"    height: 35px;\n"
"    width: 100px;\n"
"    font-size: 16px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#such_infor_commit:hover {\n"
"    cursor: pointer;\n"
"    opacity: 0.7;\n"
"    background-color: rgb(39, 174, 96);\n"
"}\n"
"QPushButton#such_infor_commit:pressed {\n"
"    padding-left: 4px;\n"
"    padding-top: 4px;\n"
"}")
        self.such_infor_commit.setObjectName("such_infor_commit")
        self.horizontalLayout_4.addWidget(self.such_infor_commit)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.horizontalLayout_8.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.content_frame)
        self.frame_5.setStyleSheet("background-color: rgb(52, 73, 94);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Lineedit_suchfeld = QtWidgets.QLineEdit(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setItalic(True)
        self.Lineedit_suchfeld.setFont(font)
        self.Lineedit_suchfeld.setStyleSheet("QLineEdit#Lineedit_suchfeld {\n"
"    background-color: white;\n"
"    line-height: 2.5;\n"
"    height: 35px;\n"
"    font-size: 25px;\n"
"    border-bottom: 3px solid green;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"}")
        self.Lineedit_suchfeld.setFrame(False)
        self.Lineedit_suchfeld.setObjectName("Lineedit_suchfeld")
        self.horizontalLayout_5.addWidget(self.Lineedit_suchfeld)
        self.pushButton_suchen = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_suchen.setStyleSheet("QPushButton#pushButton_suchen {\n"
"    height: 35px;\n"
"    width: 100px;\n"
"    background-color: green;\n"
"    border-radius: 10px;\n"
"    font-size: 16px;\n"
"    color: white;\n"
"}\n"
"QPushButton#pushButton_suchen:hover {\n"
"    cursor: pointer;\n"
"    opacity: 0.7;\n"
"    background-color: rgb(39, 174, 96);\n"
"}\n"
"\n"
"QPushButton#pushButton_suchen:pressed {\n"
"    padding-left: 4px;\n"
"    padding-bottom: 4px;\n"
"}")
        self.pushButton_suchen.setObjectName("pushButton_suchen")
        self.horizontalLayout_5.addWidget(self.pushButton_suchen)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_5)
        self.scrollArea.setStyleSheet("QScrollArea#scrollArea{\n"
"    background-color: white;\n"
"    margin-top: 15px;\n"
"    color: white;\n"
"}\n"
"")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 567, 613))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.horizontalLayout_8.addWidget(self.frame_5)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 3)
        self.verticalLayout_7.addWidget(self.content_frame)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 11)
        self.horizontalLayout_7.addWidget(self.main_frame)
        Startseite.setCentralWidget(self.frame_2)

        self.retranslateUi(Startseite)
        QtCore.QMetaObject.connectSlotsByName(Startseite)

    def retranslateUi(self, Startseite):
        _translate = QtCore.QCoreApplication.translate
        Startseite.setWindowTitle(_translate("Startseite", "MainWindow"))
        self.label34.setText(_translate("Startseite", "WEBSHOP.DE"))
        self.budget_label.setText(_translate("Startseite", "TextLabel"))
        self.hersteller_label.setText(_translate("Startseite", "Hersteller"))
        self.typ_label.setText(_translate("Startseite", "Typ"))
        self.zustand_label.setText(_translate("Startseite", "Zustand"))
        self.comboBox_zustand.setItemText(0, _translate("Startseite", "Neu"))
        self.comboBox_zustand.setItemText(1, _translate("Startseite", "Gebraucht"))
        self.baujahr_label.setText(_translate("Startseite", "Baujahr"))
        self.leistung_label.setText(_translate("Startseite", "Leistung"))
        self.km_label.setText(_translate("Startseite", "Km/h"))
        self.label_3.setText(_translate("Startseite", "Preis"))
        self.min_preis.setPlaceholderText(_translate("Startseite", "von..."))
        self.max_preis.setPlaceholderText(_translate("Startseite", "bis..."))
        self.bufferleer_button.setText(_translate("Startseite", "zurücksetzen"))
        self.such_infor_commit.setText(_translate("Startseite", "bestätigen"))
        self.Lineedit_suchfeld.setPlaceholderText(_translate("Startseite", "was suchen Sie?"))
        self.pushButton_suchen.setText(_translate("Startseite", "suchen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Startseite = QtWidgets.QMainWindow()
    ui = Ui_Startseite()
    ui.setupUi(Startseite)
    Startseite.show()
    sys.exit(app.exec_())
