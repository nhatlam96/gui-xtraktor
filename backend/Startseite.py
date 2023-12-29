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
        print(self.traktor_infos)

        self.traktor_filter_Liste = self.get_filtered_list()
        self.traktor_filter_infos = Helper2.load.product_info(self, self.traktor_filter_Liste)

        self.traktor_sorted_Liste = self.traktor_filter_Liste
        self.traktor_sorted_infos = Helper2.load.product_info(self, self.traktor_sorted_Liste)

        self.hersteller_Liste = Helper4.load.hersteller_dict().keys()
        self.model_Liste = Helper4.load.get_all_model()


        # ERST NACH TRAKTOREN MACHEN
        """self.zubehoer_Liste = Helper2.load.all_zubehoer_data(self)
        self.zubehoer_infos = Helper2.load.product_info(self, self.zubehoer_Liste)
        self.zubehoer_filter_Liste = Helper2.load.all_zubehoer_data(self)
        self.zubehoer_filter_infos = Helper2.load.product_info(self, self.zubehoer_filter_Liste)"""

        # Signale Filter
        self.pushButton_suchen.clicked.connect(self.confirm_suchfeld_info)
        self.comboBox_hersteller.currentTextChanged.connect(lambda value: self.filter_changed_hersteller(value))
        self.typ_comboBox.currentTextChanged.connect(lambda value: self.filter_changed_typ(value))
        self.baujahr_spinBox.valueChanged.connect(lambda value: self.filter_changed_baujahr(value))
        self.horizontalSlider_km.valueChanged.connect(lambda value: self.filter_changed_km(value))
        self.horizontalSlider_leistung.valueChanged.connect(lambda value: self.filter_changed_leistung(value))
        self.min_preis.valueChanged.connect(lambda value: self.filter_changed_minPreis(value))
        self.max_preis.valueChanged.connect(lambda value: self.filter_changed_maxPreis(value))
        self.bufferleer_button.clicked.connect(self.empty_search_info)
        self.such_infor_commit.clicked.connect(self.confirm_search_info)

        # Signale UI
        self.sort_comboBox.currentTextChanged.connect(lambda value: self.get_sorted_list(value))


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
        self.sell_Button.clicked.connect(lambda: switches.switch_to.Inventar(self))
        self.sort_comboBox.blockSignals(True)
        self.sort_comboBox.clear()
        self.sort_comboBox.addItems([""])
        self.sort_comboBox.addItems(["Höchster Preis zuerst", "Niedrigster Preis zuerst"])
        self.sort_comboBox.blockSignals(False)



        self.load_filter_ui()


    def load_filter_ui(self):


        # Suchfeld -> bitte button zum Sortieren hinzufügen
        #self.Lineedit_suchfeld.editingFinished.connect(self.confirm_suchfeld_info_with_enter)  # press "enter" to finish
        # self.lineEdit.returnPressed()           # return content if you press "enter"

        # Hersteller
        self.comboBox_hersteller.blockSignals(True)
        self.comboBox_hersteller.addItem("")
        self.comboBox_hersteller.addItems(self.hersteller_Liste)
        self.comboBox_hersteller.blockSignals(False)

        # Typ
        help = self.typ_comboBox.currentText()
        self.typ_comboBox.blockSignals(True)
        self.typ_comboBox.clear()
        self.typ_comboBox.addItem("")
        self.typ_comboBox.addItems(self.model_Liste)
        self.typ_comboBox.setCurrentText(help)
        self.typ_comboBox.blockSignals(False)

        # Baujahr
        self.baujahr_spinBox.blockSignals(True)
        self.baujahr_spinBox.setMinimum(1900)
        self.baujahr_spinBox.setMaximum(2023)
        self.baujahr_spinBox.blockSignals(False)




    def filter_changed_hersteller(self, value):
        Helper4.FilterHandler.set_Filter(her=value)
        self.model_Liste = Helper4.load.get_model(value)
        self.typ_comboBox.setCurrentText("")
        self.typ_comboBox.blockSignals(True)  # connect unterbrechen
        self.typ_comboBox.clear()
        self.typ_comboBox.addItem("")
        self.typ_comboBox.addItems(self.model_Liste)
        self.typ_comboBox.blockSignals(False)
        print("HERSTELLER")


    def filter_changed_typ(self, value):
        Helper4.FilterHandler.set_Filter(typ=value)
        print("TYP")

    def filter_changed_baujahr(self, value):
        Helper4.FilterHandler.set_Filter(bau=value)
        print("baujahr")

    def filter_changed_leistung(self, value):
        Helper4.FilterHandler.set_Filter(lei=value)
        self.leistung_anzeigt.setText(f"Aktuelle Wert: {value}")
        print("leistung")

    def filter_changed_km(self, value):
        Helper4.FilterHandler.set_Filter(ges=value)
        self.km_anzeigt.setText(f"Aktuelle Wert: {value}")
        print("kmh")

    def filter_changed_minPreis(self, value):
        Helper4.FilterHandler.set_Filter(pre_min=value)
        print("minPreis")

    def filter_changed_maxPreis(self, value):
        Helper4.FilterHandler.set_Filter(pre_max=value)
        print("maxPreis")

    def setup_waren_ui(self):

        scroll_area = self.findChild(QScrollArea, "scrollArea")
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        print("ZONE BETRETEN")
        liste = self.traktor_sorted_Liste
        info_liste = self.traktor_sorted_infos

        print(liste)
        print(info_liste)

        print("ZONE VERLASSEN")



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
                Helper.ProductHandler.set_current_product(text)
                switches.switch_to.product(self)
            else:
                print("Label ist None")

        return button_click_handler


    def get_filtered_list(self):

        filtered_list = []

        Filter = Helper4.FilterHandler.get_Filter()
        print("NEUE FILTER")
        print(Filter)

        her = Filter['Hersteller'] if Filter['Hersteller'] != '' else None
        typ = Filter['Typ'] if Filter['Typ'] != '' else None
        bau = Filter['Baujahr'] if Filter['Baujahr'] != '' else None
        lei = Filter['Leistung'] if Filter['Leistung'] != '' else None
        ges = Filter['Geschwindigkeit'] if Filter['Geschwindigkeit'] != '' else None
        min_pre = Filter['Preis'][0] if Filter['Preis'][0] != '' else None
        max_pre = Filter['Preis'][1] if Filter['Preis'][1] != '' else None

        for x in range(len(self.traktor_infos)):
            if her is not None:
                if self.traktor_infos[x][0] != her:
                    continue

            if typ is not None:
                if self.traktor_infos[x][1] != typ:
                    continue

            if max_pre is not None:
                if int(self.traktor_infos[x][4]) > int(max_pre):
                    continue

            if min_pre is not None:
                if int(self.traktor_infos[x][4]) < int(min_pre):
                    continue

            if ges is not None:
                if int(self.traktor_infos[x][3]) < int(ges):
                    continue

            if lei is not None:
                if int(self.traktor_infos[x][2]) < int(lei):
                    continue

            if bau is not None:
                if int(self.traktor_infos[x][5]) < int(bau):
                    continue

            filtered_list.append(self.traktor_Liste[x])


        print(filtered_list)

        return filtered_list


    def get_sorted_list(self, value):

        sorted_list = []

        sort = value if value is not None else ''

        print("NEUER SORT")
        print(sort)

        liste = self.get_filtered_list()
        liste_infos = Helper2.load.product_info(self, liste)

        # zip kombiniert beide listen damit die beiden zusammen bleiben
        neue_liste = list(zip(liste, liste_infos))

        if sort == "Höchster Preis zuerst":
            # sortiert nach preis
            sorted_combined = sorted(neue_liste, key=lambda x: int(x[1][4]), reverse=True)

            # nur die liste mit primärschlüssel ist nötig
            sorted_list = [item[0] for item in sorted_combined]

            print("SORT!!!")
            print(sorted_list)

            self.traktor_sorted_Liste = sorted_list
            self.traktor_sorted_infos = Helper2.load.product_info(self, self.traktor_sorted_Liste)

        if sort == "Niedrigster Preis zuerst":
            # sortiert nach preis
            sorted_combined = sorted(neue_liste, key=lambda x: int(x[1][4]), reverse=False)

            # nur die liste mit primärschlüssel ist nötig
            sorted_list = [item[0] for item in sorted_combined]

            print("SORT!!!")
            print(sorted_list)

            self.traktor_sorted_Liste = sorted_list
            self.traktor_sorted_infos = Helper2.load.product_info(self, self.traktor_sorted_Liste)

        if not sort:
            self.traktor_sorted_Liste = self.traktor_filter_Liste
            self.traktor_sorted_infos = Helper2.load.product_info(self, self.traktor_sorted_Liste)



        self.setup_waren_ui()

        print("UI GELADEN")




    def empty_search_info(self):

        self.comboBox_hersteller.setCurrentText("")
        self.typ_comboBox.setCurrentText("")
        self.baujahr_spinBox.setValue(1900)
        self.horizontalSlider_leistung.setValue(0)
        self.horizontalSlider_km.setValue(0)
        self.min_preis.setValue(0)
        self.max_preis.setValue(300000)

        Helper4.FilterHandler.clear_Filter()

        self.load_ui()

        self.setup_waren_ui()


    def confirm_search_info(self):

        self.traktor_filter_Liste = self.get_filtered_list()
        self.traktor_filter_infos = Helper2.load.product_info(self, self.traktor_filter_Liste)
        self.get_sorted_list("")
        self.setup_waren_ui()
        self.load_ui()


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
        self.setup_waren_ui()
        self.load_ui()
