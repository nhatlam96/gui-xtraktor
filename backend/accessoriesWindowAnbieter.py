import csv
import locale
import os.path

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Helper
import Helper2
import Helper_Accounts

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class accessoriesWindowAnbieter(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join("..", "frontend", "accessoriesWindowAnbieter.ui"), self)

        # übergabeparameter
        platzhalter = Helper.AccessoriesHandler.get_current_acc()

        product = Helper2.load.product_info(self, [[platzhalter, 1, "z"]])[0]

        acc = Helper_Accounts.UserHandler.get_current_user()
        hers_list = self.load_hers(product)  # kompatible Traktoren
        self.anz = 0

        # Währungsumgebung laden
        Helper2.conf.locale_setup(self)

        # Produktseite laden
        self.load_ui(product, acc, hers_list)
        self.load_lager(product)
        self.load_pic(product)

        # Aktionen
        self.buy_Button.clicked.connect(lambda: self.buy(product[0], self.anz, "z"))
        self.spinBox.valueChanged.connect(lambda value: self.set_anz(value))

        self.show()

    def load_ui(self, product, user, hers_list):
        Helper2.replace.text(product[0], self.findChild(QLabel, "name_label"))
        Helper2.replace.text(locale.currency(int(product[1]), grouping=True), self.findChild(QLabel, "preis_status"))
        Helper2.replace.text(f"Budget:  {locale.currency(int(user[2]), grouping=True)}",
                             self.findChild(QLabel, "budget_label"))
        Helper2.replace.text(hers_list, self.findChild(QLabel, "comp_label"))
        Helper2.load.complete_header(self)

    def set_anz(self, value):
        self.anz = value

    def load_hers(self, product):
        conv_text = ", ".join(product[3:])
        return conv_text

    def load_lager(self, row):
        if int(row[2]) > 0:
            Helper2.replace.img(os.path.join(ICON_PATH, r"check.svg"), self.findChild(QLabel, "bestand_icon"))
            return True
        else:
            Helper2.replace.img(os.path.join(ICON_PATH, r"cross.svg"), self.findChild(QLabel, "bestand_icon"))
            self.buy_Button.setDisabled(True)
            Helper2.replace.text("ausverkauft", self.findChild(QPushButton, "buy_Button"))
            return False

    def load_pic(self, row):
        gesucht = row[0]
        pfad = os.path.join(PIC_PATH, r"Zubehör")

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

    def calc_wert(self, product, loss, value):
        preis = int(product.replace(".", ""))
        new_value = -(value * (preis * loss / 100)) if (value * (preis * loss / 100)) < preis else -preis
        Helper2.replace.text(locale.currency(new_value, grouping=True), self.findChild(QLabel, "wert_status"))
        # Zinseszinzprinzip:
        # Endbetrag = Kapital×(Zinsesrate) hoch Jahresanzahl

        Helper2.replace.text(locale.currency(new_value, grouping=True),
                             self.findChild(QLabel, "wert_status"),
                             )

    def buy(self, model, anz, typ):  # weiterleiten an warenkorb mit parameter (user name, product modell)
        if anz > 0:
            Helper.show_toast(f"Sie haben {anz}x {model} dem Warenkorb hinzugefügt.", QMessageBox.Information,
                              QMessageBox.Ok, 2500)
            print("aufruf buy()")
            Helper.BuyHandler.add_to_current_shoppinglist(model, anz, typ)
            self.spinBox.setValue(0)
            print(Helper.BuyHandler.get_current_shoppinglist())
