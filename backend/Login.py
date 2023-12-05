import os.path
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QPushButton, QMessageBox

from Helper import show_toast, UserHandler
from Login_Helper import check_credentials
import switches


class Login(QMainWindow):
    def __init__(self, stacked_widget):
        super(Login, self).__init__()
        self.stacked_widget = stacked_widget

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
    app = QApplication(sys.argv)

    stacked_widget = QStackedWidget()
    stacked_widget.addWidget(Login(stacked_widget))

    widget = QWidget()
    layout = QVBoxLayout(widget)
    layout.addWidget(stacked_widget)

    main_window = QMainWindow()
    main_window.setCentralWidget(widget)
    main_window.setWindowTitle("X-Traktor")
    main_window.show()

    stacked_widget.main_window = main_window
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
