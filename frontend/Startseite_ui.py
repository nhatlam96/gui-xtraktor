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
        Startseite.resize(1400, 900)
        Startseite.setMinimumSize(QtCore.QSize(1400, 900))
        Startseite.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2 = QtWidgets.QWidget(Startseite)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.main_frame = QtWidgets.QFrame(self.frame_2)
        self.main_frame.setStyleSheet("QFrame#main_frame {\n"
"    background-color: rgb(44, 62, 80);\n"
"}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.header_frame = QtWidgets.QFrame(self.main_frame)
        self.header_frame.setStyleSheet("QFrame#header_frame{\n"
"    background-color: rgb(44, 62, 80);\n"
"}")
        self.header_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.header_frame)
        self.frame.setStyleSheet("background-color: rgb(0, 191, 165);\n"
"border-radius: 5px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.home_Button = QtWidgets.QPushButton(self.frame)
        self.home_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_Button.setText("")
        self.home_Button.setIconSize(QtCore.QSize(45, 45))
        self.home_Button.setObjectName("home_Button")
        self.horizontalLayout_2.addWidget(self.home_Button)
        self.label34 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label34.setFont(font)
        self.label34.setObjectName("label34")
        self.horizontalLayout_2.addWidget(self.label34)
        self.horizontalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_16 = QtWidgets.QFrame(self.header_frame)
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_8.setContentsMargins(9, 0, 9, 0)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.sell_Button = QtWidgets.QPushButton(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sell_Button.sizePolicy().hasHeightForWidth())
        self.sell_Button.setSizePolicy(sizePolicy)
        self.sell_Button.setMinimumSize(QtCore.QSize(154, 0))
        self.sell_Button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sell_Button.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.sell_Button.setFont(font)
        self.sell_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sell_Button.setMouseTracking(True)
        self.sell_Button.setStyleSheet("QPushButton#sell_Button{\n"
"    background-color: orange;\n"
"    border-radius: 10px;\n"
"    height: 40px;\n"
"    width: 200px;\n"
"}\n"
"\n"
"QPushButton#sell_Button:hover {\n"
"    background-color: rgb(241, 196, 15);\n"
"    cursor: pointer;\n"
"    opacity: 0.8;\n"
"}\n"
"QPushButton#sell_Button:pressed {\n"
"    padding-left: 3px;\n"
"    padding-bottom: 3px;\n"
"}")
        self.sell_Button.setObjectName("sell_Button")
        self.verticalLayout_8.addWidget(self.sell_Button)
        self.horizontalLayout.addWidget(self.frame_16, 0, QtCore.Qt.AlignLeft)
        self.frame_3 = QtWidgets.QFrame(self.header_frame)
        self.frame_3.setStyleSheet("background-color: rgb(0, 191, 165);\n"
"border-radius: 5px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.budget_label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.budget_label.setFont(font)
        self.budget_label.setObjectName("budget_label")
        self.horizontalLayout_3.addWidget(self.budget_label)
        self.acc_Button = QtWidgets.QPushButton(self.frame_3)
        self.acc_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acc_Button.setText("")
        self.acc_Button.setIconSize(QtCore.QSize(45, 45))
        self.acc_Button.setObjectName("acc_Button")
        self.horizontalLayout_3.addWidget(self.acc_Button)
        self.shopping_Button = QtWidgets.QPushButton(self.frame_3)
        self.shopping_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shopping_Button.setText("")
        self.shopping_Button.setIconSize(QtCore.QSize(45, 45))
        self.shopping_Button.setObjectName("shopping_Button")
        self.horizontalLayout_3.addWidget(self.shopping_Button)
        self.horizontalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 5)
        self.verticalLayout_7.addWidget(self.header_frame, 0, QtCore.Qt.AlignTop)
        self.content_frame = QtWidgets.QFrame(self.main_frame)
        self.content_frame.setStyleSheet("QFrame#content_frame {\n"
"    background-color:rgb(44, 62, 80);\n"
"}")
        self.content_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.content_frame.setObjectName("content_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.content_frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_4 = QtWidgets.QFrame(self.content_frame)
        self.frame_4.setStyleSheet("QFrame#frame_4{\n"
"    background-color: rgb(44, 62, 80);\n"
"    border-radius: 10px;\n"
"    border: 4px solid rgb(127, 140, 141);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setStyleSheet("QFrame#frame_10 {\n"
"    background-color: rgb(52, 73, 94);\n"
"    border-radius: 15px;\n"
"    margin-bottom: 5px;\n"
"}")
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.hersteller_label = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.hersteller_label.setFont(font)
        self.hersteller_label.setStyleSheet("color: white;")
        self.hersteller_label.setObjectName("hersteller_label")
        self.horizontalLayout_6.addWidget(self.hersteller_label)
        self.comboBox_hersteller = QtWidgets.QComboBox(self.frame_10)
        self.comboBox_hersteller.setStyleSheet("height: 25px;\n"
"")
        self.comboBox_hersteller.setEditable(False)
        self.comboBox_hersteller.setObjectName("comboBox_hersteller")
        self.horizontalLayout_6.addWidget(self.comboBox_hersteller)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setStyleSheet("QFrame#frame_9 {\n"
"    background-color: rgb(52, 73, 94);\n"
"    border-radius: 15px;\n"
"    margin-bottom: 5px;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.typ_label = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.typ_label.setFont(font)
        self.typ_label.setStyleSheet("color: white;")
        self.typ_label.setObjectName("typ_label")
        self.horizontalLayout_9.addWidget(self.typ_label)
        self.typ_comboBox = QtWidgets.QComboBox(self.frame_9)
        self.typ_comboBox.setStyleSheet("height: 25px;\n"
"")
        self.typ_comboBox.setObjectName("typ_comboBox")
        self.horizontalLayout_9.addWidget(self.typ_comboBox)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.frame_13 = QtWidgets.QFrame(self.frame_4)
        self.frame_13.setStyleSheet("QFrame#frame_13 {\n"
"    background-color: rgb(52, 73, 94);\n"
"    border-radius: 15px;\n"
"    margin-bottom: 5px;\n"
"}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.baujahr_label = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.baujahr_label.setFont(font)
        self.baujahr_label.setStyleSheet("color: white;")
        self.baujahr_label.setObjectName("baujahr_label")
        self.horizontalLayout_10.addWidget(self.baujahr_label)
        self.baujahr_spinBox = QtWidgets.QSpinBox(self.frame_13)
        self.baujahr_spinBox.setStyleSheet("height: 25px;\n"
"")
        self.baujahr_spinBox.setMinimum(1900)
        self.baujahr_spinBox.setMaximum(2023)
        self.baujahr_spinBox.setSingleStep(10)
        self.baujahr_spinBox.setObjectName("baujahr_spinBox")
        self.horizontalLayout_10.addWidget(self.baujahr_spinBox)
        self.verticalLayout_5.addWidget(self.frame_13)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setStyleSheet("QFrame#frame_12 {\n"
"    background-color: rgb(52, 73, 94);\n"
"    border-radius: 15px;\n"
"    margin-bottom: 5px;\n"
"}")
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.leistung_label = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.leistung_label.setFont(font)
        self.leistung_label.setStyleSheet("color:white;")
        self.leistung_label.setObjectName("leistung_label")
        self.verticalLayout.addWidget(self.leistung_label)
        self.horizontalSlider_leistung = QtWidgets.QSlider(self.frame_12)
        self.horizontalSlider_leistung.setMaximum(700)
        self.horizontalSlider_leistung.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_leistung.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_leistung.setTickInterval(0)
        self.horizontalSlider_leistung.setObjectName("horizontalSlider_leistung")
        self.verticalLayout.addWidget(self.horizontalSlider_leistung)
        self.leistung_anzeigt = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.leistung_anzeigt.setFont(font)
        self.leistung_anzeigt.setStyleSheet("color: white;")
        self.leistung_anzeigt.setText("")
        self.leistung_anzeigt.setAlignment(QtCore.Qt.AlignCenter)
        self.leistung_anzeigt.setObjectName("leistung_anzeigt")
        self.verticalLayout.addWidget(self.leistung_anzeigt)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setStyleSheet("QFrame#frame_11 {\n"
"    background-color: rgb(52, 73, 94);\n"
"    border-radius: 15px;\n"
"    margin-bottom: 5px;\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.km_label = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.km_label.setFont(font)
        self.km_label.setStyleSheet("color: white;")
        self.km_label.setObjectName("km_label")
        self.verticalLayout_2.addWidget(self.km_label)
        self.horizontalSlider_km = QtWidgets.QSlider(self.frame_11)
        self.horizontalSlider_km.setMaximum(100)
        self.horizontalSlider_km.setSingleStep(5)
        self.horizontalSlider_km.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_km.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_km.setTickInterval(0)
        self.horizontalSlider_km.setObjectName("horizontalSlider_km")
        self.verticalLayout_2.addWidget(self.horizontalSlider_km)
        self.km_anzeigt = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.km_anzeigt.setFont(font)
        self.km_anzeigt.setStyleSheet("color: white;")
        self.km_anzeigt.setText("")
        self.km_anzeigt.setAlignment(QtCore.Qt.AlignCenter)
        self.km_anzeigt.setObjectName("km_anzeigt")
        self.verticalLayout_2.addWidget(self.km_anzeigt)
        self.verticalLayout_5.addWidget(self.frame_11)
        self.frame_15 = QtWidgets.QFrame(self.frame_4)
        self.frame_15.setStyleSheet("QFrame#frame_15 {\n"
"    background-color: rgb(52, 73, 94);\n"
"    border-radius: 15px;\n"
"    margin-bottom: 5px;\n"
"}")
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_15)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.frame_8 = QtWidgets.QFrame(self.frame_15)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.min_preis = QtWidgets.QSpinBox(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.min_preis.setFont(font)
        self.min_preis.setStyleSheet("height: 25px;\n"
"")
        self.min_preis.setMaximum(300000)
        self.min_preis.setSingleStep(10000)
        self.min_preis.setObjectName("min_preis")
        self.horizontalLayout_11.addWidget(self.min_preis)
        self.max_preis = QtWidgets.QSpinBox(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.max_preis.setFont(font)
        self.max_preis.setStyleSheet("height: 25px;\n"
"")
        self.max_preis.setMaximum(500000)
        self.max_preis.setSingleStep(10000)
        self.max_preis.setProperty("value", 500000)
        self.max_preis.setObjectName("max_preis")
        self.horizontalLayout_11.addWidget(self.max_preis)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.verticalLayout_5.addWidget(self.frame_15)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setStyleSheet("QFrame#frame_6 {\n"
"    background-color: rgb(52, 73, 94);\n"
"    border-radius: 15px;\n"
"    margin-bottom: 5px;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bufferleer_button = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bufferleer_button.setFont(font)
        self.bufferleer_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bufferleer_button.setStyleSheet("QPushButton#bufferleer_button {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 61, 0);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    min-height: 30px;\n"
"}\n"
"QPushButton#bufferleer_button:hover {\n"
"    background-color: rgb(255, 110, 64);\n"
"    opacity: 0.8;\n"
"}\n"
"QPushButton#bufferleer_button:pressed {\n"
"    padding-left: 3px;\n"
"    padding-bottom: 3px;\n"
"}")
        self.bufferleer_button.setObjectName("bufferleer_button")
        self.horizontalLayout_4.addWidget(self.bufferleer_button)
        self.such_infor_commit = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.such_infor_commit.setFont(font)
        self.such_infor_commit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.such_infor_commit.setStyleSheet("QPushButton#such_infor_commit {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(0, 153, 255);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    min-height: 30px;\n"
"}\n"
"QPushButton#such_infor_commit:hover {\n"
"    background-color: rgb(26, 183, 234);\n"
"    opacity: 0.8;\n"
"}\n"
"QPushButton#such_infor_commit:pressed {\n"
"    padding-left: 3px;\n"
"    padding-bottom: 3px;\n"
"}")
        self.such_infor_commit.setObjectName("such_infor_commit")
        self.horizontalLayout_4.addWidget(self.such_infor_commit)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.horizontalLayout_8.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.content_frame)
        self.frame_5.setStyleSheet("QFrame#frame_5{\n"
"    background-color: rgb(44, 62, 80);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setStyleSheet("QFrame#frame_7 {\n"
"    background-color: rgb(52, 73, 94);\n"
"    min-height: 60px;\n"
"    border-radius: 15px;\n"
"    border: 4px solid rgb(127, 140, 141);\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.searchbar_Lineedit = QtWidgets.QLineEdit(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.searchbar_Lineedit.setFont(font)
        self.searchbar_Lineedit.setStyleSheet("QLineEdit#searchbar_Lineedit{\n"
"    border-bottom: 2px solid rgb(158, 158, 158);\n"
"    min-height: 30px;\n"
"    color: rgb(97, 97, 97);\n"
"}")
        self.searchbar_Lineedit.setFrame(False)
        self.searchbar_Lineedit.setObjectName("searchbar_Lineedit")
        self.horizontalLayout_5.addWidget(self.searchbar_Lineedit)
        self.search_pushButton = QtWidgets.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.search_pushButton.setFont(font)
        self.search_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_pushButton.setStyleSheet("QPushButton#search_pushButton{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(100, 221, 23);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    min-height: 30px;\n"
"}\n"
"QPushButton#search_pushButton:hover {\n"
"    background-color: rgb(178, 255, 89);\n"
"    opacity: 0.8;\n"
"}\n"
"QPushButton#search_pushButton:pressed {\n"
"    padding-left: 3px;\n"
"    padding-bottom: 3px;\n"
"}")
        self.search_pushButton.setObjectName("search_pushButton")
        self.horizontalLayout_5.addWidget(self.search_pushButton)
        self.sort_comboBox = QtWidgets.QComboBox(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.sort_comboBox.setFont(font)
        self.sort_comboBox.setStyleSheet("height: 25px;\n"
"")
        self.sort_comboBox.setEditable(False)
        self.sort_comboBox.setCurrentText("")
        self.sort_comboBox.setObjectName("sort_comboBox")
        self.horizontalLayout_5.addWidget(self.sort_comboBox)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 2)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_5)
        self.scrollArea.setStyleSheet("background-color: rgb(52, 73, 94);\n"
"")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 970, 690))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.horizontalLayout_8.addWidget(self.frame_5)
        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 6)
        self.verticalLayout_7.addWidget(self.content_frame)
        self.horizontalLayout_7.addWidget(self.main_frame)
        Startseite.setCentralWidget(self.frame_2)

        self.retranslateUi(Startseite)
        QtCore.QMetaObject.connectSlotsByName(Startseite)

    def retranslateUi(self, Startseite):
        _translate = QtCore.QCoreApplication.translate
        Startseite.setWindowTitle(_translate("Startseite", "Startseite"))
        self.label34.setText(_translate("Startseite", "WEBSHOP.DE"))
        self.sell_Button.setText(_translate("Startseite", "Verkaufen"))
        self.label_2.setText(_translate("Startseite", "Budget:"))
        self.budget_label.setText(_translate("Startseite", "TextLabel"))
        self.hersteller_label.setText(_translate("Startseite", "Hersteller"))
        self.typ_label.setText(_translate("Startseite", "Typ"))
        self.baujahr_label.setText(_translate("Startseite", "Baujahr"))
        self.leistung_label.setText(_translate("Startseite", "Leistung - PS"))
        self.km_label.setText(_translate("Startseite", "Km/h"))
        self.label_3.setText(_translate("Startseite", "Preis"))
        self.min_preis.setSuffix(_translate("Startseite", " €"))
        self.min_preis.setPrefix(_translate("Startseite", "min. "))
        self.max_preis.setSuffix(_translate("Startseite", " €"))
        self.max_preis.setPrefix(_translate("Startseite", "max. "))
        self.bufferleer_button.setText(_translate("Startseite", "zurücksetzen"))
        self.such_infor_commit.setText(_translate("Startseite", "bestätigen"))
        self.searchbar_Lineedit.setPlaceholderText(_translate("Startseite", "was suchen Sie?"))
        self.search_pushButton.setText(_translate("Startseite", "suchen"))
        self.sort_comboBox.setPlaceholderText(_translate("Startseite", "sortieren"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Startseite = QtWidgets.QMainWindow()
    ui = Ui_Startseite()
    ui.setupUi(Startseite)
    Startseite.show()
    sys.exit(app.exec_())
