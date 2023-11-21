import os.path
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QPushButton, QMessageBox
from Login_Helper import show_toast, update_main_window_size, check_credentials, username_exists, add_user_to_csv
from Login_Helper import validate_inputs
import Startseite
from PyQt5 import uic


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


class Register(QMainWindow):
    def __init__(self, stacked_widget):
        super(Register, self).__init__()
        uic.loadUi(os.path.join("..", "frontend", "Register.ui"), self)

        self.stacked_widget = stacked_widget

        self.registerAsComboBox.currentIndexChanged.connect(lambda: self.update_budget_line_edit())

        self.goToLoginButton = self.findChild(QPushButton, "goToLoginButton")
        self.goToLoginButton.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        self.registerButton = self.findChild(QPushButton, "registerButton")
        self.registerButton.clicked.connect(lambda: self.register_user())

    def update_budget_line_edit(self):
        if self.registerAsComboBox.currentText() == "Verkaeufer (Gebraucht)":
            self.budgetLineEdit.setText("0")
            self.budgetLineEdit.setEnabled(False)
        else:
            self.budgetLineEdit.setEnabled(True)

    def register_user(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        budget = self.budgetLineEdit.text()
        role = self.registerAsComboBox.currentText()

        validation_result = validate_inputs(username, password, budget, role)

        if validation_result == "success":
            if not username_exists(username):
                add_user_to_csv(username, password, int(budget), role)
                show_toast("Registration successful!", QMessageBox.Information, QMessageBox.Ok)
                self.stacked_widget.setCurrentIndex(0)
            else:
                show_toast("Username already exists!", QMessageBox.Warning, QMessageBox.Ok)
        else:
            show_toast(validation_result, QMessageBox.Warning, QMessageBox.Ok)


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
