import os.path

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox

from Helper import show_toast, show_toast_confirmation
import Helper2
from Helper_Accounts import add_user_to_csv, UserHandler, toggle_password_visibility, display_userprofile


class UserprofileWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Nutzerprofil.ui"), self)

        Helper2.load.complete_header(self)

        user = UserHandler.get_current_user()[0]
        display_userprofile(self, user)

        self.logoutButton = self.findChild(QPushButton, "Logout")
        Helper2.load.logout_button(self, self.logoutButton)

        self.aenderungenSpeichernButton = self.findChild(QPushButton, "aenderungenSpeichernButton")
        self.aenderungenSpeichernButton.clicked.connect(self.handle_save_changes)

        self.aenderungenVerwerfenButton = self.findChild(QPushButton, "aenderungenVerwerfenButton")
        self.aenderungenVerwerfenButton.clicked.connect(lambda: display_userprofile(self, user))

        self.showPasswordCheckBox.stateChanged.connect(lambda: toggle_password_visibility(self))

        self.show()

    def handle_save_changes(self):
        confirmation = show_toast_confirmation(self, "Are you sure you want to save changes?")
        if confirmation == QMessageBox.Yes:
            user = UserHandler.get_current_user()[0]
            add_user_to_csv(user, self.passwordLineEdit.text(), self.budgetLineEdit.text(),
                            self.loginStatusLabel.text())
            show_toast("Changes saved!", QMessageBox.Information, QMessageBox.Ok, 1750)
