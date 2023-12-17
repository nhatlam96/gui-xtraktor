import locale
import os.path
import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize
import Helper, Helper2, Helper3, Helper_Accounts
import switches

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")




class GebrauchtwarenWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "GebrauchtwarenWindow.ui"), self)


        # alles Simulation, denn braucht integration durch Startseite, die noch nicht fertig ist

        # Simulierte übergabeparameter
        platzhalter = [["Axos_340_CX", 5, "t"]]
        self.product = platzhalter
        self.product_info = Helper2.load.product_info(self, platzhalter)[0]
        acc = ["Sieglinde", 100000]


        #simulierte bidder
        self.bidder = [ ["Alejandro", 160000],
                        ["Francois", 400000],
                        ["Chris", 90000],
                        ["Francesco", 190000],
                        ["Mette", 275000],
                        ["Birgit", 700000],
                        ["Lukas", 110000],
                        ["Sandra", 75000] ]


        # dyn.Layout buttons
        self.buttons = {}

        # Währungsumgebung laden
        Helper2.conf.locale_setup(self)

        # dynamisches Widget laden
        self.add_widget()

        # Produktseite laden
        self.load_ui(self.product_info, acc)
        self.load_pic(self.product_info)


        self.show()




    def load_ui(self, product, user):
        Helper2.replace.text(self,
                             f"{product[0]} - {product[1]}", self.findChild(QLabel, "name_label")
                             )
        Helper2.replace.text(self,
                             locale.currency(int(product[4]), grouping=True), self.findChild(QLabel, "alt_preis_status")
                             )
        Helper2.replace.text(self, product[2], self.findChild(QLabel, "ps_status"))
        Helper2.replace.text(self, product[3], self.findChild(QLabel, "kmh_status"))
        Helper2.replace.text(self, product[5], self.findChild(QLabel, "baujahr_status"))
        Helper2.load.complete_header(self)


    def load_pic(self, row):
        gesucht = row[1]
        pfad = os.path.join(PIC_PATH, r"Traktoren")

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



    def add_widget(self):

        scroll_area = self.findChild(QScrollArea, "dyn_scrollarea")
        content_widget = QWidget()
        layout = QHBoxLayout(content_widget)


        new_widget = QWidget()
        inner_layout = QVBoxLayout(new_widget)  # v-layout für widget


        head_layout = QVBoxLayout()
        inner_layout.addLayout(head_layout, 8)


        for x in range(len(self.bidder)):
            other_buyer = QLabel(f"{self.bidder[x][0]}")
            other_buyer.setAlignment(Qt.AlignCenter)
            other_buyer_price = QLabel(f"{locale.currency(int(self.bidder[x][1]), grouping=True)}")
            other_buyer_price.setAlignment(Qt.AlignCenter)
            buyer_info_layout = QHBoxLayout()
            buyer_info_layout.addWidget(other_buyer)
            buyer_info_layout.addWidget(other_buyer_price)
            head_layout.addLayout(buyer_info_layout)

        content_layout = QVBoxLayout()
        inner_layout.addLayout(content_layout, 4)


        title_layout =QVBoxLayout()
        title_layout.setContentsMargins(0, 40, 0, 40)
        content_layout.addLayout(title_layout,2)
        title = QLabel("Höchstes Gebot")
        title.setAlignment(Qt.AlignCenter)

        title_layout.addWidget(title)


        buyer_layout = QHBoxLayout()
        content_layout.addLayout(buyer_layout, 2)
        buyer = QLabel(f"{self.bidder[1][0]}")
        price = QLabel(f"{locale.currency(int(self.bidder[1][1]), grouping=True)}")

        button = QPushButton("Verkauf bestätigen")
        self.buttons = button
        button.clicked.connect(lambda : self.confirm_sell(self.bidder[1]))


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


    def confirm_sell(self, bidder):

        #toast zum bestätigen


        pass







    def calc_wert(self, product, loss, jahre):
        normalPreis = int(product)
        verlustRate = (100 - loss) / 100
        new_value = normalPreis * (verlustRate) ** jahre
        # Zinseszinzprinzip:
        # Endbetrag = Kapital×(Zinsesrate) hoch Jahresanzahl
        Helper2.replace.text(self,locale.currency(new_value, grouping=True),self.findChild(QLabel, "wert_status"))


    def sell(self, product):  # sell and handle money transfers
        normalPreis = int(product)
        provision = normalPreis * 0.01
        # Helper_Accounts.update_userBalance("Klaus", provision) # this is the real one
        Helper_Accounts.update_userBalance("Test", provision)  # this is for test



def main():
    app = QApplication(sys.argv)  # construct QApp before QWidget
    window = GebrauchtwarenWindow()
    window.setWindowTitle("X-Traktor")
    window.show()  # class Mainwindow aufrufen
    sys.exit(app.exec_())  # exit cleanly


if __name__ == "__main__":
    main()
