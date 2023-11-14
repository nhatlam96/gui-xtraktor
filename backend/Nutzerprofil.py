import os.path
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

class UserprofileWindow(QMainWindow):
    def __init__(self):
        super().__init__() # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Nutzerprofil.ui"), self)
        self.show()

# if main program, run app, otherwise just import class
if __name__ == "__main__":
    app = QApplication(sys.argv) # construct QApp before QWidget
    window = UserprofileWindow()
    window.show()  # class Mainwindow aufrufen
    sys.exit(app.exec_()) # exit cleanly