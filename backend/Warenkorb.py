import locale
import os.path

from PyQt5 import uic
from PyQt5.QtWidgets import *

import Helper
import Helper2
import Helper_Accounts
from Helper_Accounts import UserHandler, update_userBalance
from Helper import get_program_time

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class WarenkorbWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Warenkorb.ui"), self)

        print("AUFRUF WARENKORB")

        # Übergabeparameter
        self.acc = UserHandler.get_current_user()
        self.shopping_list = Helper.BuyHandler.get_current_shoppinglist()
        self.info_list = Helper2.load.product_info(self, self.shopping_list) if self.shopping_list else []

        print("INFO")
        print(self.info_list)

        # dyn.Layout buttons
        self.buttons = {}
        self.spinBoxes = {}

        # Lokale Umgebung laden
        Helper2.conf.locale_setup(self)

        # Ui laden
        self.load_ui()

        # Aktionen
        self.buy_Button.clicked.connect(lambda: self.buy(self.acc))
        self.showFullScreen()
        self.show()

    def load_ui(self):
        Helper2.load.complete_header(self)
        self.add_shopping_items(self.info_list, self.shopping_list)
        self.add_sum_list(self.info_list, self.shopping_list)
        Helper2.replace.text(str(locale.currency(self.calc_sum(self.info_list, self.shopping_list), grouping=True)),
                             self.findChild(QLabel, "summe_status"))

    def check_quantity(self, number, value):
        print(f"Warenkorb.py - check params: {number}, {value}")  # Debug
        print(f"Warenkorb.py - shopping list: {self.shopping_list}")  # Debug
        print(f"Warenkorb.py - info list: {self.info_list}")  # Debug

        product_name = self.shopping_list[number][0]
        if self.shopping_list[number][2] == "t":
            available_quantity = int(self.info_list[number][6])
        else:
            available_quantity = int(self.info_list[number][2])

        if value > available_quantity:
            adjusted_quantity = min(value, available_quantity)
            self.spinBoxes[number].setValue(adjusted_quantity)
            self.shopping_list[number][1] = adjusted_quantity
            message = f"Not enough quantity in the Lager for {product_name}."
            Helper.show_toast(message, QMessageBox.Warning, QMessageBox.Ok, 1750)
        else:
            self.shopping_list[number][1] = value

        self.add_sum_list(self.info_list, self.shopping_list)
        Helper2.replace.text(str(locale.currency(self.calc_sum(self.info_list, self.shopping_list), grouping=True)),
                             self.findChild(QLabel, "summe_status"))

    def buy(self, user):
        print(f"Warenkorb.py - Shopping Liste: {self.shopping_list}")  # Debug
        # Check if the shopping list is empty
        if not self.shopping_list:
            Helper.show_toast("Shopping list is empty!", QMessageBox.Warning, QMessageBox.Ok, 1750)
            return
        else:
            confirmation = Helper.show_toast_confirmation(self, "Kauf bestätigen?")
            if confirmation == QMessageBox.Yes:

                summe = self.calc_sum(self.info_list, self.shopping_list)
                # check if enough budget is available and then subtract the sum from the budget
                if summe <= int(user[2]):
                    update_userBalance(user[0], -summe)
                    Helper_Accounts.UserHandler.set_current_user(user[0])
                    Helper.show_toast("Kauf erfolgreich!", QMessageBox.Information, QMessageBox.Ok, 1750)

                    # update the user inventory csv file
                    for item in self.shopping_list:
                        Helper_Accounts.writeInventar(item[0], item[1], item[2], get_program_time().format("YYYY-MM"
                                                                                                           "-DD "
                                                                                                           "HH:mm:ss"))
                    # update the seller inventories csv file
                    Helper_Accounts.update_seller_inventories(self.shopping_list)

                    Helper.BuyHandler.clear_current_shoppinglist()
                    self.shopping_list = Helper.BuyHandler.get_current_shoppinglist()
                    self.info_list = self.load_info(self.shopping_list) if self.shopping_list else []
                    self.add_shopping_items(self.info_list, self.shopping_list)
                    self.add_sum_list(self.info_list, self.shopping_list)
                    Helper2.load.complete_header(self)
                    Helper2.replace.text(str(locale.currency(int(0), grouping=True)),
                                         self.findChild(QLabel, "summe_status"))
                else:
                    Helper.show_toast("Nicht genug Budget!", QMessageBox.Warning, QMessageBox.Ok, 1750)

    @staticmethod
    def calc_sum(info_liste, shopping_liste):
        summe = 0
        for x in range(len(shopping_liste)):
            if shopping_liste[x][2] == "t":
                summe += (int(info_liste[x][4]) * int(shopping_liste[x][1]))
            if shopping_liste[x][2] == "z":
                summe += (int(info_liste[x][1]) * int(shopping_liste[x][1]))
        return summe

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
                label2 = QLabel(locale.currency(int(float(info_liste[x][4])), grouping=True))
                label3 = QLabel(f"   {shopping_liste[x][1]} Stück")

            else:
                label1 = QLabel(f"Zubehör | {info_liste[x][0]}")
                label2 = QLabel(locale.currency(int(float(info_liste[x][1])), grouping=True))
                label3 = QLabel(f"   {shopping_liste[x][1]} Stück")

            top_layer.addWidget(label1)
            top_layer.addWidget(label3)
            bottom_layer.addWidget(label2)

            label1.setStyleSheet("color: white; font-size: 16px; font-weight: 500;")
            label2.setStyleSheet("color: white; font-size: 16px; font-weight: 500;")
            label3.setStyleSheet("color: white; font-size: 16px; font-weight: 500;")
            layout.addWidget(new_widget)

        scroll_area.setWidget(content_widget)

    def add_shopping_items(self, info_liste, shopping_liste):

        scroll_area = self.findChild(QScrollArea, "dyn_scrollarea")
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        for x in range(len(shopping_liste)):
            new_widget = QWidget()
            new_widget.setMaximumHeight(200)

            inner_layout = QHBoxLayout(new_widget)  # v-layout für widget

            picture_layout = QVBoxLayout()
            inner_layout.addLayout(picture_layout, 1)

            label1 = QLabel()
            picture_layout.addWidget(label1)
            pixmap = Helper2.load.product_pic(self, shopping_liste[x])
            scaled_pixmap = pixmap.scaled(200, 200)
            label1.setPixmap(scaled_pixmap)

            info_layout = QVBoxLayout()
            inner_layout.addLayout(info_layout, 3)

            if shopping_liste[x][2] == "t":
                self.convert_preis(x)
                label2 = QLabel(f"{info_liste[x][0]} | {shopping_liste[x][0]}")
            elif shopping_liste[x][2] == "z":
                label2 = QLabel(f"Zubehör | {shopping_liste[x][0]}")
            else:
                label2 = QLabel()

            label2.setStyleSheet("color: white; font-size: 16px; font-weight: 500;")
            label3 = QLabel("Beschreibung")
            label3.setStyleSheet("color: white; font-size: 16px; font-weight: 500;")

            info_layout.addWidget(label2)
            info_layout.addWidget(label3)

            value_layout = QVBoxLayout()
            inner_layout.addLayout(value_layout, 3)

            label4 = QSpinBox()
            label4.setStyleSheet("""
                color: white;
                font-size: 16px;
                font-weight: 500;
                background-color: grey;
                min-height: 25px;
            """)
            label4.setMinimum(1)
            label4.setValue(shopping_liste[x][1])
            self.spinBoxes[x] = label4
            label4.valueChanged.connect(lambda value, nr=x: self.check_quantity(nr, value))

            label5 = QPushButton("Entfernen")
            label5.setStyleSheet("""
                QPushButton {
                    background-color: rgb(192, 57, 43);
                    min-height: 30px;
                    border-radius: 10px;
                    color:white;
                    font-size:16px;
                    font-weight: 500;
                }
                QPushButton:hover {
                    background-color: rgb(211, 84, 0);
                    cursor: pointer;
                }
                QPushButton:pressed {
                    padding-left: 3px;
                    padding-bottom: 3px;
                }    
            """)
            self.buttons[x] = label5
            label5.clicked.connect(lambda nr=x: self.make_button_click_handler(shopping_liste[nr][0]))

            if shopping_liste[x][2] == "t":
                label6 = QLabel(locale.currency(int(float(info_liste[x][4])), grouping=True))
            elif shopping_liste[x][2] == "z":
                label6 = QLabel(locale.currency(int(float(info_liste[x][1])), grouping=True))
            else:
                label6 = QLabel()
            label6.setStyleSheet("color: white; font-size: 16px; font-weight: 500;")

            value_layout.addWidget(label4)
            value_layout.addWidget(label5)
            value_layout.addWidget(label6)

            layout.addWidget(new_widget)  # widget dem container hinzufügen

        # erstellten Container einfügen in QScrollArea
        scroll_area.setWidget(content_widget)

    def make_button_click_handler(self, label):

        # Helper Wert aktualisieren
        Helper.BuyHandler.remove_from_current_shoppinglist(str(label))

        # Lokale Werte aktualisieren
        self.shopping_list = Helper.BuyHandler.get_current_shoppinglist()
        self.info_list = Helper2.load.product_info(self, self.shopping_list) if self.shopping_list else []

        # UI neu laden
        self.load_ui()

    def convert_preis(self, row):

        preis = int(self.info_list[row][4])
        loss = int(Helper2.load.loss(self.info_list[row][0]))
        jahre = int(Helper.get_time_difference_since_program_time(f"{self.info_list[row][5]}-01-01 12:00:00"))
        verlustrate = (100 - loss) / 100
        conv_preis = int(float(preis) * float(verlustrate ** jahre))
        neu_preis = int(float(conv_preis) * 0.65) if self.acc[3] == "Admin" else int(conv_preis)

        self.info_list[row][4] = neu_preis
