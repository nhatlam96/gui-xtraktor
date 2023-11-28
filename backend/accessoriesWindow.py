import locale
import os.path
import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic, Qt
from PyQt5.QtGui import *
import Helper

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class accessoriesWindow(QMainWindow):

    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        accessoriesWindow_ui = uic.loadUi(os.path.join("..", "frontend", "accessoriesWindow.ui"), self)
        Helper.WindowSizeHandler.set_sizes(accessoriesWindow_ui.minimumSize(), accessoriesWindow_ui.maximumSize())

        # Simulierte übergabeparameter
        platzhalter = Helper.AccessoriesHandler.get_current_acc()
        product = self.load_data(platzhalter)
        acc_platzhalter = "Sieglinde"
        acc = self.load_acc(acc_platzhalter)
        hers_list = self.load_hers(product)  # kompatible Traktoren

        # Währungsumgebung laden
        self.locale_setup()

        # Produktseite laden
        self.load_ui(product, acc, hers_list)
        self.load_lager(product)
        self.load_pic(product)

        # Aktionen
        #self.buy_Button.clicked.connect(self.buy)
        self.shopping_Button.clicked.connect(lambda: self.change_widget("test", "Home"))
        self.acc_Button.clicked.connect(lambda: self.change_widget("test", "Home"))
        self.home_Button.clicked.connect(lambda: self.change_widget("test", "Home"))

        self.show()

    def locale_setup(self):
        locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")

    def replace_text(self, new_text, label):
        label.setText(new_text)

    def replace_img(self, image_name, label):
        pixmap = QPixmap(image_name)
        label.setPixmap(pixmap)

    def replace_icon(self, icon_name, label):
        icon = QIcon(icon_name)
        label.setIcon(icon)

    def load_ui(self, product, user, hers_list):
        self.replace_text(product[0], self.findChild(QLabel, "name_label"))
        self.replace_text(locale.currency(int(product[1]), grouping=True), self.findChild(QLabel, "preis_status"))
        self.replace_text(f"Budget:  {locale.currency(int(user[2]), grouping=True)}", self.findChild(QLabel, "budget_label"))
        self.replace_text(hers_list, self.findChild(QLabel, "comp_label"))
        self.replace_icon(os.path.join(ICON_PATH, r"home.svg"), self.findChild(QPushButton, "home_Button"))
        self.replace_icon(os.path.join(ICON_PATH, r"user.svg"), self.findChild(QPushButton, "acc_Button"))
        self.replace_icon(os.path.join(ICON_PATH, r"shopping-cart.svg"), self.findChild(QPushButton, "shopping_Button"))

    def load_data(self, placeholder):
        csv_path = os.path.join(CSV_PATH, r"Zubehör.csv")

        with open(csv_path, mode="r") as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                if row[0] == placeholder:
                    return row

    def load_hers(self, product):
        conv_text = ", ".join(product[3:])
        return conv_text

    def load_lager(self, row):
        if int(row[2]) > 0:
            self.replace_img(os.path.join(ICON_PATH, r"check.svg"), self.findChild(QLabel, "bestand_icon"))
            return True
        else:
            self.replace_img(os.path.join(ICON_PATH, r"cross.svg"), self.findChild(QLabel, "bestand_icon"))
            self.buy_Button.setDisabled(True)
            self.replace_text("ausverkauft", self.findChild(QPushButton, "buy_Button"))
            return False

    def load_pic(self, row):
        gesucht = row[0  ]
        pfad = os.path.join(PIC_PATH, r"Zubehör")

        for dateiname in os.listdir(pfad):
            if gesucht in dateiname:
                voll_pfad = os.path.join(pfad, dateiname)
                self.replace_img(voll_pfad, self.findChild(QLabel, "picture"))

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

    """ # feature muss noch überarbeitet werden

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.showFullScreen()
            self.picture.setPixmap(self.picture.pixmap().scaledToWidth(self.width()))  # Bild auf die Fensterbreite skalieren
    """

    def calc_wert(self, product, loss, value):
        preis = int(product.replace(".", ""))
        new_value = -(value * (preis * loss / 100)) if (value * (preis * loss / 100)) < preis else -preis
        self.replace_text(locale.currency(new_value, grouping=True), self.findChild(QLabel, "wert_status"))

    def buy(self, acc):  # weiterleiten an warenkorb mit parameter (user name, product modell)
        pass  # Warenkorb.ui nötig

    def change_widget(self, acc, page):  # page = wohin als nächstes
        pass

