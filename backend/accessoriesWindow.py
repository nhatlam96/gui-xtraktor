import locale
import os.path
import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic, Qt
from PyQt5.QtGui import *
import Helper
import Helper2

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class accessoriesWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join("..", "frontend", "accessoriesWindow.ui"), self)

        # Simulierte übergabeparameter
        platzhalter = Helper.AccessoriesHandler.get_current_acc()
        product = self.load_data(platzhalter)
        acc_platzhalter = "Sieglinde"
        acc = self.load_acc(acc_platzhalter)
        hers_list = self.load_hers(product)  # kompatible Traktoren

        # Währungsumgebung laden
        Helper2.conf.locale_setup(self)

        # Produktseite laden
        self.load_ui(product, acc, hers_list)
        self.load_lager(product)
        self.load_pic(product)

        # Aktionen
        self.buy_Button.clicked.connect(lambda: self.buy(product[0], 1, "z"))

        self.show()


    def load_ui(self, product, user, hers_list):
        Helper2.replace.text(self, product[0], self.findChild(QLabel, "name_label"))
        Helper2.replace.text(self, locale.currency(int(product[1]), grouping=True), self.findChild(QLabel, "preis_status"))
        Helper2.replace.text(self, f"Budget:  {locale.currency(int(user[2]), grouping=True)}", self.findChild(QLabel, "budget_label"))
        Helper2.replace.text(self, hers_list, self.findChild(QLabel, "comp_label"))
        Helper2.load.complete_header(self)

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
            Helper2.replace.img(self, os.path.join(ICON_PATH, r"check.svg"), self.findChild(QLabel, "bestand_icon"))
            return True
        else:
            Helper2.replace.img(self, os.path.join(ICON_PATH, r"cross.svg"), self.findChild(QLabel, "bestand_icon"))
            self.buy_Button.setDisabled(True)
            Helper2.replace.text(self, "ausverkauft", self.findChild(QPushButton, "buy_Button"))
            return False

    def load_pic(self, row):
        gesucht = row[0]
        pfad = os.path.join(PIC_PATH, r"Zubehör")

        for dateiname in os.listdir(pfad):
            if gesucht in dateiname:
                voll_pfad = os.path.join(pfad, dateiname)
                Helper2.replace.img(self, voll_pfad, self.findChild(QLabel, "picture"))

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

    def calc_wert(self, product, loss, value):
        preis = int(product.replace(".", ""))
        new_value = -(value * (preis * loss / 100)) if (value * (preis * loss / 100)) < preis else -preis
        Helper2.replace.text(self, locale.currency(new_value, grouping=True), self.findChild(QLabel, "wert_status"))
        # Zinseszinzprinzip:
        # Endbetrag = Kapital×(Zinsesrate) hoch Jahresanzahl
        
        Helper2.replace.text(self, 
                             locale.currency(new_value, grouping=True),
                             self.findChild(QLabel, "wert_status"),
        )
    
    def buy(self, model, anz, typ):  # weiterleiten an warenkorb mit parameter (user name, product modell)
        if anz > 0:
            print("aufruf buy()")
            Helper.BuyHandler.add_to_current_shoppinglist(model, anz, typ)
            print(Helper.BuyHandler.get_current_shoppinglist())