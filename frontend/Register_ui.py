# Form implementation generated from reading ui file 'c:\Users\julia\Documents\HS Worms\Fächer\GUI\hs_wo_gui_2023\frontend\Register.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(540, 200)
        Register.setMinimumSize(QtCore.QSize(520, 200))
        Register.setMaximumSize(QtCore.QSize(540, 220))
        self.centralwidget = QtWidgets.QWidget(parent=Register)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setStyleSheet("QFrame#frame_3{\n"
"    background-color: rgb(44, 62, 80);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.registerAsComboBox = QtWidgets.QComboBox(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.registerAsComboBox.setFont(font)
        self.registerAsComboBox.setStyleSheet("background-color: rgb(127, 140, 141);\n"
"color: white;")
        self.registerAsComboBox.setObjectName("registerAsComboBox")
        self.registerAsComboBox.addItem("")
        self.registerAsComboBox.addItem("")
        self.verticalLayout_2.addWidget(self.registerAsComboBox)
        self.usernameLineEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setStyleSheet("background-color: rgb(127, 140, 141);\n"
"color: white;")
        self.usernameLineEdit.setMaxLength(16)
        self.usernameLineEdit.setFrame(False)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.verticalLayout_2.addWidget(self.usernameLineEdit)
        self.passwordLineEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setStyleSheet("background-color: rgb(127, 140, 141);\n"
"color: white;")
        self.passwordLineEdit.setMaxLength(16)
        self.passwordLineEdit.setFrame(False)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.verticalLayout_2.addWidget(self.passwordLineEdit)
        self.repeatPasswordLineEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        self.repeatPasswordLineEdit.setStyleSheet("background-color: rgb(127, 140, 141);\n"
"color: white;")
        self.repeatPasswordLineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase|QtCore.Qt.InputMethodHint.ImhNoPredictiveText|QtCore.Qt.InputMethodHint.ImhSensitiveData)
        self.repeatPasswordLineEdit.setMaxLength(16)
        self.repeatPasswordLineEdit.setFrame(False)
        self.repeatPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.repeatPasswordLineEdit.setObjectName("repeatPasswordLineEdit")
        self.verticalLayout_2.addWidget(self.repeatPasswordLineEdit)
        self.showPasswordCheckBox = QtWidgets.QCheckBox(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.showPasswordCheckBox.setFont(font)
        self.showPasswordCheckBox.setStyleSheet("color: white;")
        self.showPasswordCheckBox.setObjectName("showPasswordCheckBox")
        self.verticalLayout_2.addWidget(self.showPasswordCheckBox)
        self.budgetLineEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.budgetLineEdit.setFont(font)
        self.budgetLineEdit.setStyleSheet("background-color: rgb(127, 140, 141);\n"
"color: white;")
        self.budgetLineEdit.setInputMask("")
        self.budgetLineEdit.setText("")
        self.budgetLineEdit.setMaxLength(9)
        self.budgetLineEdit.setFrame(False)
        self.budgetLineEdit.setObjectName("budgetLineEdit")
        self.verticalLayout_2.addWidget(self.budgetLineEdit)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(parent=self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.registerButton = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.registerButton.setFont(font)
        self.registerButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.registerButton.setStyleSheet("QPushButton#registerButton {\n"
"    background-color: rgb(52, 152, 219);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    width: 100px;\n"
"    height: 25px;\n"
"}\n"
"QPushButton#registerButton:hover {\n"
"    cursor: pointer;\n"
"    opacity: 0.5;\n"
"}\n"
"QPushButton#registerButton:pressed {\n"
"    padding-left: 2px;\n"
"    padding-bottom: 2px;\n"
"}")
        self.registerButton.setObjectName("registerButton")
        self.verticalLayout.addWidget(self.registerButton)
        self.goToLoginButton = QtWidgets.QPushButton(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.goToLoginButton.setFont(font)
        self.goToLoginButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.goToLoginButton.setStyleSheet("QPushButton#goToLoginButton {\n"
"    background-color: rgb(230, 126, 34);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    width: 120px;\n"
"    height: 25px;\n"
"}\n"
"QPushButton#goToLoginButton:hover {\n"
"    cursor: pointer;\n"
"    opacity: 0.5;\n"
"}\n"
"QPushButton#goToLoginButton:pressed {\n"
"    padding-left: 2px;\n"
"    padding-bottom: 2px;\n"
"}")
        self.goToLoginButton.setAutoDefault(False)
        self.goToLoginButton.setDefault(False)
        self.goToLoginButton.setFlat(True)
        self.goToLoginButton.setObjectName("goToLoginButton")
        self.verticalLayout.addWidget(self.goToLoginButton)
        self.horizontalLayout.addWidget(self.frame)
        self.horizontalLayout_2.addWidget(self.frame_3)
        Register.setCentralWidget(self.centralwidget)
        self.actionClose = QtGui.QAction(parent=Register)
        self.actionClose.setObjectName("actionClose")

        self.retranslateUi(Register)
        self.registerAsComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Registrierung"))
        self.registerAsComboBox.setPlaceholderText(_translate("Register", "Register as..."))
        self.registerAsComboBox.setItemText(0, _translate("Register", "Please select profile..."))
        self.registerAsComboBox.setItemText(1, _translate("Register", "User"))
        self.usernameLineEdit.setPlaceholderText(_translate("Register", "Username"))
        self.passwordLineEdit.setPlaceholderText(_translate("Register", "Password"))
        self.repeatPasswordLineEdit.setPlaceholderText(_translate("Register", "Repeat Password"))
        self.showPasswordCheckBox.setText(_translate("Register", "Show password"))
        self.budgetLineEdit.setPlaceholderText(_translate("Register", "Budget in €"))
        self.registerButton.setText(_translate("Register", "Register"))
        self.goToLoginButton.setText(_translate("Register", "Back to login!"))
        self.actionClose.setText(_translate("Register", "Close"))
