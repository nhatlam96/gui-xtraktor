import csv
import os
import os.path
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import switches
import Helper
import Helper2

csv_path = os.path.join("..", "resources", "csv")
image_path = os.path.join("..", "resources", "Traktoren")
zubehoer_path = os.path.join("..", "resources", "Zubehör")

class Startseite(QMainWindow):

    def __init__(self):
        super().__init__()  # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Startseite.ui"), self)

        Helper2.load.complete_header(self)

        # Buttonaktionen in liste von dyn. Layout
        self.buttons = {}
        # ### original list of list information Trator
        self.datalist = self.load_list_data(os.path.join(csv_path, "mobile Arbeitsmaschinen Landwirtschaft.csv") )
        # ### goal: emptying original data list to "filtern" content
        self.filtereddatalist = self.load_list_data(os.path.join(csv_path, "mobile Arbeitsmaschinen Landwirtschaft.csv"))
        self.zubehordatalist = self.load_list_data(os.path.join(csv_path, "Zubehör.csv"))
        print(len(self.zubehordatalist))
        self.zubehorfilter = []

        self.listImage = self.load_list_image()
        print(self.listImage)

        # ### Aktuelle ausgewaehlte Produkte abspeichern (fuer Produkt Filter dienen)

        self.ausgewaehlteProdukt = {}

        self.ausgewaehlteProdukt_Lange = len(self.ausgewaehlteProdukt)

        # ### Zurücksetzen Button und Bestätigen Button deklarieren
        self.bufferleer_button.clicked.connect(self.empty_search_info)
        self.such_infor_commit.clicked.connect(self.confirm_search_info)

        # ### Such_pushButton in Suchfeld einstellen

        self.pushButton_suchen.clicked.connect(self.confirm_suchfeld_info)
        self.Lineedit_suchfeld.editingFinished.connect(self.confirm_suchfeld_info_with_enter)  # press "enter" to finish
        # self.lineEdit.returnPressed()           # return content if you press "enter"

        self.setup_waren_ui() # ### Eine Frage, Wenn ich diese Code nach oben schiebe, funktioniert das nicht mehr, Warum?

        # ### Ereignisse bei den QSlider von Preis, Leistung und Kilometer umgehen und Werte
        # ### auf die entsprechenden Label anzuzeigen

        self.horizontalSlider_km.valueChanged.connect(self.km_changed)
        self.horizontalSlider_leistung.valueChanged.connect(self.leistung_changed)

        # ############ Spin Box bei dem Lager und Baujahr einstellen

        self.baujahr_spinBox.setMinimum(1900)
        self.baujahr_spinBox.setMaximum(2023)
        self.baujahr_spinBox.valueChanged.connect(self.filter_baujahr_changed)

        # ########### Umgehen mit dem Ereignis, wenn User Value des Baujahr geaendert wurde

        # self.uic.baujahr_spinBox.valueChanged.connect(self.Baujahr_Value_aendern)

        # ########## Fügen Artikel in ComboBox hinzu

        self.comboBox_hersteller.addItem("")
        self.comboBox_hersteller.addItems(self.add_hersteller())
        self.comboBox_hersteller.currentTextChanged.connect(lambda value: self.filter_changed_hersteller(value))

        self.typ_comboBox.addItems(["Traktor", "Zubehör"])
        self.typ_comboBox.currentTextChanged.connect(self.filter_changed_typ)

        self.horizontalSlider_leistung.valueChanged.connect(self.filter_changed_leistung)
        self.horizontalSlider_km.valueChanged.connect(self.filter_changed_km)

        # ########## Preis Eintrage umgehen
        self.min_preis.addItems(self.add_min_preis())   # ### allow only adding string
        self.max_preis.addItems(self.add_max_preis())
        self.min_preis.currentTextChanged.connect(lambda currentValue: self.filter_changed_minPreis(currentValue))
        self.max_preis.currentTextChanged.connect(lambda currentValue: self.filter_changed_maxPreis(currentValue))
        self.sell_Button.clicked.connect(lambda: switches.switch_to.Inventar(self))

        print(self.buttons)
        self.show()

    def filter_baujahr_changed(self):
        self.filtereddatalist = []
        intUmwandlung = int(self.baujahr_value_nehmen())

        for index in range(len(self.datalist)):
            if intUmwandlung == int(self.datalist[index][5]):
                self.filtereddatalist.append(self.datalist[index])

        self.setup_waren_ui()

    def filter_changed_minPreis(self, currentValue):

        self.filtereddatalist = []
        intUmwandlung = int(currentValue)
        for index in range(len(self.datalist)):
            if intUmwandlung <= int(self.datalist[index][4]):
                self.filtereddatalist.append(self.datalist[index])
        self.setup_waren_ui()

    def filter_changed_maxPreis(self, currentValue):

        self.filtereddatalist = []

        intUmwandlung = int(currentValue)
        for index in range(len(self.datalist)):
            if intUmwandlung >= int(self.datalist[index][4]) or int(self.datalist[index][4]) > int(self.get_minPreis()):
                self.filtereddatalist.append(self.datalist[index])
        self.setup_waren_ui()

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

    def get_minPreis(self):
        return self.min_preis.currentText()

    def get_maxPreis(self):
        return  self.max_preis.currentText()

    def filter_changed_km(self, currentKm):
        self.filtereddatalist = []
        intUmwandlung_km = int(currentKm)

        for index in range(len(self.datalist)):
            if intUmwandlung_km >= int(self.datalist[index][3]):
                self.filtereddatalist.append(self.datalist[index])

        self.setup_waren_ui()

    def filter_changed_leistung(self, currentLeistung):
        self.filtereddatalist = []
        intUmwandlung_currentLeistung = int(currentLeistung)

        if (self.ausgewaehlteProdukt_Lange == 0):
            for index in range(len(self.datalist)):
                intUmwandlung_datalist = int(self.datalist[index][2])
                if intUmwandlung_currentLeistung >= intUmwandlung_datalist:
                    self.filtereddatalist.append(self.datalist[index])
                    self.ausgewaehlteProdukt.add(self.datalist[index])

        else:
            new_list = list(self.ausgewaehlteProdukt)
            for index in range(self.ausgewaehlteProdukt_Lange):
                intUmwandlung_datalist = int(new_list[index][2])
                if intUmwandlung_currentLeistung >= intUmwandlung_datalist:
                    self.filtereddatalist.append(new_list[index])

        self.setup_waren_ui()

    # ########## Typ Eintrag muss noch einmal diskutieren, weil ich ("Tu") nicht weiß, ob es um Verkehr oder Zubehör geht
    # ######### danke
    def filter_changed_typ(self, currentTyp):

        if (currentTyp == "Zubehör"):
            self.zubehor_setup()
        else: self.setup_waren_ui()

    def filter_changed_hersteller(self, currentHersteller):

        print(f"hersteller {currentHersteller}")
        self.filtereddatalist = []

        for x in range(len(self.datalist)):
            if self.datalist[x][0] == currentHersteller:
                self.filtereddatalist.append(self.datalist[x])

        print(self.filtereddatalist)
        self.setup_waren_ui()

    # ########## aktuelle Value von Baujahr aufnehmen
    def baujahr_value_nehmen(self):
        return self.baujahr_spinBox.value()

    # ############ aktuelle Value von Km aufnehmen
    def km_value_nehmen(self):
        return self.horizontalSlider_km.value()

    # ############ aktuelle Value von Leistung aufnehmen
    def leistung_value_nehmen(self):
        return self.horizontalSlider_leistung.value()

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

    def load_list_data(self, csvListpath):

        main_list = []
        csv_list_path = csvListpath # os.path.join(csv_path, "mobile Arbeitsmaschinen Landwirtschaft.csv")

        with open(csv_list_path, "r") as file:
            csv_file_reader = csv.reader(file)      # list von CSV file erstellen
            next(csv_file_reader)  # Auf Header Info springen
            vermitteln_to_list = list(csv_file_reader)  # csv reader file in List vermitteln

            for index in range(len(vermitteln_to_list)):
                main_list.append(vermitteln_to_list[index])

        return main_list

    def load_list_image(self):
        imageList = []
        validImage_extension = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

        for file in os.listdir(os.path.join("..", "resources", "Traktoren")):
            get_extendsion = os.path.splitext(file)[1]

            if get_extendsion.lower() in validImage_extension:
                imageList.append(os.path.join(image_path, file))
        print(imageList)
        return imageList

    # ########## Funktion für Dynamic aufladen
    def setup_waren_ui(self):

        scroll_area = self.findChild(QScrollArea, "scrollArea")
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        data_list = self.filtereddatalist   # ### get only content list of Item if user find Traktor details

        imageList = self.load_list_image()
        for index in range(len(data_list)):
            new_widget = QWidget()
            inner_layout = QHBoxLayout(new_widget)

            inner_layout1 = QVBoxLayout()
            herstell_label = QLabel("Hersteller: " + str(data_list[index][0]))
            modell_label = QLabel("Modell: " + str(data_list[index][1]))
            inner_layout1.addWidget(herstell_label, stretch = 1)
            inner_layout1.addWidget(modell_label, stretch = 1)
            # ### CSS for label
            herstell_label.setStyleSheet("color: white; font-weight: 500; text-align: center; padding: 5px;")
            modell_label.setStyleSheet("color: white; font-weight: 500; text-align: center; padding: 5px;")

            inner_layout2 = QVBoxLayout()
            preis = QLabel("Preis: " + str(data_list[index][4]) + " €")
            kaufen = QPushButton("Kaufen")
            kaufen.setStyleSheet("""
                QPushButton {
                    color: white;
                    background-color: rgb(230, 126, 34);
                    max-width: 200px;
                }
                QPushButton:hover {
                    cursor: pointer;
                    opacity: 0.8;
                }
            """)
            preis.setStyleSheet("color: white; font-weight:500; text-align: center; padding:5px")
            self.buttons[index] = kaufen
            kaufen.clicked.connect(self.make_button_click_handler(str(data_list[index][1])))

            inner_layout2.addWidget(preis, stretch = 1)
            inner_layout2.addWidget(kaufen, stretch = 1)

            inner_layout3 = QHBoxLayout()
            ps = QLabel("PS: " + str(data_list[index][2]))
            ps.setStyleSheet("color: white; font-weight:500; text-align: center; padding:5px")
            leistung = QLabel("Leistung: " + str(data_list[index][2]))
            leistung.setStyleSheet("color: white; font-weight:500; text-align: center; padding:5px")
            km = QLabel("Km/h: " + str(data_list[index][3]))
            km.setStyleSheet("color: white; font-weight:500; text-align: center; padding:5px")
            inner_layout3.addWidget(ps, stretch = 1)
            inner_layout3.addWidget(leistung, stretch = 1)
            inner_layout3.addWidget(km, stretch = 1)

            inner_layout4 = QHBoxLayout()
            inner_layout4.addLayout(inner_layout1, stretch = 1)
            inner_layout4.addLayout(inner_layout2, stretch = 1)

            inner_layout5 = QVBoxLayout()
            inner_layout5.addLayout(inner_layout4, stretch = 1)
            inner_layout5.addLayout(inner_layout3, stretch = 1)

            inner_layout6 = QHBoxLayout()
            bild_label = QLabel()
            picture = QPixmap(imageList[index])
            scale_picture = picture.scaled(400,400,Qt.KeepAspectRatio)
            bild_label.setPixmap(scale_picture)
            bild_label.setStyleSheet("""
                QLabel{
                    max-width: 400px;
                    max-height: 400px;
                }
            """)
            inner_layout6.addWidget(bild_label, stretch = 1)
            inner_layout6.addLayout(inner_layout5, stretch = 1)

            inner_layout.addLayout(inner_layout6)
            layout.addWidget(new_widget)

        scroll_area.setWidget(content_widget)

    def zubehor_setup(self):

        scroll_area = self.findChild(QScrollArea, "scrollArea")
        inhalt_layout = QWidget()
        layout = QVBoxLayout(inhalt_layout)

        zubehorList = self.zubehordatalist

        for index in range(len(zubehorList)):
            innerWidget = QWidget()
            inner_layout = QHBoxLayout(innerWidget)

            layout1 = QHBoxLayout()
            name_label = QLabel("Zubehör: " + str(zubehorList[index][0]))
            preis_label = QLabel("Preis: " + str(zubehorList[index][1]))
            layout1.addWidget(name_label, stretch = 1)
            layout1.addWidget(preis_label, stretch = 1)

            layout2 = QHBoxLayout()
            hersteller = QLabel("Hersteller: " + str(zubehorList[index][3]))
            bestand = QLabel("Bestand: " + str(zubehorList[index][2]))
            layout2.addWidget(hersteller, stretch = 1)
            layout2.addWidget(bestand, stretch = 1)

            layout3 = QVBoxLayout()
            layout3.addLayout(layout1, stretch = 1)
            layout3.addLayout(layout2, stretch = 1)

            layout4 = QHBoxLayout()
            bilder = QLabel("test")
            layout4.addWidget(bilder, stretch = 1)
            layout4.addLayout(layout3, stretch = 1)

            inner_layout.addLayout(layout4)
            layout.addWidget(innerWidget)

        scroll_area.setWidget(inhalt_layout)

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
