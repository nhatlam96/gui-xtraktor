import sys
from PyQt5.QtWidgets import *
from frontend.Startseite_ui import Ui_MainWindow


class Mainwindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        # ### fugen Typ von Traktor hinzu

        self.uic.typ_comboBox.addItem("Traktor 1")
        self.uic.typ_comboBox.addItem("Traktor 2")
        self.uic.typ_comboBox.addItem("Traktor 3")
        self.uic.typ_comboBox.addItem("Traktor 4")

        # ## Button deklarieren
        self.uic.bufferleer_button.clicked.connect(self.such_infor_leermachen)
        self.uic.such_infor_commit.clicked.connect(self.such_infor_bestatigen)

        # self.uic.lineEdit.editingFinished()         # press "enter" to finish
        # self.uic.lineEdit.returnPressed()           # return content if you press "enter"

    # ### loschen alle Eintragen, in den User Suchinformation drauf schreiben
    def such_infor_leermachen(self):
        self.uic.katergorie_lineedit.clear()
        self.uic.zustand_lineedit.clear()
        self.uic.baujahr_lineEdit.clear()
        self.uic.leistung_linedit.clear()
        self.uic.km_lineedit.clear()
        self.uic.hersteller_lineedit.clear()
        self.uic.typ_comboBox.clear()

    def such_infor_bestatigen(self):
        pass

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Mainwindow()  # class Mainwindow aufrufen
    main_win.show()

    sys.exit(app.exec_())
