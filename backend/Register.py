import os

from PyQt5 import uic
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox

from Helper import show_toast
from Login_Helper import validate_inputs, username_exists, add_user_to_csv, toggle_password_visibility


class Register(QMainWindow):
    def __init__(self, stacked_widget):
        super(Register, self).__init__()
        self.stacked_widget = stacked_widget

        uic.loadUi(os.path.join("..", "frontend", "Register.ui"), self)

        # https://stackoverflow.com/a/47513327
        rx = QRegExp("\d+")
        self.budgetLineEdit.setValidator(QRegExpValidator(rx))

        self.registerAsComboBox.currentIndexChanged.connect(lambda: self.update_budget_line_edit())

        self.goToLoginButton = self.findChild(QPushButton, "goToLoginButton")
        self.goToLoginButton.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        self.registerButton = self.findChild(QPushButton, "registerButton")
        self.registerButton.clicked.connect(lambda: self.register_user())

        self.showPasswordCheckBox.stateChanged.connect(lambda: toggle_password_visibility(self))

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
