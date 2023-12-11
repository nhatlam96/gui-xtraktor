import os.path
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

import switches
from Helper import show_toast
from backend.Helper_Accounts import UserHandler, check_credentials


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi(os.path.join("..", "frontend", "Login.ui"), self)

        self.goToRegisterButton = self.findChild(QPushButton, "goToRegisterButton")
        self.goToRegisterButton.clicked.connect(lambda: switches.switch_to.register(self))

        self.loginButton.clicked.connect(lambda: self.login_check())

        self.usernameLineEdit.setText("Sieglinde")
        self.passwordLineEdit.setText("1234")

        self.show()

    def login_check(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()

        if check_credentials(username, password):
            UserHandler.set_current_user(self, username)
            switches.switch_to.startseite(self)
            show_toast("Login successful!", QMessageBox.Information, QMessageBox.Ok)
        else:
            show_toast("Invalid credentials!", QMessageBox.Warning, QMessageBox.Ok)


def main():
    app = QApplication(sys.argv)  # construct QApp before QWidget
    window = Login()
    window.setWindowTitle("X-Traktor")
    window.show()  # class Mainwindow aufrufen
    sys.exit(app.exec_())  # exit cleanly


if __name__ == "__main__":
    main()
