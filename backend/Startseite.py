import os.path
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

class StartpageWindow(QMainWindow):  
    def __init__(self, stacked_widget):
        super().__init__() # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Startseite.ui"), self)
                  
        # fuegen Typ von Traktor hinzu
        self.typ_comboBox.addItem("Traktor 1")
        self.typ_comboBox.addItem("Traktor 2")
        self.typ_comboBox.addItem("Traktor 3")
        self.typ_comboBox.addItem("Traktor 4")

        # ######## fuegen Zustand von Traktor hinzu


        # ### Zurücksetzen Button und Bestätigen Button deklarieren

        self.bufferleer_button.clicked.connect(self.empty_search_info)
        self.such_infor_commit.clicked.connect(self.confirm_search_info)

        # self.lineEdit.editingFinished()         # press "enter" to finish
        # self.lineEdit.returnPressed()           # return content if you press "enter"

        self.stacked_widget = stacked_widget

        self.show()
        
        # self.uic.lineEdit.editingFinished()         # press "enter" to finish
        # self.uic.lineEdit.returnPressed()           # return content if you press "enter"

        # ############ Spin Box bei den Auf Lager und Baujahr einstellen

        self.baujahr_spinBox.setMinimum(1900)
        self.baujahr_spinBox.setMaximum(2023)

        self.auf_lager_spinBox.setMinimum(0)
        self.auf_lager_spinBox.setMaximum(100)

        # ########### Umgehen mit dem Ereignis, wenn User Value des Baujahr geaendert wurde

        # self.uic.baujahr_spinBox.valueChanged.connect(self.Baujahr_Value_aendern)

        # ########### Umgehen mit dem Ereignis, wenn User Value des Auf Lager geaendert wurde

        # self.uic.auf_lager_spinBox.valueChanged.connect(self.Auflager_Value_aendern)

    # ########## aktuelle Value von Baujahr nehmen
    def baujahr_value_nehmen(self):
        return self.baujahr_spinBox.value()

    # ########## aktuelle Value von Auf Lager nehmen
    def auflager_value_nehmen(self):
        return self.auf_lager_spinBox.value()

    # ############ aktuelle Value von Km nehmen
    def km_value_nehmen(self):
        return self.horizontalSlider_km.value()

    # ############ aktuelle Value von Leistung nehmen
    def leistung_value_nehmen(self):
        return self.horizontalSlider_leistung.value()

    # ############ aktuelle Value von Preis nehmen

    def preis_value_nehmen(self):
        return self.horizontalSlider_preis.value()


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