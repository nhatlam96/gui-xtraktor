import os.path
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

class StartpageWindow(QMainWindow):  
    def __init__(self):
        super().__init__() # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Startseite.ui"), self)
        self.show()
          
        # fuegen Typ von Traktor hinzu
        self.typ_comboBox.addItem("Traktor 1")
        self.typ_comboBox.addItem("Traktor 2")
        self.typ_comboBox.addItem("Traktor 3")
        self.typ_comboBox.addItem("Traktor 4")

        # Button deklarieren
        self.bufferleer_button.clicked.connect(self.empty_search_info)
        self.such_infor_commit.clicked.connect(self.confirm_search_info)

        # self.lineEdit.editingFinished()         # press "enter" to finish
        # self.lineEdit.returnPressed()           # return content if you press "enter"

    # loeschen alle Eintraege, in den User Suchinformation drauf schreiben
    def empty_search_info(self):
        self.katergorie_lineedit.clear()
        self.zustand_lineedit.clear()
        self.baujahr_lineEdit.clear()
        self.leistung_linedit.clear()
        self.km_lineedit.clear()
        self.hersteller_lineedit.clear()
        self.typ_comboBox.clear()

    # hol mal alle Informationen, die User bereits eingetragen hat
    def confirm_search_info(self):
        print("Button click!")
        print("Kategorie: ", self.katergorie_lineedit.text())
        print("Zustand: ", self.zustand_lineedit.text())
        print("Leistung: ", self.leistung_linedit.text())
        print("Km/h: ", self.km_lineedit.text())
        print("Hersteller: ", self.hersteller_lineedit.text())
        print("Typ: ", self.typ_comboBox.currentText())

# if main program, run app, otherwise just import class
if __name__ == "__main__":
    app = QApplication(sys.argv) # construct QApp before QWidget
    window = StartpageWindow()
    window.show()  # class Mainwindow aufrufen
    sys.exit(app.exec_()) # exit cleanly