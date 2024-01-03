import locale
import os.path

from PyQt5 import uic
from PyQt5.QtWidgets import *

import Helper_Accounts
import Helper
import Helper2
import switches

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class SellWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Sell.ui"), self)

        print("AUFRUF SELL")

        # Übergabeparameter
        self.inventar_liste = Helper.InvHandler.get_inv()
        print(self.inventar_liste)
        self.info_liste = Helper2.load.product_info(self, self.inventar_liste)
        self.bidders_liste = Helper_Accounts.get_bidders()

        # Lokale Umbegbung laden
        Helper2.conf.locale_setup(self)

        # Buttons von dyn. Layout
        self.buttons_tab1 = {}

        # UI laden
        self.load_ui()

        print("WORKS")
        self.show()

    def load_ui(self):
        Helper2.load.complete_header(self)
        self.create_content()
        self.add_bidders_tab()


    def create_content(self):

        scroll_area = self.findChild(QScrollArea, "scrollArea")

        content_widget = QWidget()

        layout = QVBoxLayout(content_widget)

        for x in range(len(self.inventar_liste)):

            new_widget = QWidget()
            new_widget.setMaximumHeight(200)

            inner_layout = QHBoxLayout(new_widget)  # v-layout für widget

            picture_layout = QVBoxLayout()
            inner_layout.addLayout(picture_layout, 1)

            label1 = QLabel()
            picture_layout.addWidget(label1)
            pixmap = Helper2.load.product_pic(self, self.inventar_liste[x])
            scaled_pixmap = pixmap.scaled(200, 200)
            label1.setPixmap(scaled_pixmap)

            info_layout = QVBoxLayout()
            inner_layout.addLayout(info_layout, 3)

            if self.inventar_liste[x][2] == "t":
                label2 = QLabel(f"{self.info_liste[x][0]} | {self.inventar_liste[x][0]}")
            elif self.inventar_liste[x][2] == "z":
                label2 = QLabel(f"Zubehoer | {self.inventar_liste[x][0]}")
            else:
                label2 = QLabel()

            info_layout.addWidget(label2, 1)


            desc_layout = QVBoxLayout()
            info_layout.addLayout(desc_layout, 3)

            if self.inventar_liste[x][2] == "z":
                pass
            else:
                ps = QLabel(f"PS: {self.info_liste[x][2]}")
                km = QLabel(f"Km/h: {self.info_liste[x][3]}")
                baujahr = QLabel(f"Baujahr: {self.info_liste[x][5]}")

                desc_layout.addWidget(ps)
                desc_layout.addWidget(km)
                desc_layout.addWidget(baujahr)


            value_layout = QVBoxLayout()
            inner_layout.addLayout(value_layout, 3)

            anz_layout = QHBoxLayout()
            value_layout.addLayout(anz_layout)

            label4 = QLabel(f"Im Besitz: {self.inventar_liste[x][1]} Stück")
            spinbox = QSpinBox()
            spinbox.setSuffix(" Stück")
            spinbox.setMaximum(int(self.inventar_liste[x][1]))

            label5 = QPushButton("Verkaufen")

            self.buttons_tab1[x] = label5
            label5.clicked.connect(lambda nr=x, label=self.inventar_liste[x][0], typ=self.inventar_liste[x][2],
                                          zeit=self.inventar_liste[x][4], user = self.inventar_liste[x][3],
                                          spin=spinbox: self.make_button_click_handler(label, spin.value(), typ,user, zeit))


            value_innerlayout = QHBoxLayout()

            if self.inventar_liste[x][2] == "t":
                label6 = QLabel(locale.currency(int(self.info_liste[x][4]), grouping=True))
            elif self.inventar_liste[x][2] == "z":
                label6 = QLabel(locale.currency(int(self.info_liste[x][1]), grouping=True))
            else:
                label6 = QLabel()

            label7 = QLabel(f"Alter: ")

            value_innerlayout.addWidget(label7)
            value_innerlayout.addWidget(label6)

            anz_layout.addWidget(label4)
            anz_layout.addWidget(spinbox)

            value_layout.addWidget(label5)
            value_layout.addLayout(value_innerlayout)

            layout.addWidget(new_widget)

        scroll_area.setWidget(content_widget)

    def add_bidders_tab(self):

        scroll_area = self.findChild(QScrollArea, "bidders_scrollArea")
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        for item in self.bidders_liste:
            new_widget = QWidget()
            new_widget.setMaximumHeight(100)

            inner_layout = QHBoxLayout(new_widget)

            label1 = QLabel(item[0])
            label2 = QLabel(locale.currency(int(item[3]), grouping=True))

            inner_layout.addWidget(label1)
            inner_layout.addWidget(label2)

            layout.addWidget(new_widget)

        scroll_area.setWidget(content_widget)



    def make_button_click_handler(self, label, anz, typ,user, zeit):

        if anz > 0:
            print(self.inventar_liste[0])
            Helper.current_Sell_Handler.add_sell_item(label, anz, typ, user, zeit)
            if typ == "t":
                switches.switch_to.Sell_item()
            else:
                switches.switch_to.Sell_item_Access()
