import os.path

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton

from Helper import UserHandler
import Helper2
from Login_Helper import add_user_to_csv, toggle_password_visibility
from backend.Nutzerprofil_Helper import display_userprofile


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
        self.aenderungenSpeichernButton.clicked.connect(
            lambda: add_user_to_csv(user, self.passwortLineEdit.text(), self.budgetLineEdit.text(),
                                    self.loginStatusLabel.text()))

        self.aenderungenVerwerfenButton = self.findChild(QPushButton, "aenderungenVerwerfenButton")
        self.aenderungenVerwerfenButton.clicked.connect(lambda: display_userprofile(self, user))

        self.showPasswordCheckBox.stateChanged.connect(lambda: toggle_password_visibility(self))

        self.show()
