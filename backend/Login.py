import atexit
import os.path
import subprocess
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

import Helper, Helper3, Helper_Accounts
import switches
from Helper import show_toast
from Helper_Accounts import UserHandler, check_credentials


# Reference to the TimeMaster subprocess
time_master_process = None


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi(os.path.join("..", "frontend", "Login.ui"), self)

        self.setWindowTitle("X-Traktor")

        # Signale
        self.goToRegisterButton.clicked.connect(lambda: switches.switch_to.register(self))
        self.loginButton.clicked.connect(lambda: self.login_check())

        # Budgets erhöhen pro Jahr
        timeDiff = Helper.get_time_difference_since_program_time("2022-01-01 12:00:00")
        print("timeDiff", timeDiff)
        Helper_Accounts.update_budgetsPerYear(int(timeDiff))

        # ui laden
        self.load_ui()

        self.show()

    def load_ui(self):
        self.usernameLineEdit.setText("Sieglinde")
        self.passwordLineEdit.setText("1234")

    def login_check(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()

        if check_credentials(username, password):
            UserHandler.set_current_user(self, username)
            Helper.InvHandler.def_inv()
            switches.switch_to.startseite(self)
        else:
            show_toast("Invalid credentials!", QMessageBox.Warning, QMessageBox.Ok, 1750)


def main():
    print("Starting Login window...")
    global time_master_process

    # TimeMaster.py as separate process
    time_master_process = subprocess.Popen(["python", "-m", "TimeMaster"])

    app = QApplication(sys.argv)
    Login()
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
