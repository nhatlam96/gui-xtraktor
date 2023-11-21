import os.path
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QPushButton, QMessageBox

import Startseite
from Helper import show_toast
from Login_Helper import update_main_window_size, check_credentials
from backend.Login_Register import Register


class Login(QMainWindow):
    def __init__(self, stacked_widget):
        super(Login, self).__init__()
        uic.loadUi(os.path.join("..", "frontend", "Login.ui"), self)

        self.stacked_widget = stacked_widget

        self.goToRegisterButton = self.findChild(QPushButton, "goToRegisterButton")
        self.goToRegisterButton.clicked.connect(lambda: self.switch_to_register())

        self.loginButton.clicked.connect(lambda: self.login_check())
        self.show()

    def switch_to_register(self):
        self.stacked_widget.setCurrentIndex(1)
        update_main_window_size(self.stacked_widget.main_window, 540, 220)

    def switch_to_startseite(self):
        self.stacked_widget.setCurrentIndex(2)
        update_main_window_size(self.stacked_widget.main_window, 888, 666)
        show_toast("Login successful!", QMessageBox.Information, QMessageBox.Ok)

    def login_check(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()

        if check_credentials(username, password):
            self.switch_to_startseite()
        else:
            show_toast("Invalid credentials!", QMessageBox.Warning, QMessageBox.Ok)


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
