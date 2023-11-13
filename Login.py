from PyQt5.QtWidgets import *
from PyQt5 import uic


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Login.ui", self)
        self.show()


def main():
    app = QApplication([])
    login = Login()
    app.exec_()


main()
