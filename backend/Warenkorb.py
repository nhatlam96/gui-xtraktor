import os.path
import sys
import locale
import Helper, Helper2, Helper3
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import *
from PyQt5 import uic

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class WarenkorbWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Warenkorb.ui"), self)

        self.buttons = {}
        self.spinBoxes = {}

        Helper2.conf.locale_setup(self)
        Helper2.load.complete_header(self)

        self.shopping_list = Helper.BuyHandler.get_current_shoppinglist()

        # shopping_list = Helper.BuyHandler.get_current_shoppinglist()
        self.info_list = self.load_info(self.shopping_list) if self.shopping_list else []

        self.add_shopping_items(self.info_list, self.shopping_list)
        self.add_sum_list(self.info_list, self.shopping_list)
        Helper2.replace.text(self,
                             str(locale.currency(self.calc_sum(self.info_list, self.shopping_list), grouping=True)),
                             self.findChild(QLabel, "summe_status"))

        self.buy_Button.clicked.connect(lambda: self.buy(self.info_list))

        self.show()

    def set_anz(self, number, value):
        self.shopping_list[number][1] = value
        self.add_sum_list(self.info_list, self.shopping_list)
        Helper2.replace.text(self,
                             str(locale.currency(self.calc_sum(self.info_list, self.shopping_list), grouping=True)),
                             self.findChild(QLabel, "summe_status"))

    def buy(self, liste):
        # TODO toast confirmation: sicher ob kaufen oder nicht
        print(liste)
        # summe = self.calc_sum(self, liste) # self, info_liste, shopping_liste
        # sum = Helper3.getSumme(geraeteArt, geraeteTyp, anzahl, account):
        # print(sum)
        
        # kann pls jemand übernehmen, nur coding

    def load_info(self, liste):
        info = []
        for x in range(len(liste)):
            if liste[x][2] == "t":
                info.append(Helper2.load.traktor_data(self, liste[x][0]))
            if liste[x][2] == "z":
                info.append(Helper2.load.zub_data(self, liste[x][0]))

        print("load_info geht!")
        print(info)
        return info

    def calc_sum(self, info_liste, shopping_liste):
        summe = 0

        for x in range(len(shopping_liste)):
            if shopping_liste[x][2] == "t":
                summe += (int(info_liste[x][4]) * int(shopping_liste[x][1]))
            if shopping_liste[x][2] == "z":
                summe += (int(info_liste[x][1]) * int(shopping_liste[x][1]))

        return summe

    def load_pic(self, row):

        pfad = os.path.join(PIC_PATH, r"Traktoren")

        if row[2] == "z":
            pfad = os.path.join(PIC_PATH, r"Zubehör")

        gesucht = row[0]

        for dateiname in os.listdir(pfad):
            if gesucht in dateiname:
                voll_pfad = os.path.join(pfad, dateiname)
                pixmap = QPixmap(voll_pfad)
                return pixmap

    def add_sum_list(self, info_liste, shopping_liste):

        scroll_area = self.findChild(QScrollArea, "summe_scrollarea")

        content_widget = QWidget()

        layout = QVBoxLayout(content_widget)

        for x in range(len(shopping_liste)):
            new_widget = QWidget()
            new_widget.setMaximumHeight(100)

            inner_layout = QVBoxLayout(new_widget)

            top_layer = QHBoxLayout()
            inner_layout.addLayout(top_layer)

            bottom_layer = QHBoxLayout()
            inner_layout.addLayout(bottom_layer)

            if shopping_liste[x][2] == "t":
                label1 = QLabel(f"{info_liste[x][0]} | {info_liste[x][1]}")
                label2 = QLabel(locale.currency(int(info_liste[x][4]), grouping=True))
                label3 = QLabel(f"   {shopping_liste[x][1]} Stück")

            if shopping_liste[x][2] == "z":
                label1 = QLabel(f"Zubehoer | {info_liste[x][0]}")
                label2 = QLabel(locale.currency(int(info_liste[x][1]), grouping=True))
                label3 = QLabel(f"   {shopping_liste[x][1]} Stück")

            top_layer.addWidget(label1)
            top_layer.addWidget(label3)
            bottom_layer.addWidget(label2)

            layout.addWidget(new_widget)

        scroll_area.setWidget(content_widget)

    def add_shopping_items(self, info_liste, shopping_liste):

        # dynamisches Layout laden
        scroll_area = self.findChild(QScrollArea, "dyn_scrollarea")

        # neues Widget als Container für einzelne Widgets
        content_widget = QWidget()

        # QHBoxLayout erstellen für Container
        layout = QVBoxLayout(content_widget)

        for x in range(len(shopping_liste)):
            new_widget = QWidget()
            new_widget.setMaximumHeight(200)

            inner_layout = QHBoxLayout(new_widget)  # v-layout für widget

            picture_layout = QVBoxLayout()
            inner_layout.addLayout(picture_layout, 1)

            label1 = QLabel()
            picture_layout.addWidget(label1)
            pixmap = self.load_pic(shopping_liste[x])
            scaled_pixmap = pixmap.scaled(200, 200)
            label1.setPixmap(scaled_pixmap)

            info_layout = QVBoxLayout()
            inner_layout.addLayout(info_layout, 3)

            if shopping_liste[x][2] == "t":
                label2 = QLabel(f"{info_liste[x][0]} | {shopping_liste[x][0]}")

            elif shopping_liste[x][2] == "z":
                label2 = QLabel(f"Zubehoer | {shopping_liste[x][0]}")
            else:
                label2 = QLabel()

            label3 = QLabel("Beschreibung")

            info_layout.addWidget(label2)
            info_layout.addWidget(label3)

            value_layout = QVBoxLayout()
            inner_layout.addLayout(value_layout, 3)

            label4 = QSpinBox()
            label5 = QPushButton("Entfernen")

            label4.setMinimum(1)
            label4.setValue(shopping_liste[x][1])
            if shopping_liste[x][2] == "t":
                label6 = QLabel(locale.currency(int(info_liste[x][4]), grouping=True))
            elif shopping_liste[x][2] == "z":
                label6 = QLabel(locale.currency(int(info_liste[x][1]), grouping=True))
            else:
                label6 = QLabel()

            self.spinBoxes[x] = label4
            label4.valueChanged.connect(lambda value, nr=x: self.set_anz(nr, value))

            self.buttons[x] = label5
            label5.clicked.connect(lambda nr=x: self.make_button_click_handler(shopping_liste[nr][0]))

            value_layout.addWidget(label4)
            value_layout.addWidget(label5)
            value_layout.addWidget(label6)

            layout.addWidget(new_widget)  # widget dem container hinzufuegen

        # erstellten Container einfuegen in QScrollArea
        scroll_area.setWidget(content_widget)

    def make_button_click_handler(self, label):

        Helper.BuyHandler.remove_from_current_shoppinglist(str(label))
        self.shopping_list = Helper.BuyHandler.get_current_shoppinglist()
        self.info_list = self.load_info(self.shopping_list) if self.shopping_list else []
        print(self.shopping_list)
        self.add_shopping_items(self.info_list, self.shopping_list)
        self.add_sum_list(self.info_list, self.shopping_list)
        Helper2.replace.text(self, 
                             str(locale.currency(self.calc_sum(self.info_list, self.shopping_list), grouping=True)),
                             self.findChild(QLabel, "summe_status"))
