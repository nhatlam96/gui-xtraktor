import os.path

from PyQt5.QtWidgets import *
from PyQt5 import uic

class ProfileWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join("..", "frontend", "Nutzerprofil.ui"), self)
        self.show()

def main():
    app = QApplication([])
    profileWindow = ProfileWindow()
    app.exec_()

main()
