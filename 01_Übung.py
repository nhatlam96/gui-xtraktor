from PyQt5.QtWidgets import *
from PyQt5 import uic


def sayit(msg):
    message = QMessageBox()
    message.setText(msg)
    message.exec_()


class LoginWindow(QMainWindow):

    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi("myGui.ui", self)
        self.show()

        self.login_Button.clicked.connect(self.login)
        self.message_Button.clicked.connect(lambda: sayit(self.message_textEdit.toPlainText()))
        self.actionClose.triggered.connect(exit)

    def login(self):
        if self.username_lineedit.text() == "username" and self.password_lineedit.text() == "password":
            self.message_textEdit.setEnabled(True)
            self.message_Button.setEnabled(True)

        else:
            message = QMessageBox()
            message.setText("invalid login!")
            message.exec_()


def main():
    app = QApplication([])
    window = LoginWindow()
    app.exec_()


main()
