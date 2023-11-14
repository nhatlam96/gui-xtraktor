import os.path

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# Global variables for both login and register instances to be used in the switchToRegister and switchToLogin slots
login = None
register = None


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join("..", "frontend", "Login.ui"), self)
        self.show()

        # Connect the push button click event to the slot
        self.goToRegisterButton = self.findChild(QPushButton, "goToRegisterButton")
        self.goToRegisterButton.clicked.connect(self.switchToRegister)

    # noinspection PyUnresolvedReferences
    @staticmethod
    def switchToRegister():
        global login, register  # Use the global instances
        login.hide()
        register.show()


class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join("..", "frontend", "Register.ui"), self)
        self.hide()  # Hide the register form initially

        # Connect the push button click event to the slot
        self.goToLoginButton = self.findChild(QPushButton, "goToLoginButton")
        self.goToLoginButton.clicked.connect(self.switchToLogin)

    # noinspection PyUnresolvedReferences
    @staticmethod
    def switchToLogin():
        global login, register  # Use the global instances
        register.hide()
        login.show()


def main():
    app = QApplication([])

    global login, register  # Declare global variables
    # Create instances for both login and register forms
    login = Login()
    register = Register()

    app.exec_()


if __name__ == "__main__":
    main()
