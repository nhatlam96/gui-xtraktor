import sys
from PyQt5.QtWidgets import *
from traktor import Ui_MainWindow


class Mainwindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        # ## Button deklarieren
        self.uic.Button_Profile.clicked.connect(self.goto_profile)
        self.uic.Button_startseite.clicked.connect(self.goto_startseite)
        self.uic.Button_Warenkopf.clicked.connect(self.goto_warenkopf)
        self.uic.Button_Artikelsuchen.clicked.connect(self.get_suchfeld_content)

        # self.uic.lineEdit.editingFinished()         # press "enter" to finish
        # self.uic.lineEdit.returnPressed()           # return content if you press "enter"
        self.uic.suchfeld.text()

    def get_suchfeld_content(self):
        # copy_content = self.uic.Button_Artikelsuchen.toPlainText()
        pass
    def goto_warenkopf(self):
        # ## go to the shoppingsite interface
        pass

    def goto_startseite(self):
        # get the startseite interface
        pass

    def goto_profile(self):
        # ## get the interface of profile
        pass

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Mainwindow()  # class Mainwindow aufrufen
    main_win.show()

    sys.exit(app.exec_())
