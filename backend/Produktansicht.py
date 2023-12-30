import locale
import os.path
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import Helper
import switches
import Helper2

from Vollbild_Klasse import FullScreenImage

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class ProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "ProductWindow.ui"), self)

        print("AUFRUF PRODUKT")

        # übergabeparameter
        self.product = Helper2.load.traktor_data(self, Helper.ProductHandler.current_product)
        self.loss = int(Helper2.load.loss(self.product[0]))
        self.z_list = self.load_zub()  # kompatibles Zubehoer []
        self.buttons = {}  # speichert array von buttonaktionen für dyn. layout
        self.anz = 0

        # Währungsumgebung laden
        Helper2.conf.locale_setup(self)

        # dynamisches Widget laden
        self.add_widget()

        # Produktseite laden
        self.load_ui()
        self.load_lager()
        self.load_pic(self.product)

        # Aktionen
        self.buy_Button.clicked.connect(lambda: self.buy(self.product[1], self.anz))
        self.wert_spinBox.valueChanged.connect(lambda value: self.calc_wert(value))
        self.anz_spinBox.valueChanged.connect(lambda value: self.set_anz(value))

        # Mausevent mit Bild verknüpfen
        picture_label = self.findChild(QLabel, "picture")
        picture_label.mousePressEvent = lambda event: self.show_fullscreen(event, picture_label.pixmap())

        self.show()


    def closeEvent(self, event):
        print("Window is closing")
        switches.WindowHandler.release_window(ProductWindow)
        super().closeEvent(event)  # Fenster wird wirklich geschlossen

    @staticmethod
    def show_fullscreen(event, pixmap):
        FullScreenImage.show_fullscreen(event, pixmap)


    def load_ui(self):
        Helper2.conf.locale_setup(self)
        Helper2.replace.text(f"{self.product[0]} - {self.product[1]}",
                             self.findChild(QLabel, "name_label"))
        Helper2.replace.text(locale.currency(int(self.product[4]), grouping=True),
                             self.findChild(QLabel, "preis_status"))
        Helper2.replace.text(self.product[2], self.findChild(QLabel, "ps_status"))
        Helper2.replace.text(self.product[3], self.findChild(QLabel, "kmh_status"))
        Helper2.replace.text(self.product[5], self.findChild(QLabel, "baujahr_status"))
        Helper2.load.complete_header(self)


    def set_anz(self, value):
        self.anz = value
        self.calc_preis(value)

    def calc_preis(self, value):
        preis = int(self.product[4])
        new_value = preis * value
        Helper2.replace.text(locale.currency(new_value, grouping=True), self.findChild(QLabel, "ges_status"))

    def calc_wert(self, jahre):
        normalPreis = int(self.product[4])
        verlustRate = (100 - self.loss) / 100
        new_value = int(normalPreis * (verlustRate ** jahre)) # ** -> Potenz
        Helper2.replace.text(locale.currency(new_value - normalPreis , grouping=True), self.findChild(QLabel, "wert_status"))
        Helper2.replace.text(locale.currency(new_value, grouping=True), self.findChild(QLabel, "rest_status"))




    def load_zub(self):
        pfad = os.path.join(CSV_PATH, r"Zubehör.csv")

        with open(pfad, mode="r") as file:
            csv_reader = csv.reader(file)
            data_list = []

            for row in csv_reader:
                for column in row:
                    if self.product[0] == column:
                        data_list.append(row)
                        break

            return data_list


    def load_lager(self):
        if int(self.product[6]) > 0:
            Helper2.replace.img(os.path.join(ICON_PATH, r"check.svg"),self.findChild(QLabel, "bestand_icon"))
            return True
        else:
            Helper2.replace.img(os.path.join(ICON_PATH, r"cross.svg"),self.findChild(QLabel, "bestand_icon"))
            self.buy_Button.setDisabled(True)
            Helper2.replace.text("ausverkauft", self.findChild(QPushButton, "buy_Button"))
            return False

    def load_pic(self, row):
        gesucht = str(row[1])
        pfad = os.path.join(PIC_PATH, r"Traktoren")

        for dateiname in os.listdir(pfad):
            if gesucht in dateiname:
                voll_pfad = os.path.join(pfad, dateiname)
                Helper2.replace.img(voll_pfad, self.findChild(QLabel, "picture"))

    def load_zpic(self, name):
        gesucht = name
        pfad = os.path.join(PIC_PATH, r"Zubehör")

        for dateiname in os.listdir(pfad):
            if gesucht in dateiname:
                voll_pfad = os.path.join(pfad, dateiname)
                pixmap = QPixmap(voll_pfad)
                scaled_pixmap = pixmap.scaled(64, 64)
                return scaled_pixmap

    def load_acc(self, user):
        pfad = os.path.join(CSV_PATH, r"Accounts.csv")

        with open(pfad, mode="r") as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                if row[0] == user:
                    return row

    def add_widget(self):

        zusatz = self.z_list

        # dynamisches Layout laden
        scroll_area = self.findChild(QScrollArea, "dyn_scrollarea")

        # neues Widget als Container für einzelne Widgets
        content_widget = QWidget()

        # QHBoxLayout erstellen für Container
        layout = QHBoxLayout(content_widget)

        for x in range(len(zusatz)):
            new_widget = QWidget()
            inner_layout = QVBoxLayout(new_widget)  # v-layout für widget

            label1 = QLabel(zusatz[x][0])
            label2 = QLabel()
            label2.setPixmap(self.load_zpic(zusatz[x][0]))
            label3 = QLabel(locale.currency(int(zusatz[x][1]), grouping=True))

            button = QPushButton("Mehr info")
            self.buttons[x] = button

            button.clicked.connect(self.make_button_click_handler(label1))

            inner_layout.addWidget(label1)
            inner_layout.addWidget(label2)
            inner_layout.addWidget(label3)
            inner_layout.addWidget(button)

            layout.addWidget(new_widget)  # widget dem container hinzufuegen

            # erstellten Container einfuegen in QScrollArea
            scroll_area.setWidget(content_widget)

    def make_button_click_handler(self, label):
        def button_click_handler():
            if label is not None:
                Helper.AccessoriesHandler.set_current_acc(label.text())
                switches.switch_to.accessories(self)
                #switches.switch_to.accessories_Anbieter(self)
            else:
                print("Label ist None")

        return button_click_handler



    def buy(self, model, anz):
        if anz > 0:
            Helper.show_toast(f"Sie haben {anz}x {model} dem Warenkorb hinzugefügt.",
                              QMessageBox.Information,
                              QMessageBox.Ok, 2500)
            print("aufruf buy()")
            Helper.BuyHandler.add_to_current_shoppinglist(model, anz, "t")
            self.anz_spinBox.setValue(0)
            print(Helper.BuyHandler.get_current_shoppinglist())
