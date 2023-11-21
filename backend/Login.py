import os.path
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QPushButton, QMessageBox

from Helper import show_toast, UserHandler, WindowSizeHandler, update_main_window_size
from Login_Helper import check_credentials
from Register import Register
from Startseite import Startseite


class Login(QMainWindow):
    def __init__(self, stacked_widget):
        super(Login, self).__init__()
        self.stacked_widget = stacked_widget

        login_ui = uic.loadUi(os.path.join("..", "frontend", "Login.ui"), self)
        WindowSizeHandler.set_sizes(login_ui.minimumSize(), login_ui.maximumSize())

        self.goToRegisterButton = self.findChild(QPushButton, "goToRegisterButton")
        self.goToRegisterButton.clicked.connect(lambda: self.switch_to_register())

        self.loginButton.clicked.connect(lambda: self.login_check())
        self.show()

    def switch_to_register(self):
        register = Register(self.stacked_widget)
        self.stacked_widget.addWidget(register)
        self.stacked_widget.setCurrentWidget(register)
        update_main_window_size(self.stacked_widget.main_window)

    def switch_to_startseite(self):
        startseite = Startseite(self.stacked_widget)
        self.stacked_widget.addWidget(startseite)
        self.stacked_widget.setCurrentWidget(startseite)
        update_main_window_size(self.stacked_widget.main_window)
        show_toast("Login successful!", QMessageBox.Information, QMessageBox.Ok)

    def login_check(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()

        if check_credentials(username, password):
            UserHandler.set_current_user(username)
            self.switch_to_startseite()
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
    main_window.setMinimumSize(WindowSizeHandler.get_minimum_size())
    main_window.setMaximumSize(WindowSizeHandler.get_maximum_size())
    main_window.show()

    stacked_widget.main_window = main_window
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
