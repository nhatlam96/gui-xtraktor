# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/nhatlamluong/Projects/hs_wo_gui_2023/Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(513, 213)
        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setObjectName("centralwidget")
        self.usernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLineEdit.setGeometry(QtCore.QRect(50, 60, 231, 31))
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setGeometry(QtCore.QRect(50, 100, 231, 31))
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.loginAsComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.loginAsComboBox.setGeometry(QtCore.QRect(50, 20, 231, 31))
        self.loginAsComboBox.setObjectName("loginAsComboBox")
        self.loginAsComboBox.addItem("")
        self.loginAsComboBox.addItem("")
        self.loginAsComboBox.addItem("")
        self.loginAsComboBox.addItem("")
        self.loginAsComboBox.addItem("")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(300, 20, 151, 61))
        self.loginButton.setObjectName("loginButton")
        self.goToRegisterButton = QtWidgets.QPushButton(self.centralwidget)
        self.goToRegisterButton.setGeometry(QtCore.QRect(300, 110, 181, 25))
        self.goToRegisterButton.setFlat(True)
        self.goToRegisterButton.setObjectName("goToRegisterButton")
        Register.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Register)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Register.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Register)
        self.statusbar.setObjectName("statusbar")
        Register.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(Register)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Register)
        self.loginAsComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Login"))
        self.usernameLineEdit.setPlaceholderText(_translate("Register", "Username"))
        self.passwordLineEdit.setPlaceholderText(_translate("Register", "Password"))
        self.loginAsComboBox.setCurrentText(_translate("Register", "Please select profile..."))
        self.loginAsComboBox.setItemText(0, _translate("Register", "Please select profile..."))
        self.loginAsComboBox.setItemText(1, _translate("Register", "Käufer (Neuware)"))
        self.loginAsComboBox.setItemText(2, _translate("Register", "Verkäufer (Neuware)"))
        self.loginAsComboBox.setItemText(3, _translate("Register", "Käufer (Gebraucht)"))
        self.loginAsComboBox.setItemText(4, _translate("Register", "Verkäufer (Gebraucht)"))
        self.loginButton.setText(_translate("Register", "Login"))
        self.goToRegisterButton.setText(_translate("Register", "No Account? Register here!"))
        self.menuFile.setTitle(_translate("Register", "File"))
        self.actionClose.setText(_translate("Register", "Close"))
