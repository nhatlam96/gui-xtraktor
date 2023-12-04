import os.path
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

class UserprofileWindow(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__() # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Nutzerprofil.ui"), self)
        self.stacked_widget = stacked_widget
        self.show()
