import os.path
import sys
import locale
import Helper, Helper2
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import *
from PyQt5 import uic


CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class WarenkorbWindow(QMainWindow):
    def __init__(self):
        super().__init__() # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Warenkorb.ui"), self)

        self.buttons = {}

        Helper2.conf.locale_setup(self)
        Helper2.load.complete_header(self)

        # shopping_list = Helper.BuyHandler.get_current_shoppinglist()
        self.shopping_list = [["Fendt","Vario_1050","521","60","367000","2015","8"],
                              ["Fendt","Vario_1038","395","60","298000","2015","2"]]     # zu Testzwecke

        self.add_shopping_items(self.shopping_list)
        self.add_sum_list(self.shopping_list)
        Helper2.replace.text(self, str(locale.currency(self.calc_sum(self.shopping_list), grouping=True)), self.findChild(QLabel, "summe_status"))

        self.buy_Button.clicked.connect(lambda: self.buy(self.shopping_list))

        self.show()


    def buy(self, liste):

        summe = self.calc_sum(liste)

        # kann pls jemand übernehmen, nur coding




    def calc_sum(self, liste):
        sum = 0

        for x in range(len(liste)):
            sum += (int(liste[x][4]) * int(liste[x][-1]))

        return sum

    def load_pic(self, gesucht, label):
        pfad = os.path.join(PIC_PATH, r"Traktoren")

        for dateiname in os.listdir(pfad):
            if gesucht in dateiname:
                voll_pfad = os.path.join(pfad, dateiname)
                pixmap = QPixmap(voll_pfad)
                return pixmap

    def add_sum_list(self, liste):

        scroll_area = self.findChild(QScrollArea, "summe_scrollarea")

        content_widget = QWidget()

        layout = QVBoxLayout(content_widget)

        for x in range(len(liste)):
            new_widget = QWidget()

            inner_layout = QVBoxLayout(new_widget)

            top_layer = QHBoxLayout()
            inner_layout.addLayout(top_layer)

            bottom_layer = QHBoxLayout()
            inner_layout.addLayout(bottom_layer)

            label1 = QLabel(f"{liste[x][0]} | {liste[x][1]}")
            label2 = QLabel(locale.currency(int(liste[x][4]), grouping=True))
            label3 = QLabel(f"   {liste[x][-1]} Stück")

            top_layer.addWidget(label1)
            top_layer.addWidget(label3)
            bottom_layer.addWidget(label2)

            layout.addWidget(new_widget)

        scroll_area.setWidget(content_widget)


    def add_shopping_items(self, liste):
        # dynamisches Layout laden
        scroll_area = self.findChild(QScrollArea, "dyn_scrollarea")

        # neues Widget als Container für einzelne Widgets
        content_widget = QWidget()

        # QHBoxLayout erstellen für Container
        layout = QVBoxLayout(content_widget)


        for x in range(len(liste)):
            new_widget = QWidget()
            new_widget.setStyleSheet("QWidget { border: 1px solid black; }")

            inner_layout = QHBoxLayout(new_widget)  # v-layout für widget


            picture_layout = QVBoxLayout()
            inner_layout.addLayout(picture_layout)

            label1 = QLabel()
            picture_layout.addWidget(label1)
            label1.setPixmap(self.load_pic(liste[x][1], label1))

            info_layout = QVBoxLayout()
            inner_layout.addLayout(info_layout)

            label2 = QLabel(f"{liste[x][0]} | {liste[x][1]}")
            label3 = QLabel("Beschreibung")

            info_layout.addWidget(label2)
            info_layout.addWidget(label3)


            value_layout = QVBoxLayout()
            inner_layout.addLayout(value_layout)

            label4 = QSpinBox()
            label5 = QPushButton("Entfernen")
            label6 = QLabel(locale.currency(int(liste[x][4]), grouping=True))

            self.buttons[x] = label5
            label5.clicked.connect(lambda: self.make_button_click_handler(liste[x][1]))

            value_layout.addWidget(label4)
            value_layout.addWidget(label5)
            value_layout.addWidget(label6)


            layout.addWidget(new_widget)  # widget dem container hinzufuegen

            # erstellten Container einfuegen in QScrollArea
            scroll_area.setWidget(content_widget)

    def make_button_click_handler(self, label):
        def button_click_handler():
            if label is not None:
                text = label.text()
                Helper.BuyHandler.remove_from_current_shoppinglist(text)
                self.shopping_list = Helper.BuyHandler.get_current_shoppinglist()
                self.add_widget(self.shopping_list)
            else:
                print("Label ist None")

        return button_click_handler





# if main program, run app, otherwise just import class
if __name__ == "__main__":
    app = QApplication(sys.argv) # construct QApp before QWidget
    window = WarenkorbWindow()
    window.show()  # class Mainwindow aufrufen
    sys.exit(app.exec_()) # exit cleanly


