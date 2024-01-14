import locale
import os.path

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Vollbild_Klasse import FullScreenImage

import switches
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
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)

        print("AUFRUF ACCESSORIES")

        # übergabeparameter
        model = Helper.AccessoriesHandler.get_current_acc()
        self.product = Helper2.load.product_info(self, [[model, 1, "z"]])[0]
        self.acc = Helper_Accounts.UserHandler.get_current_user()
        self.hers_list = self.load_hers()  # kompatible Traktoren
        self.loss = int(Helper2.load.loss("Zusatz"))

        # dyn. Layout Help
        self.anz = 0
        self.ges_preis = 0

        # Währungsumgebung laden
        Helper2.conf.locale_setup(self)

        # Produktseite laden
        self.load_ui()
        self.load_lager()
        self.load_pic()

        # Aktionen
        self.buy_Button.clicked.connect(lambda: self.buy(self.anz, "z"))
        self.anz_spinBox.valueChanged.connect(lambda value: self.check_quantity(value))
        self.wert_spinBox.valueChanged.connect(lambda value: self.calc_wert(value))

        # Mausevent mit Bild verknüpfen
        picture_label = self.findChild(QLabel, "picture")
        picture_label.mousePressEvent = lambda event: self.show_fullscreen(event, picture_label.pixmap())

        self.show()

    def closeEvent(self, event):
        print("Window is closing")
        switches.WindowHandler.release_window(accessoriesWindow)
        super().closeEvent(event)  # Fenster wird wirklich geschlossen

    @staticmethod
    def show_fullscreen(event, pixmap):
        FullScreenImage.show_fullscreen(event, pixmap)

    def load_ui(self):
        Helper2.replace.text(self.product[0], self.findChild(QLabel, "name_label"))
        if self.acc[3] == "Admin":
            Helper2.replace.text(locale.currency(int(float(self.product[1]) * 0.65), grouping=True),
                                 self.findChild(QLabel, "preis_status"))
            self.preis_label.setText("EK-Stückpreis:")
        else:
            Helper2.replace.text(locale.currency(int(self.product[1]), grouping=True),
                                 self.findChild(QLabel, "preis_status"))
        Helper2.replace.text(f"Budget:  {locale.currency(int(self.acc[2]), grouping=True)}",
                             self.findChild(QLabel, "budget_label"))
        Helper2.replace.text(self.hers_list, self.findChild(QLabel, "comp_label"))
        Helper2.load.complete_header(self)

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

    @staticmethod
    def load_zpic(name):
        gesucht = name
        pfad = os.path.join(PIC_PATH, r"Zubehör")

        for dateiname in os.listdir(pfad):
            if gesucht in dateiname:
                voll_pfad = os.path.join(pfad, dateiname)
                pixmap = QPixmap(voll_pfad)
                scaled_pixmap = pixmap.scaled(64, 64)
                return scaled_pixmap

    def calc_wert(self, jahre):
        normalpreis = int(float(self.product[1]) * 0.65) if self.acc[3] == "Admin" else int(self.product[1])
        verlustrate = (100 - self.loss) / 100
        new_value = int(normalpreis * (verlustrate ** jahre))  # ** -> Potenz (Zinseszins)
        Helper2.replace.text(locale.currency(new_value - normalpreis, grouping=True),
                             self.findChild(QLabel, "wert_status"))
        Helper2.replace.text(locale.currency(new_value, grouping=True), self.findChild(QLabel, "rest_status"))

    def check_quantity(self, value):
        self.calc_wert(value)
        available_quantity = int(self.product[2])
        current_shopping_list = Helper.BuyHandler.get_current_shoppinglist()

        total_quantity = sum(item[1] for item in current_shopping_list if item[0] == self.product[0])
        current_user = Helper_Accounts.UserHandler.get_current_user()

        if (total_quantity + value > available_quantity) and (current_user[3] != "Admin"):
            adjusted_quantity = min(value, available_quantity - total_quantity)
            self.anz_spinBox.setValue(adjusted_quantity)
            self.anz = adjusted_quantity
            message = f"Not enough quantity in the Lager for {self.product[0]}."
            Helper.show_toast(message, QMessageBox.Warning, QMessageBox.Ok, 2300)
        else:
            self.anz_spinBox.setValue(value)
            self.anz = value

    def buy(self, anz, typ):
        model = self.product[0]
        if anz > 0:
            current_shopping_list = Helper.BuyHandler.get_current_shoppinglist()

            # Check if product already in shopping list
            for item in current_shopping_list:
                if item[0] == model:
                    item[1] += anz
                    Helper.show_toast(f"Quantität von {model} im Warenkorb wurde aktualisiert.",
                                      QMessageBox.Information, QMessageBox.Ok, 1750)
                    self.anz_spinBox.setValue(0)
                    print(Helper.BuyHandler.get_current_shoppinglist())
                    return

            # If product not in shopping list, then add
            Helper.show_toast(f"Sie haben {anz}x {model} dem Warenkorb hinzugefügt.",
                              QMessageBox.Information, QMessageBox.Ok, 2500)
            Helper.BuyHandler.add_to_current_shoppinglist(model, anz, typ)
            self.anz_spinBox.setValue(0)
            print(Helper.BuyHandler.get_current_shoppinglist())
        else:
            Helper.show_toast("Bitte Quantität erhöhen", QMessageBox.Warning, QMessageBox.Ok, 1750)
