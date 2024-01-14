import csv
import locale
import os.path

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from Vollbild_Klasse import FullScreenImage

import Helper
import Helper2
import Helper3
import Helper_Accounts
import switches

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")
BIDDERS_FILE_PATH = os.path.join("..", "resources", "csv", "Bidders.csv")


class GebrauchtwarenWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # vereinfacht das Erstellen weiterer
        uic.loadUi(os.path.join("..", "frontend", "GebrauchtwarenWindow.ui"), self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)

        print("AUFRUF GEBRAUCHT")

        # übergabeparameter
        self.product = Helper.current_Sell_Handler.get_current_sell_item()
        self.product_info = Helper2.load.product_info(self, [self.product])[0]

        # Währungsumgebung laden
        Helper2.conf.locale_setup(self)

        # Produktseite laden
        self.load_ui()

        # simulierte bidders
        self.beispielGebot = self.conv_preis
        self.bidders_liste = Helper_Accounts.get_bidders()
        self.bestOffer = []
        self.sortedOffers = []
        self.read_in_bidders()

        # dynamisches Widget laden
        self.add_widget()

        # Mausevent mit Bild verknüpfen
        picture_label = self.findChild(QLabel, "picture")
        picture_label.mousePressEvent = lambda event: self.show_fullscreen(event, picture_label.pixmap())

        self.show()

    def closeEvent(self, event):
        print("Window is closing")
        switches.WindowHandler.release_window(GebrauchtwarenWindow)
        super().closeEvent(event)  # Fenster wird wirklich geschlossen

    @staticmethod
    def show_fullscreen(event, pixmap):
        FullScreenImage.show_fullscreen(event, pixmap)

    def load_ui(self):
        pixmap = Helper2.load.product_pic(self, self.product)
        label = self.findChild(QLabel, "picture")
        label.setPixmap(pixmap)

        Helper2.replace.text(f"{self.product_info[0]} - {self.product_info[1]}", self.findChild(QLabel, "name_label"))
        Helper2.replace.text(locale.currency(float(self.product_info[4]), grouping=True),
                             self.findChild(QLabel, "alt_preis_status"))
        Helper2.replace.text(f"{self.product[1]} Stück", self.findChild(QLabel, "anz_status"))
        Helper2.replace.text(self.product_info[2], self.findChild(QLabel, "ps_status"))
        Helper2.replace.text(self.product_info[3], self.findChild(QLabel, "kmh_status"))
        Helper2.replace.text(self.product_info[5], self.findChild(QLabel, "baujahr_status"))
        Helper2.load.complete_header(self)

        self.convert_preis()

    def read_in_bidders(self):
        with open(BIDDERS_FILE_PATH, 'r', newline='') as file:
            data = list(csv.reader(file))

        for bidder in data:
            if Helper3.isInterested():
                bidder.append("yes")
                kaufangebot = Helper3.genKaufangebot(self.beispielGebot)  # bidder[1] # hier muss richtiges Gebot hin
                if int(kaufangebot) <= int(bidder[3]):  # kann nicht budget übersteigen
                    bidder[1] = kaufangebot
                else:
                    bidder[1] = bidder[3]
            else:
                bidder.append("no")
                bidder[1] = "0"
            print("bidder", bidder)




        self.bestOffer = max(data, key=lambda data: int(data[1]))
        self.sortedOffers = sorted(data, key=lambda data: int(data[1]), reverse=True)  # bid/offer

    def add_widget(self):
        scroll_area = self.findChild(QScrollArea, "dyn_scrollarea")

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        print("SORTED OFFERS")
        print(self.sortedOffers)

        stylesheet = "QLabel {color: white; font-size: 16px; font-weight: bold;}"
        for index in range(len(self.sortedOffers)):
            offer = self.sortedOffers[index]
            print(offer)

            new_widget = QWidget()
            new_widget.setStyleSheet(stylesheet)

            inner_layout = QHBoxLayout(new_widget)

            if index == 0:
                name = QLabel(f"Meistbietende/r: {offer[0]}")
                # name.setStyleSheet("font-size: 20px; font-weight: bold; ")
            else:
                name = QLabel(f"Bieter: {offer[0]}")
            inner_layout.addWidget(name, 1)

            if offer[1] != "0":
                gebot = QLabel(f"Gebot: {offer[1]}")
            else:
                gebot = QLabel(f"Kein Gebot")
            inner_layout.addWidget(gebot, 1)

            if index == 0:
                button = QPushButton("Verkauf bestätigen")
                button.clicked.connect(self.button_handler)
                button.setStyleSheet(
                    """
                    QPushButton{
                        border-radius: 10px;
                        background-color: rgb(230,126,34);
                        color: white;
                        font-size: 16px;
                        font-weight: bold;
                        min-height: 40px;
                    }
                    QPushButton:hover {
                        background-color: rgb(253,139,37);
                        opacity: 0.8;
                    }
                    QPushButton:pressed {
                        padding-left: 3px;
                        padding-bottom: 3px;
                    }
                    """
                )
                inner_layout.addWidget(button, 3)

            content_layout.addWidget(new_widget)

        scroll_area.setWidget(content_widget)

    def button_handler(self):
        modell = self.product[0]
        anzahl = self.product[1]
        t_z = self.product[2]
        account = self.product[3]
        timestamp = self.product[4]
        preis = float(self.product_info[4])
        Helper_Accounts.sellGebrauchtFromInventar(modell, anzahl, t_z, account, timestamp)
        Helper_Accounts.update_biddersBalance(account, preis)   # voller preis abzug von bidder
        Helper_Accounts.update_accountsBalance(account, preis*0.99)     # 99 % von Wert für Verkäufer
        Helper_Accounts.update_klausBalance(preis*0.01)     # 1 % Provision für Klaus
        print("verkauf bestätigt")
        Helper.show_toast(f"Der Verkauf über {preis}€ wurde erfolgreich abgeschlossen.",
                          QMessageBox.Information,
                          QMessageBox.Ok, 2000)

    def convert_preis(self):

        preis = int(self.product_info[4])
        loss = int(Helper2.load.loss(self.product_info[0]))
        jahre = int(Helper.get_time_difference_since_program_time(f"{self.product_info[-2]}-01-01 12:00:00"))
        verlustrate = (100 - loss) / 100
        neu_preis = int(float(preis) * float(verlustrate ** jahre))

        self.conv_preis = neu_preis

        Helper2.replace.text(self.product[4][:4], self.findChild(QLabel, "kauf_status"))
        Helper2.replace.text(str(jahre), self.findChild(QLabel, "zeit_status"))
        Helper2.replace.text(locale.currency((neu_preis-preis), grouping=True), self.findChild(QLabel, "wert_status"))
        Helper2.replace.text(locale.currency(neu_preis, grouping=True), self.findChild(QLabel, "neu_preis_status"))
