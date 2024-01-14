import os

from PyQt5 import uic
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox

from Helper import show_toast
from Helper_Accounts import add_user_to_csv, username_exists, validate_inputs, toggle_password_visibility
import switches


class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join("..", "frontend", "Register.ui"), self)

        # erklärung: https://stackoverflow.com/a/47513327
        rx = QRegExp("\d+")
        self.budgetLineEdit.setValidator(QRegExpValidator(rx))

        # for future use, when a role-based budget is implemented
        # self.registerAsComboBox.currentIndexChanged.connect(lambda: self.update_budget_line_edit())

        self.goToLoginButton = self.findChild(QPushButton, "goToLoginButton")
        self.goToLoginButton.clicked.connect(lambda: switches.switch_to.login(self))

        self.registerButton = self.findChild(QPushButton, "registerButton")
        self.registerButton.clicked.connect(lambda: self.register_user())

        self.showPasswordCheckBox.stateChanged.connect(lambda: toggle_password_visibility(self, "Register"))

        self.show()

    """ for future use, when a role-based budget is implemented
    def update_budget_line_edit(self):
        if self.registerAsComboBox.currentText() == "Verkäufer (Gebraucht)":
            self.budgetLineEdit.setText("0")
            self.budgetLineEdit.setEnabled(False)
        else:
            self.budgetLineEdit.setEnabled(True)
    """

    def register_user(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        password_repeat = self.repeatPasswordLineEdit.text()
        budget = self.budgetLineEdit.text()
        role = self.registerAsComboBox.currentText()

        validation_result = validate_inputs(username, password, password_repeat, budget, role)

        if validation_result == "success":
            if not username_exists(username):
                add_user_to_csv(username, password, int(budget), role)
                show_toast("Registration successful!", QMessageBox.Information, QMessageBox.Ok, 1750)
                switches.switch_to.login(self)
            else:
                show_toast("Username already exists!", QMessageBox.Warning, QMessageBox.Ok, 1750)
        else:
            show_toast(validation_result, QMessageBox.Warning, QMessageBox.Ok, 1750)
