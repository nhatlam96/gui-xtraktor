import os.path
import csv
from PyQt5.QtCore import Qt

import switches
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox

import Helper
from Helper import show_toast, show_toast_confirmation
import Helper2
from Helper_Accounts import add_user_to_csv, UserHandler, toggle_password_visibility

ACCOUNTS_FILE_PATH = os.path.join("..", "resources", "csv", "Accounts.csv")


class UserprofileWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Nutzerprofil.ui"), self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)

        print("AUFRUF NUTZER")

        # Übergabeparameter
        self.user = UserHandler.get_current_user()[0]

        # Signale
        self.aenderungenSpeichernButton.clicked.connect(self.handle_save_changes)
        self.aenderungenVerwerfenButton.clicked.connect(lambda: self.display_userprofile())
        self.showPasswordCheckBox.stateChanged.connect(lambda: toggle_password_visibility(self, "Userprofile"))
        self.logout_button.clicked.connect(lambda: self.logout())

        # load ui
        self.display_userprofile()
        Helper2.load.complete_header(self)

        self.show()

    def closeEvent(self, event):
        print("Window is closing")
        switches.WindowHandler.release_window(UserprofileWindow)
        super().closeEvent(event)  # Fenster wird wirklich geschlossen

    @staticmethod
    def logout():
        Helper.BuyHandler.clear_current_shoppinglist()
        switches.switch_to.login()

    def handle_save_changes(self):
        confirmation = show_toast_confirmation(self, "Are you sure you want to save changes?")
        if confirmation == QMessageBox.Yes:
            user = UserHandler.get_current_user()[0]
            add_user_to_csv(user, self.passwordLineEdit.text(), self.budgetLineEdit.text(),
                            self.loginStatusLabel.text())
            show_toast("Changes saved!", QMessageBox.Information, QMessageBox.Ok, 1750)

    def display_userprofile(self):
        with open(ACCOUNTS_FILE_PATH, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['username'] == self.user:
                    self.loginStatusLabel.setText(row['role'])
                    self.usernameLabel.setText(row['username'])
                    self.passwordLineEdit.setText(row['password'])
                    self.budgetLineEdit.setText(row['budget'])
