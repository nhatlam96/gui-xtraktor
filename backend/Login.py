import atexit
import os.path
import subprocess
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

import switches
from Helper import show_toast
from Helper_Accounts import UserHandler, check_credentials

# Reference to the TimeMaster subprocess
time_master_process = None


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
            show_toast("Login successful!", QMessageBox.Information, QMessageBox.Ok, 1750)
        else:
            show_toast("Invalid credentials!", QMessageBox.Warning, QMessageBox.Ok, 1750)


def main():
    global time_master_process

    # Start TimeMaster.py as a separate process
    time_master_process = subprocess.Popen(["python", "-m", "TimeMaster"])

    app = QApplication(sys.argv)
    window = Login()
    window.setWindowTitle("X-Traktor")
    window.show()
    sys.exit(app.exec_())


@atexit.register
def on_exit():
    global time_master_process
    if time_master_process:
        # noinspection PyUnresolvedReferences
        time_master_process.terminate()
        print("TimeMaster terminated")


if __name__ == "__main__":
    main()
