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


class GebrauchtwarenWindowAccessories(QMainWindow):
    def __init__(self):
        super().__init__()  # vereinfacht das Erstellen weiterer
        uic.loadUi(os.path.join("..", "frontend", "GebrauchtwarenWindowAccessories.ui"), self)

        print("AUFRUF GEBRAUCHT ACCESSORIES")

        # übergabeparameter
        self.product = Helper.current_Sell_Handler.get_current_sell_item()
        self.product_info = Helper2.load.product_info(self, [self.product])[0]

        # simulierte bidders
        # self.bidders = self.readInBidders()
        # print(self.bidders)

        # Währungsumgebung laden
        Helper2.conf.locale_setup(self)

        # dynamisches Widget laden
        # self.add_widget()

        # Produktseite laden
        self.load_ui()

        # Mausevent mit Bild verknüpfen
        picture_label = self.findChild(QLabel, "picture")
        picture_label.mousePressEvent = lambda event: self.show_fullscreen(event, picture_label.pixmap())

        self.show()

    def closeEvent(self, event):
        print("Window is closing")
        switches.WindowHandler.release_window(GebrauchtwarenWindowAccessories)
        super().closeEvent(event)  # Fenster wird wirklich geschlossen

    @staticmethod
    def show_fullscreen(event, pixmap):
        FullScreenImage.show_fullscreen(event, pixmap)

    def load_ui(self):
        pixmap = Helper2.load.product_pic(self, self.product)
        label = self.findChild(QLabel, "picture")
        label.setPixmap(pixmap)

        Helper2.replace.text(f"{self.product[1]} Stück", self.findChild(QLabel, "anz_status"))
        Helper2.replace.text(f"Zubehör - {self.product_info[0]}",
                                 self.findChild(QLabel, "name_label"))
        Helper2.replace.text(locale.currency(int(self.product_info[1]), grouping=True),
                                 self.findChild(QLabel, "alt_preis_status"))
        Helper2.load.complete_header(self)
        Helper2.replace.text(f"{str(self.load_hers())}", self.findChild(QLabel, "comp_label"))



    def load_hers(self):
        conv_text = ", ".join(self.product_info[3:])
        return conv_text

    def readInBidders(self):
        with open(BIDDERS_FILE_PATH, 'r', newline='') as file:
            data = list(csv.reader(file))

        for bidder in data:
            if not Helper3.isInterested():
                data.remove(bidder)
        for bidder in data:
            bidder[1] = Helper3.genKaufangebot(bidder[1])

        # bestOffer = max(data, key=lambda data: data[1])
        sortedOffers = sorted(data, key=lambda data: data[1])  # bid/offer
        return sortedOffers

    def add_widget(self):

        scroll_area = self.findChild(QScrollArea, "dyn_scrollarea")
        content_widget = QWidget()
        layout = QHBoxLayout(content_widget)

        new_widget = QWidget()
        inner_layout = QVBoxLayout(new_widget)  # v-layout für widget

        head_layout = QVBoxLayout()
        inner_layout.addLayout(head_layout, 8)

        for x in range(len(self.bidders)):
            other_buyer = QLabel(f"{self.bidders[x][0]}")
            other_buyer.setAlignment(Qt.AlignCenter)
            other_buyer_price = QLabel(f"{locale.currency(int(self.bidders[x][1]), grouping=True)}")
            other_buyer_price.setAlignment(Qt.AlignCenter)
            buyer_info_layout = QHBoxLayout()
            buyer_info_layout.addWidget(other_buyer)
            buyer_info_layout.addWidget(other_buyer_price)
            head_layout.addLayout(buyer_info_layout)

        content_layout = QVBoxLayout()
        inner_layout.addLayout(content_layout, 4)

        title_layout = QVBoxLayout()
        title_layout.setContentsMargins(0, 40, 0, 40)
        content_layout.addLayout(title_layout, 2)
        title = QLabel("Höchstes Gebot")
        title.setAlignment(Qt.AlignCenter)

        title_layout.addWidget(title)

        buyer_layout = QHBoxLayout()
        content_layout.addLayout(buyer_layout, 2)
        buyer = QLabel(f"{self.bidders[1][0]}")
        price = QLabel(f"{locale.currency(int(self.bidders[1][1]), grouping=True)}")

        button = QPushButton("Verkauf bestätigen")
        button.clicked.connect(lambda: self.confirm_sell(self, price, buyer))
        button.clicked.connect(lambda: self.bidderSell(self, price, buyer))

        buyer_layout.addWidget(buyer)
        buyer_layout.addWidget(price)
        buyer_layout.addWidget(button)

        layout.addWidget(new_widget)  # widget dem container hinzufuegen

        # erstellten Container einfuegen in QScrollArea
        scroll_area.setWidget(content_widget)

    def make_button_click_handler(self, label):
        def button_click_handler():
            if label is not None:
                text = label.text()
                Helper.AccessoriesHandler.set_current_acc(text)
                switches.switch_to.accessories(self)
            else:
                print("Label ist None")

        return button_click_handler

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