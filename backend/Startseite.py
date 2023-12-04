import csv
import os
import os.path
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *

from Helper import UserHandler

csv_path = os.path.join("..", "resources", "csv")
image_path = os.path.join("..", "resources", "Traktoren")


class Startseite(QMainWindow):

    def __init__(self, stacked_widget):
        super().__init__()  # vereinfacht das Erstellen weiterer Subklassen
        self.stacked_widget = stacked_widget

        uic.loadUi(os.path.join("..", "frontend", "Startseite.ui"), self)

        user = UserHandler.get_current_user()
        print(f"Startseite: {user}")

        # ### Zurücksetzen Button und Bestätigen Button deklarieren
        self.bufferleer_button.clicked.connect(self.empty_search_info)
        self.such_infor_commit.clicked.connect(self.confirm_search_info)

        # ### Such_pushButton in Suchfeld einstellen

        self.pushButton_suchen.clicked.connect(self.confirm_suchfeld_info)
        self.Lineedit_suchfeld.editingFinished.connect(self.confirm_suchfeld_info_with_enter)  # press "enter" to finish
        # self.lineEdit.returnPressed()           # return content if you press "enter"

        self.setup_waren_ui()

        # ### Ereignisse bei den QSlider von Preis, Leistung und Kilometer umgehen und Werte
        # ### auf die entsprechenden Label anzuzeigen

        self.horizontalSlider_preis.valueChanged.connect(self.preis_changed)
        self.horizontalSlider_km.valueChanged.connect(self.km_changed)
        self.horizontalSlider_leistung.valueChanged.connect(self.leistung_changed)

        # self.uic.lineEdit.editingFinished()         # press "enter" to finish
        # self.uic.lineEdit.returnPressed()           # return content if you press "enter"

        # ############ Spin Box bei dem Lager und Baujahr einstellen

        self.baujahr_spinBox.setMinimum(1900)
        self.baujahr_spinBox.setMaximum(2023)

        self.auf_lager_spinBox.setMinimum(0)
        self.auf_lager_spinBox.setMaximum(100)

        # ########### Umgehen mit dem Ereignis, wenn User Value des Baujahr geaendert wurde

        # self.uic.baujahr_spinBox.valueChanged.connect(self.Baujahr_Value_aendern)

        # ########### Umgehen mit dem Ereignis, wenn User Value des Auf Lager geaendert wurde

        # self.uic.auf_lager_spinBox.valueChanged.connect(self.Auflager_Value_aendern)

        # ########## Fügen Artikel in ComboBox hinzu

        self.comboBox_hersteller.addItem("")
        self.comboBox_hersteller.addItems(self.add_hersteller())

        self.typ_comboBox.addItem("")
        self.typ_comboBox.addItems(self.add_typ())

        self.show()

    # ########## aktuelle Value von Baujahr nehmen
    def baujahr_value_nehmen(self):
        return self.baujahr_spinBox.value()

    # ########## aktuelle Value von Lager nehmen
    def auflager_value_nehmen(self):
        return self.auf_lager_spinBox.value()

    # ############ aktuelle Value von Km nehmen
    def km_value_nehmen(self):
        return self.horizontalSlider_km.value()

    # ############ aktuelle Value von Leistung nehmen
    def leistung_value_nehmen(self):
        return self.horizontalSlider_leistung.value()

    # ########## aktuelle Value von Preis nehmen

    def preis_value_nehmen(self):
        return self.horizontalSlider_preis.value()

    # ########## Preis Wert auf Preis_label anzeigen lassen
    def preis_changed(self):
        preis_value = self.preis_value_nehmen()
        self.preis_anzeigt.setText(f"Aktuelle Wert: {preis_value}")

    # ########## Km Wert auf Km_label anzeigen lassen
    def km_changed(self):
        km_value = self.km_value_nehmen()
        self.km_anzeigt.setText(f"Aktuelle Wert: {km_value}")

    # ########## Leistung Wert auf Leistung_label anzeigen lassen
    def leistung_changed(self):
        leistung_value = self.leistung_value_nehmen()
        self.leistung_anzeigt.setText(f"Aktuelle Wert: {leistung_value}")

    # ########## Add Artikel in die Hersteller ComboBox hinzu

    def add_hersteller(self):
        Hersteller_eintraeger = []
        Arbeitmaschinen_csv_path = os.path.join(csv_path, "mobile Arbeitsmaschinen Landwirtschaft.csv")

        # ### Öffnen ein csv File und das durch eigene Value abspeichert
        with open(Arbeitmaschinen_csv_path, "r") as file:
            csv_file_reader = csv.reader(file)
            next(csv_file_reader)  # ### Verzichten auf Header Zeile

            for row in csv_file_reader:
                Hersteller_eintraeger.append(row[0])

        return set(Hersteller_eintraeger)

    # ########## Add Artikel in Typ ComboBox hinzu

    def add_typ(self):
        typ_eintraeger = []
        Arbeitmaschinen_csv_path = os.path.join(csv_path, "mobile Arbeitsmaschinen Landwirtschaft.csv")

        with open(Arbeitmaschinen_csv_path, "r") as file:
            csv_file_reader = csv.reader(file)
            next(csv_file_reader)

            for row in csv_file_reader:
                typ_eintraeger.append(row[1])

        return set(typ_eintraeger)

    def load_list_data(self):

        main_list = []

        csv_list_path = os.path.join(csv_path, "mobile Arbeitsmaschinen Landwirtschaft.csv")

        with open(csv_list_path, "r") as file:
            csv_file_reader = csv.reader(file)

            next(csv_file_reader)  # Auf Header Info springen

            vermitteln_to_list = list(csv_file_reader)  # csv reader file in List vermitteln

            for index in range(len(vermitteln_to_list)):
                main_list.append(vermitteln_to_list[index])

        return main_list

    def load_list_image(self):
        alle_file = os.listdir("..", "resources" | "Traktoren")
        pass

    # ########## Funktion für Dynamic aufladen
    def setup_waren_ui(self):
        scroll_area = self.findChild(QScrollArea, "scrollArea")
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        data_list = self.load_list_data()

        for index in range(len(data_list)):
            new_widget = QWidget()
            inner_layout = QHBoxLayout(new_widget)

            inner_layout1 = QVBoxLayout()
            herstell_label = QLabel("Hersteller: " + str(data_list[index][0]))
            modell_label = QLabel("Modell: " + str(data_list[index][1]))
            inner_layout1.addWidget(herstell_label)
            inner_layout1.addWidget(modell_label)

            inner_layout2 = QVBoxLayout()
            preis = QLabel("Preis: " + str(data_list[index][4]))
            kaufen = QLabel("Kaufen")
            inner_layout2.addWidget(preis)
            inner_layout2.addWidget(kaufen)

            inner_layout3 = QHBoxLayout()
            ps = QLabel("PS: " + str(data_list[index][2]))
            leistung = QLabel("Leistung: " + str(data_list[index][2]))
            km = QLabel("Km/h: " + str(data_list[index][3]))
            inner_layout3.addWidget(ps)
            inner_layout3.addWidget(leistung)
            inner_layout3.addWidget(km)

            inner_layout4 = QHBoxLayout()
            inner_layout4.addLayout(inner_layout1)
            inner_layout4.addLayout(inner_layout2)

            inner_layout5 = QVBoxLayout()
            inner_layout5.addLayout(inner_layout4)
            inner_layout5.addLayout(inner_layout3)

            inner_layout6 = QHBoxLayout()
            bild_label = QLabel()
            # bild_label.setPixmap()
            inner_layout6.addWidget(bild_label)
            inner_layout6.addLayout(inner_layout5)

            inner_layout.addLayout(inner_layout6)
            layout.addWidget(new_widget)

        scroll_area.setWidget(content_widget)

    # ### Löschen alle Einträge, in den User Suchinformation darauf geschrieben haben
    def empty_search_info(self):

        self.horizontalSlider_leistung.setValue(0)
        self.horizontalSlider_km.setValue(0)
        self.horizontalSlider_preis.setValue(0)
        self.baujahr_spinBox.setValue(1900)
        self.auf_lager_spinBox.setValue(0)
        self.comboBox_hersteller.setCurrentText("")
        self.typ_comboBox.setCurrentText("")

    # ########## Alle Informationen zurückgeben, die User bereits eingetragen hat
    def confirm_search_info(self):
        print("Button click!")
        print("Preis: ", self.horizontalSlider_preis.value())  # get the value of Preis
        print("Zustand: ", self.comboBox_zustand.currentText())  # get the value of Zustand
        print("Leistung: ", self.horizontalSlider_leistung.value())  # get the value of Leistung
        print("Km/h: ", self.horizontalSlider_km.value())  # get the value of Leistung
        print("Hersteller: ", self.comboBox_hersteller.currentText())  # get the value of Hersteller
        print("Typ: ", self.typ_comboBox.currentText())  # get the value of Typ
        print("Baujahr: ", self.baujahr_spinBox.value())  # get value of Baujahr SpinBox
        print("Auf Lager: ", self.auf_lager_spinBox.value())  # get value of Lager SpinBox

    def confirm_suchfeld_info(self):
        such_Inhalt = self.Lineedit_suchfeld.text()
        print(such_Inhalt)

    def confirm_suchfeld_info_with_enter(self):
        such_Inhalt = self.Lineedit_suchfeld.text()
        print(such_Inhalt)


"""

# NICHT MEHR GÜLTIG ZU VIELE ABHÄNGIGKEITEN!!!  --->>>  NUR NOCH ÜBER LOGIN --->>> PLS LOGIN VEREINFACHEN, DANKE!

# if main program, run app, otherwise just import class
if __name__ == "__main__":
    app = QApplication(sys.argv)  # construct QApp before QWidget
    test = QStackedWidget()
    window = Startseite(test)
    window.show()  # class Mainwindow aufrufen
    sys.exit(app.exec_())  # exit cleanly

"""