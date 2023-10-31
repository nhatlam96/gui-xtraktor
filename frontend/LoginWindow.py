from PyQt5.QtWidgets import *
from PyQt5 import uic


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('LoginWindow.ui', self)
        self.show()


def main():
    app = QApplication([])
    login_window = LoginWindow()
    app.exec_()


main()
