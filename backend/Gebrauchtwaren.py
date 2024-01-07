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


        print("AUFRUF GEBRAUCHT")

        self.beispielGebot = 142069 # brauchen aber eigentliches Gebot


        # übergabeparameter
        self.product = Helper.current_Sell_Handler.get_current_sell_item()
        self.product_info = Helper2.load.product_info(self, [self.product])[0]
        print(self.product)
        print(Helper.get_time_difference_since_program_time(self.product[4]))
        print(Helper.get_program_time())
        print("PRODUCT:")
        print(self.product[4])

        self.bidders_liste = Helper_Accounts.get_bidders()
        # simulierte bidders
        self.bestOffer = 0
        self.sortedOffers = 0
        self.readInBidders()

        print(self.bestOffer)
        print(self.sortedOffers)
        print("bestOffer:", self.bestOffer)
        print("sortedOffers:", self.sortedOffers)

        # Währungsumgebung laden
        Helper2.conf.locale_setup(self)

        # dynamisches Widget laden
        self.add_widget()

        # Produktseite laden
        self.load_ui()

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

        Helper2.replace.text(f"{self.product_info[0]} - {self.product_info[1]}",
                                 self.findChild(QLabel, "name_label"))
        Helper2.replace.text(locale.currency(int(self.product_info[4]), grouping=True),
                                 self.findChild(QLabel, "alt_preis_status"))
        Helper2.replace.text(f"{self.product[1]} Stück", self.findChild(QLabel, "anz_status"))
        Helper2.replace.text(self.product_info[2], self.findChild(QLabel, "ps_status"))
        Helper2.replace.text(self.product_info[3], self.findChild(QLabel, "kmh_status"))
        Helper2.replace.text(self.product_info[5], self.findChild(QLabel, "baujahr_status"))
        Helper2.load.complete_header(self)

    def readInBidders(self):
        with open(BIDDERS_FILE_PATH, 'r', newline='') as file:
            data = list(csv.reader(file))

        for bidder in data:
            if not Helper3.isInterested():
                data.remove(bidder)
        for bidder in data:
            kaufangebot = Helper3.genKaufangebot(self.beispielGebot)#bidder[1]) # hier muss richtiges Gebot hin
            if kaufangebot <= bidder[3]:    # kann nicht budget übersteigen
                bidder[1] = kaufangebot
            else:
                bidder[1] = bidder[3]

        self.bestOffer = max(data, key=lambda data: data[1])
        self.sortedOffers = sorted(data, key=lambda data: data[1], reverse=True)  # bid/offer


    def add_widget(self):
        scroll_area = self.findChild(QScrollArea, "dyn_scrollarea")

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        new_widget = QWidget()
        inner_layout = QVBoxLayout(new_widget)

        button = QPushButton("Verkauf bestätigen")
        button.clicked.connect(self.button_handler)

        inner_layout.addWidget(button)
        content_layout.addWidget(new_widget)

        new_widget.setLayout(inner_layout)
        content_widget.setLayout(content_layout)

        scroll_area.setWidget(content_widget)




    def button_handler(self):
        pass




    def confirm_sell(self, gebot, bidder):
        Helper.show_toast(f"{bidder} hat den Verkauf über {gebot}€ abgeschlossen.",
                          QMessageBox.Information,
                          QMessageBox.Ok, 2000)

    def calc_wert(self, product, loss, jahre):
        normalPreis = int(product)
        verlustRate = (100 - loss) / 100
        new_value = normalPreis * (verlustRate) ** jahre
        # Zinseszinzprinzip:
        # Endbetrag = Kapital×(Zinsesrate) hoch Jahresanzahl
        Helper2.replace.text(locale.currency(new_value, grouping=True), self.findChild(QLabel, "wert_status"))

    def bidderSell(self, gebot, bidder):  # sell and handle money transfers
        verkaufsPreis = int(gebot * 0.99)
        Helper_Accounts.update_biddersBalance(bidder, verkaufsPreis)
        provision = int(gebot * 0.01)
        Helper_Accounts.update_klausBalance(provision)