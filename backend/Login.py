import os.path
import sys
import Startseite
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget


class Login(QMainWindow):
    def __init__(self, stacked_widget):
        super(Login, self).__init__()  # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Login.ui"), self)

        self.stacked_widget = stacked_widget

        self.goToRegisterButton = self.findChild(QPushButton, "goToRegisterButton")
        self.goToRegisterButton.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        self.loginButton.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        self.show()


class Register(QMainWindow):
    def __init__(self, stacked_widget):
        super(Register, self).__init__()
        uic.loadUi(os.path.join("..", "frontend", "Register.ui"), self)

        self.stacked_widget = stacked_widget

        self.goToLoginButton = self.findChild(QPushButton, "goToLoginButton")
        self.goToLoginButton.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))


# if main program, run app, otherwise just import class
if __name__ == "__main__":
    app = QApplication(sys.argv)  # construct QApp before QWidget

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
    main_window.setFixedSize(520, 200)
    main_window.show()  # class Mainwindow aufrufen
    sys.exit(app.exec_())  # exit cleanly
