import os

from PyQt5 import uic
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox, QLineEdit

from Helper import show_toast, WindowSizeHandler
from Login_Helper import validate_inputs, username_exists, add_user_to_csv


class Register(QMainWindow):
    def __init__(self, stacked_widget):
        super(Register, self).__init__()
        self.stacked_widget = stacked_widget

        register_ui = uic.loadUi(os.path.join("..", "frontend", "Register.ui"), self)
        WindowSizeHandler.set_sizes(register_ui.minimumSize(), register_ui.maximumSize())

        # https://stackoverflow.com/a/47513327
        rx = QRegExp("\d+")
        self.budgetLineEdit.setValidator(QRegExpValidator(rx))

        self.registerAsComboBox.currentIndexChanged.connect(lambda: self.update_budget_line_edit())

        self.goToLoginButton = self.findChild(QPushButton, "goToLoginButton")
        self.goToLoginButton.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        self.registerButton = self.findChild(QPushButton, "registerButton")
        self.registerButton.clicked.connect(lambda: self.register_user())

        self.showPasswordCheckBox.stateChanged.connect(self.toggle_password_visibility)

    def toggle_password_visibility(self):
        checkbox_value = self.showPasswordCheckBox.isChecked()
        if checkbox_value:
            self.passwordLineEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordLineEdit.setEchoMode(QLineEdit.Password)

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
