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


class accessoriesWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join("..", "frontend", "accessoriesWindow.ui"), self)

        print("AUFRUF ACCESSORIES")

        # übergabeparameter
        platzhalter = Helper.AccessoriesHandler.get_current_acc()
        print(platzhalter)
        self.product = Helper2.load.product_info(self,[[platzhalter, 1, "z"]])[0]
        self.acc = Helper_Accounts.UserHandler.get_current_user()
        self.hers_list = self.load_hers()  # kompatible Traktoren
        self.anz = 0
        self.loss = int(Helper2.load.loss("Zusatz"))
        self.ges_preis = 0


        # Währungsumgebung laden
        Helper2.conf.locale_setup(self)

        # Produktseite laden
        self.load_ui()
        self.load_lager()
        self.load_pic()

        # Aktionen
        self.buy_Button.clicked.connect(lambda: self.buy(self.anz, "z"))
        self.anz_spinBox.valueChanged.connect(lambda value: self.set_anz(value))
        self.wert_spinBox.valueChanged.connect(lambda value: self.calc_wert(value))

        self.show()


    def load_ui(self):
        Helper2.replace.text(self.product[0], self.findChild(QLabel, "name_label"))
        Helper2.replace.text(locale.currency(int(self.product[1]), grouping=True), self.findChild(QLabel, "preis_status"))
        Helper2.replace.text(f"Budget:  {locale.currency(int(self.acc[2]), grouping=True)}", self.findChild(QLabel, "budget_label"))
        Helper2.replace.text(self.hers_list, self.findChild(QLabel, "comp_label"))
        Helper2.load.complete_header(self)

    def set_anz(self, value):
        self.anz = value
        self.calc_preis(value)

    def load_hers(self):
        conv_text = ", ".join(self.product[3:])
        return conv_text

    def load_lager(self):
        if int(self.product[2]) > 0:
            Helper2.replace.img(os.path.join(ICON_PATH, r"check.svg"), self.findChild(QLabel, "bestand_icon"))
            return True
        else:
            Helper2.replace.img(os.path.join(ICON_PATH, r"cross.svg"), self.findChild(QLabel, "bestand_icon"))
            self.buy_Button.setDisabled(True)
            Helper2.replace.text("ausverkauft", self.findChild(QPushButton, "buy_Button"))
            return False

    def load_pic(self):
        gesucht = self.product[0]
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

    def calc_wert(self, jahre):
        normalPreis = int(self.product[1])
        verlustRate = (100 - self.loss) / 100
        new_value = int(normalPreis * (verlustRate ** jahre))  # ** -> Potenz (Zinseszins)
        Helper2.replace.text(locale.currency(new_value - normalPreis, grouping=True),
                             self.findChild(QLabel, "wert_status"))
        Helper2.replace.text(locale.currency(new_value, grouping=True), self.findChild(QLabel, "rest_status"))


    def calc_preis(self, value):
        preis = int(self.product[1].replace(".", ""))
        new_value = preis * value
        Helper2.replace.text(locale.currency(new_value, grouping=True), self.findChild(QLabel, "ges_status"))


    def buy(self, anz, typ):
        model = self.product[0]
        if anz > 0:
            Helper.show_toast(f"Sie haben {anz}x {model} dem Warenkorb hinzugefügt.", QMessageBox.Information,
                              QMessageBox.Ok, 2500)
            Helper.BuyHandler.add_to_current_shoppinglist(model, anz, typ)
            self.anz_spinBox.setValue(0)
            print(Helper.BuyHandler.get_current_shoppinglist())
