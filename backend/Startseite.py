import csv
import locale
import os
import os.path
import sys

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import switches
import Helper
import Helper2
import Helper4


# Ressourcenpfade
csv_path = os.path.join("..", "resources", "csv")
image_path = os.path.join("..", "resources", "Traktoren")

class Startseite(QMainWindow):

    def __init__(self):
        super().__init__()  # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Startseite.ui"), self)


        # NEUES LISTENMODEL MUSS NOCH ANGEWENDET WERDEN
        self.traktor_Liste = Helper2.load.all_traktor_data(self)
        self.traktor_infos = Helper2.load.product_info(self, self.traktor_Liste)
        self.traktor_filter_Liste = Helper2.load.all_traktor_data(self)
        self.traktor_filter_infos = Helper2.load.product_info(self, self.traktor_filter_Liste)


        # ERST NACH TRAKTOREN MACHEN
        """self.zubehoer_Liste = Helper2.load.all_zubehoer_data(self)
        self.zubehoer_infos = Helper2.load.product_info(self, self.zubehoer_Liste)
        self.zubehoer_filter_Liste = Helper2.load.all_zubehoer_data(self)
        self.zubehoer_filter_infos = Helper2.load.product_info(self, self.zubehoer_filter_Liste)"""


        # Zwischenspeicher für Listen
        #self.datalist = self.load_list_data()               # Standard Liste
        #self.filtereddatalist = self.load_list_data()       # Liste mit Filter

        # lokale Umgebung laden
        Helper2.conf.locale_setup(self)

        # Button dict. von dyn. Layout
        self.buttons = {}

        # Seite laden
        self.setup_waren_ui()
        self.load_ui()

        self.show()



    def load_ui(self):
        Helper2.load.complete_header(self)
        self.load_filter_ui()


    def load_filter_ui(self):


        # Suchfeld -> bitte button zum Sortieren hinzufügen
        self.pushButton_suchen.clicked.connect(self.confirm_suchfeld_info)
        self.Lineedit_suchfeld.editingFinished.connect(self.confirm_suchfeld_info_with_enter)  # press "enter" to finish
        # self.lineEdit.returnPressed()           # return content if you press "enter"

        # Hersteller
        self.comboBox_hersteller.addItem("")
        self.comboBox_hersteller.addItems(self.add_hersteller())
        self.comboBox_hersteller.currentTextChanged.connect(lambda value: self.filter_changed_hersteller(value))

        # Typ
        self.typ_comboBox.addItem("")
        self.typ_comboBox.addItems(self.add_typ())
        self.typ_comboBox.currentTextChanged.connect(self.filter_changed_typ)

        # Baujahr
        self.baujahr_spinBox.setMinimum(1900)
        self.baujahr_spinBox.setMaximum(2023)

        # Leistung & Km/h
        self.horizontalSlider_km.valueChanged.connect(self.km_changed)
        self.horizontalSlider_km.valueChanged.connect(self.filter_changed_km)
        self.horizontalSlider_leistung.valueChanged.connect(self.leistung_changed)
        self.horizontalSlider_leistung.valueChanged.connect(self.filter_changed_leistung)

        # Preis
        self.min_preis.addItems(self.add_min_preis())  # allow only adding string
        self.max_preis.addItems(self.add_max_preis())
        self.min_preis.currentTextChanged.connect(lambda currentValue: self.filter_changed_minPreis(currentValue))
        self.max_preis.currentTextChanged.connect(lambda currentValue: self.filter_changed_maxPreis(currentValue))
        self.sell_Button.clicked.connect(lambda: switches.switch_to.Inventar(self))

        # Zurücksetzen & Bestätigen
        self.bufferleer_button.clicked.connect(self.empty_search_info)
        self.such_infor_commit.clicked.connect(self.confirm_search_info)


        # Tu´s Ideen
        # self.uic.lineEdit.editingFinished()         # press "enter" to finish
        # self.uic.lineEdit.returnPressed()           # return content if you press "enter"

        # self.uic.baujahr_spinBox.valueChanged.connect(self.Baujahr_Value_aendern)



    def add_min_preis(self):
        preis_item = []
        start_preis = 100000

        for count in range(20):
            preis_item.append(start_preis)
            start_preis += 100000

        for count in range(20):
            preis_item[count] = str(preis_item[count])  # ### string Umwandlung
        return preis_item

    def add_max_preis(self):
        preis_items = []
        end_preis = 100000

        for count in range(20):
            preis_items.append(end_preis)
            end_preis += 100000
        for count in range(20):
            preis_items[count] = str(preis_items[count])
        return preis_items

    def filter_changed_minPreis(self, currentValue):
        Helper4.FilterHandler.set_Filter(pre_min=currentValue)
        print(Helper4.FilterHandler.get_Filter())

    def filter_changed_maxPreis(self, currentValue):
        Helper4.FilterHandler.set_Filter(pre_max=currentValue)
        print(Helper4.FilterHandler.get_Filter())

    def filter_changed_km(self, currentKm):
        Helper4.FilterHandler.set_Filter(ges=currentKm)
        print(Helper4.FilterHandler.get_Filter())

    def filter_changed_leistung(self, currentLeistung):
        Helper4.FilterHandler.set_Filter(lei=currentLeistung)
        print(Helper4.FilterHandler.get_Filter())

    def filter_changed_typ(self, currentTyp):
        Helper4.FilterHandler.set_Filter(typ=currentTyp)
        print(Helper4.FilterHandler.get_Filter())

    def filter_changed_hersteller(self, currentHersteller):
        Helper4.FilterHandler.set_Filter(her=currentHersteller)
        print(Helper4.FilterHandler.get_Filter())


    def get_minPreis(self):
        return self.min_preis.currentText()

    def get_maxPreis(self):
        return  self.max_preis.currentText()

    def baujahr_value_nehmen(self):
        return self.baujahr_spinBox.value()

    def km_value_nehmen(self):
        return self.horizontalSlider_km.value()

    def leistung_value_nehmen(self):
        return self.horizontalSlider_leistung.value()

    def km_changed(self):
        km_value = self.km_value_nehmen()
        self.km_anzeigt.setText(f"Aktuelle Wert: {km_value}")

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

        print(main_list)
        return main_list



    def setup_waren_ui(self):

        scroll_area = self.findChild(QScrollArea, "scrollArea")
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        liste = self.traktor_filter_Liste
        info_liste = self.traktor_filter_infos


        for x in range(len(liste)):

            new_widget = QWidget()
            new_widget.setMaximumHeight(200)

            inner_layout = QHBoxLayout(new_widget)  # v-layout für widget

            picture_layout = QVBoxLayout()
            inner_layout.addLayout(picture_layout, 1)

            label1 = QLabel()
            picture_layout.addWidget(label1)
            pixmap = Helper2.load.product_pic(self, liste[x])
            scaled_pixmap = pixmap.scaled(200, 200)
            label1.setPixmap(scaled_pixmap)

            info_layout = QVBoxLayout()
            inner_layout.addLayout(info_layout, 3)

            name_layout = QVBoxLayout()
            info_layout.addLayout(name_layout, 1)

            if liste[x][2] == "t":
                label2 = QLabel(f"{info_liste[x][0]} | {liste[x][0]}")
            elif liste[x][2] == "z":
                label2 = QLabel(f"Zubehoer | {liste[x][0]}")
            else:
                label2 = QLabel()

            name_layout.addWidget(label2)

            desc_layout = QVBoxLayout()
            info_layout.addLayout(desc_layout, 4)


            ps = QLabel(f"PS: {info_liste[x][2]}")
            km = QLabel(f"Km/h: {info_liste[x][3]}")
            baujahr = QLabel(f"Baujahr: {info_liste[x][5]}")

            desc_layout.addWidget(ps)
            desc_layout.addWidget(km)
            desc_layout.addWidget(baujahr)

            value_layout = QVBoxLayout()
            inner_layout.addLayout(value_layout, 3)

            kaufen = QPushButton("Kaufen")

            self.buttons[x] = kaufen
            kaufen.clicked.connect(self.make_button_click_handler(str(liste[x][0])))

            if liste[x][2] == "t":
                label6 = QLabel(locale.currency(int(info_liste[x][4]), grouping=True))
            elif liste[x][2] == "z":
                label6 = QLabel(locale.currency(int(info_liste[x][1]), grouping=True))
            else:
                label6 = QLabel()


            value_layout.addWidget(kaufen)
            value_layout.addWidget(label6)
            value_layout.setAlignment(label6, QtCore.Qt.AlignHCenter)


            layout.addWidget(new_widget)  # widget dem container hinzufügen

            # erstellten Container einfügen in QScrollArea

        scroll_area.setWidget(content_widget)

    def make_button_click_handler(self, label):
        def button_click_handler():
            if label is not None:
                text = label
                print(text)
                Helper.ProductHandler.set_current_product(text)
                switches.switch_to.product(self)
            else:
                print("Label ist None")

        return button_click_handler






    # ### Löschen alle Einträge, in den User Suchinformation darauf geschrieben haben
    def empty_search_info(self):

        self.horizontalSlider_leistung.setValue(0)
        self.horizontalSlider_km.setValue(0)
        self.baujahr_spinBox.setValue(1900)
        self.comboBox_hersteller.setCurrentText("")
        self.typ_comboBox.setCurrentText("")

        self.setup_waren_ui() # ### Idee ist, alle Item wieder anzeigen, funktioniert aber noch nicht

    # ########## Alle Informationen zurückgeben, die User bereits eingetragen hat
    def confirm_search_info(self):
        print("Button click!")
        # ###print("Preis: ", self.horizontalSlider_preis.value())  # get the value of Preis
        print("Zustand: ", self.comboBox_zustand.currentText())  # get the value of Zustand
        print("Leistung: ", self.horizontalSlider_leistung.value())  # get the value of Leistung
        print("Km/h: ", self.horizontalSlider_km.value())  # get the value of Leistung
        print("Hersteller: ", self.comboBox_hersteller.currentText())  # get the value of Hersteller
        print("Typ: ", self.typ_comboBox.currentText())  # get the value of Typ
        print("Baujahr: ", self.baujahr_spinBox.value())  # get value of Baujahr SpinBox
        # ### print("Auf Lager: ", self.auf_lager_spinBox.value())  # get value of Lager SpinBox

    def confirm_suchfeld_info(self):
        such_Inhalt = self.Lineedit_suchfeld.text()
        such_Inhalt_lower = such_Inhalt.lower()
        self.filtereddatalist = []

        for index in range(len(self.datalist)):
            for item in self.datalist[index]:
                if such_Inhalt_lower in item.lower():       # ### string in string suchen
                    self.filtereddatalist.append(self.datalist[index])

        self.setup_waren_ui()

    def confirm_suchfeld_info_with_enter(self):
        such_Inhalt = self.Lineedit_suchfeld.text()
        such_Inhalt_lower = such_Inhalt.lower()
        self.filtereddatalist = []

        for index in range(len(self.datalist)):
            for item in self.datalist[index]:
                if such_Inhalt_lower in item.lower():       # ### string in string suchen
                    self.filtereddatalist.append(self.datalist[index])

        self.setup_waren_ui()
