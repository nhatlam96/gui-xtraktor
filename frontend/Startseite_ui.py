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
        Startseite.resize(888, 668)
        self.frame_2 = QtWidgets.QWidget(Startseite)
        self.frame_2.setObjectName("frame_2")
        self.main_frame = QtWidgets.QFrame(self.frame_2)
        self.main_frame.setGeometry(QtCore.QRect(9, 9, 841, 631))
        self.main_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_frame.setObjectName("main_frame")
        self.header_frame = QtWidgets.QFrame(self.main_frame)
        self.header_frame.setGeometry(QtCore.QRect(10, 10, 821, 111))
        self.header_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.header_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.header_frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.horizontalLayout.addWidget(self.frame_3)
        self.content_frame = QtWidgets.QFrame(self.main_frame)
        self.content_frame.setGeometry(QtCore.QRect(10, 141, 821, 471))
        self.content_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.content_frame.setObjectName("content_frame")
        self.frame_4 = QtWidgets.QFrame(self.content_frame)
        self.frame_4.setGeometry(QtCore.QRect(10, 10, 241, 456))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.hersteller_label = QtWidgets.QLabel(self.frame_10)
        self.hersteller_label.setObjectName("hersteller_label")
        self.horizontalLayout_6.addWidget(self.hersteller_label)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_10)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_6.addWidget(self.comboBox_2)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.typ_label = QtWidgets.QLabel(self.frame_9)
        self.typ_label.setObjectName("typ_label")
        self.verticalLayout_6.addWidget(self.typ_label)
        self.typ_comboBox = QtWidgets.QComboBox(self.frame_9)
        self.typ_comboBox.setObjectName("typ_comboBox")
        self.verticalLayout_6.addWidget(self.typ_comboBox)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.frame_14 = QtWidgets.QFrame(self.frame_4)
        self.frame_14.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.zustand_label = QtWidgets.QLabel(self.frame_14)
        self.zustand_label.setObjectName("zustand_label")
        self.horizontalLayout_9.addWidget(self.zustand_label)
        self.comboBox = QtWidgets.QComboBox(self.frame_14)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_9.addWidget(self.comboBox)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.frame_4)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.baujahr_label = QtWidgets.QLabel(self.frame_13)
        self.baujahr_label.setObjectName("baujahr_label")
        self.horizontalLayout_10.addWidget(self.baujahr_label)
        self.baujahr_spinBox = QtWidgets.QSpinBox(self.frame_13)
        self.baujahr_spinBox.setObjectName("baujahr_spinBox")
        self.horizontalLayout_10.addWidget(self.baujahr_spinBox)
        self.verticalLayout_5.addWidget(self.frame_13)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.leistung_label = QtWidgets.QLabel(self.frame_12)
        self.leistung_label.setObjectName("leistung_label")
        self.horizontalLayout_11.addWidget(self.leistung_label)
        self.horizontalSlider = QtWidgets.QSlider(self.frame_12)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_11.addWidget(self.horizontalSlider)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.km_label = QtWidgets.QLabel(self.frame_11)
        self.km_label.setObjectName("km_label")
        self.horizontalLayout_7.addWidget(self.km_label)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.frame_11)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalLayout_7.addWidget(self.horizontalSlider_3)
        self.verticalLayout_5.addWidget(self.frame_11)
        self.frame_15 = QtWidgets.QFrame(self.frame_4)
        self.frame_15.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.frame_15)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame_15)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_8.addWidget(self.horizontalSlider_2)
        self.verticalLayout_5.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_4)
        self.frame_16.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_4 = QtWidgets.QLabel(self.frame_16)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_12.addWidget(self.label_4)
        self.auf_lager_spinBox = QtWidgets.QSpinBox(self.frame_16)
        self.auf_lager_spinBox.setObjectName("auf_lager_spinBox")
        self.horizontalLayout_12.addWidget(self.auf_lager_spinBox)
        self.verticalLayout_5.addWidget(self.frame_16)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bufferleer_button = QtWidgets.QPushButton(self.frame_6)
        self.bufferleer_button.setObjectName("bufferleer_button")
        self.horizontalLayout_4.addWidget(self.bufferleer_button)
        self.such_infor_commit = QtWidgets.QPushButton(self.frame_6)
        self.such_infor_commit.setObjectName("such_infor_commit")
        self.horizontalLayout_4.addWidget(self.such_infor_commit)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.content_frame)
        self.frame_5.setGeometry(QtCore.QRect(270, 20, 541, 431))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setGeometry(QtCore.QRect(10, 10, 511, 44))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setGeometry(QtCore.QRect(10, 70, 511, 341))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setObjectName("frame_8")
        Startseite.setCentralWidget(self.frame_2)

        self.retranslateUi(Startseite)
        QtCore.QMetaObject.connectSlotsByName(Startseite)

    def retranslateUi(self, Startseite):
        _translate = QtCore.QCoreApplication.translate
        Startseite.setWindowTitle(_translate("Startseite", "MainWindow"))
        self.pushButton.setText(_translate("Startseite", "PushButton"))
        self.label.setText(_translate("Startseite", "TextLabel"))
        self.label_2.setText(_translate("Startseite", "TextLabel"))
        self.pushButton_2.setText(_translate("Startseite", "PushButton"))
        self.pushButton_3.setText(_translate("Startseite", "PushButton"))
        self.hersteller_label.setText(_translate("Startseite", "Hersteller"))
        self.typ_label.setText(_translate("Startseite", "Typ"))
        self.zustand_label.setText(_translate("Startseite", "Zustand"))
        self.baujahr_label.setText(_translate("Startseite", "Baujahr"))
        self.leistung_label.setText(_translate("Startseite", "Leistung"))
        self.km_label.setText(_translate("Startseite", "Km/h"))
        self.label_3.setText(_translate("Startseite", "Preis"))
        self.label_4.setText(_translate("Startseite", "Auf Lager"))
        self.bufferleer_button.setText(_translate("Startseite", "zurücksetzen"))
        self.such_infor_commit.setText(_translate("Startseite", "bestätigen"))
        self.pushButton_4.setText(_translate("Startseite", "PushButton"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Startseite = QtWidgets.QMainWindow()
    ui = Ui_Startseite()
    ui.setupUi(Startseite)
    Startseite.show()
    sys.exit(app.exec_())
