import csv
import locale
import os.path

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Helper_Accounts
import switches

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class conf:

    @staticmethod
    def locale_setup(self):
        locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")


class replace:

    @staticmethod
    def text(new_text, label):
        label.setText(str(new_text))

    @staticmethod
    def img(image_name, label):
        pixmap = QPixmap(image_name)
        label.setPixmap(pixmap)

    @staticmethod
    def icon(icon_name, label):
        icon = QIcon(icon_name)
        label.setIcon(icon)

class load:

    def complete_header(self):
        def replace_icon(button, icon_path):
            button_widget = self.findChild(QPushButton, button)
            if button_widget:
                replace.icon(os.path.join(ICON_PATH, icon_path), button_widget)
                return True
            return False

        conf.locale_setup(self)

        def set_budget_label():
            try:
                gCU = Helper_Accounts.UserHandler.get_current_user()[2]
                replace.text(str(locale.currency(int(gCU), grouping=True)), self.findChild(QLabel, "budget_label"))
            except Exception as e:
                print(f"Error fetching user data: {e}")
                replace.text("Budget not found!", self.findChild(QLabel, "budget_label"))

        if replace_icon("home_Button", r"home.svg"):
            self.home_Button.clicked.connect(lambda: switches.switch_to.startseite())
        if replace_icon("acc_Button", r"user.svg"):
            self.acc_Button.clicked.connect(lambda: switches.switch_to.nutzer(self))
        if replace_icon("shopping_Button", r"shopping-cart.svg"):
            self.shopping_Button.clicked.connect(lambda: switches.switch_to.shopping_cart())

        set_budget_label()


    def traktor_data(self, model):
        csv_path = os.path.join(CSV_PATH, r"mobile Arbeitsmaschinen Landwirtschaft.csv")
        with open(csv_path, mode="r") as file:
            for row in csv.reader(file):
                if row[1] == model:
                    return row
            
    def zub_data(self, model):
        pfad = os.path.join(CSV_PATH, r"Zubehör.csv")
        with open(pfad, mode="r") as file:
            for row in csv.reader(file):
                for column in row:
                    if model == column:
                        return row

    @staticmethod
    def loss(hersteller):
        pfad = os.path.join(CSV_PATH, r"Wertminderung.csv")
        with open(pfad, mode="r") as file:
            for row in csv.reader(file):
                if row[0] == hersteller:
                    return int(row[1])
            return 0

    def all_traktor_data(self):
        liste = []

        csv_path = os.path.join(CSV_PATH, r"mobile Arbeitsmaschinen Landwirtschaft.csv")
        with open(csv_path, mode="r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Überspringe die erste Zeile
            for row in csv_reader:
                liste.append([row[1], "1", "t"])

        print("TEST LISTE")
        print(liste)
        return liste

    def all_zubehoer_data(self):
        liste = []

        pfad = os.path.join(CSV_PATH, r"Zubehör.csv")
        with open(pfad, mode="r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Überspringe die erste Zeile
            for row in csv_reader:
                liste.append([row[0], "1", "z"])

        return liste


    def product_pic(self, row):

        pfad = os.path.join(PIC_PATH, r"Traktoren")

        if row[2] == "z":
            pfad = os.path.join(PIC_PATH, r"Zubehör")

        gesucht = row[0]

        for dateiname in os.listdir(pfad):
            if gesucht.lower() in dateiname.lower():
                voll_pfad = os.path.join(pfad, dateiname)
                pixmap = QPixmap(voll_pfad)
                return pixmap


    def product_info(self, liste):
        info = []
        for x in range(len(liste)):
            if liste[x][2] == "t":
                info.append(load.traktor_data(self, liste[x][0]))
            if liste[x][2] == "z":
                info.append(load.zub_data(self, liste[x][0]))

        return info
