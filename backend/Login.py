import os.path
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QPushButton, QMessageBox
from Helper import showToast, updateMainWindowSize, checkCredentials, usernameExists, addUserToCSV, validateInputs
import Startseite
from PyQt5 import uic


class Login(QMainWindow):
    def __init__(self, stacked_widget):
        super(Login, self).__init__()
        uic.loadUi(os.path.join("..", "frontend", "Login.ui"), self)

        self.stacked_widget = stacked_widget

        self.goToRegisterButton = self.findChild(QPushButton, "goToRegisterButton")
        self.goToRegisterButton.clicked.connect(lambda: self.switchToRegister())

        self.loginButton.clicked.connect(lambda: self.loginCheck())
        self.show()

    def switchToRegister(self):
        self.stacked_widget.setCurrentIndex(1)
        updateMainWindowSize(self.stacked_widget.main_window, 540, 220)

    def switchToStartseite(self):
        self.stacked_widget.setCurrentIndex(2)
        updateMainWindowSize(self.stacked_widget.main_window, 888, 666)
        showToast("Login successful!", QMessageBox.Information)

    def loginCheck(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()

        if checkCredentials(username, password):
            self.switchToStartseite()
        else:
            showToast("Invalid credentials!", QMessageBox.Warning)


class Register(QMainWindow):
    def __init__(self, stacked_widget):
        super(Register, self).__init__()
        uic.loadUi(os.path.join("..", "frontend", "Register.ui"), self)

        self.stacked_widget = stacked_widget

        self.goToLoginButton = self.findChild(QPushButton, "goToLoginButton")
        self.goToLoginButton.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        self.registerButton = self.findChild(QPushButton, "registerButton")
        self.registerButton.clicked.connect(lambda: self.registerUser())

    def registerUser(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        budget = self.budgetLineEdit.text()
        role = self.registerAsComboBox.currentText()

        validation_result = validateInputs(username, password, budget, role)

        if validation_result == "success":
            if not usernameExists(username):
                addUserToCSV(username, password, int(budget), role)
                showToast("Registration successful!", QMessageBox.Information)
                self.stacked_widget.setCurrentIndex(0)
            else:
                showToast("Username already exists!", QMessageBox.Warning)
        else:
            showToast(validation_result, QMessageBox.Warning)


def main():
    app = QApplication(sys.argv)

    stacked_widget = QStackedWidget()

    login = Login(stacked_widget)
    register = Register(stacked_widget)
    start = Startseite.StartpageWindow(stacked_widget)

    stacked_widget.addWidget(login)
    stacked_widget.addWidget(register)
    stacked_widget.addWidget(start)

    widget = QWidget()
    layout = QVBoxLayout(widget)
    layout.addWidget(stacked_widget)

    main_window = QMainWindow()
    main_window.setCentralWidget(widget)
    main_window.setFixedSize(540, 220)
    main_window.setWindowTitle("X-Traktor")
    main_window.show()

    stacked_widget.main_window = main_window
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
