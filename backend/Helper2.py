import locale
import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import Helper_Accounts
import switches
import csv
import Helper

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class conf:

    @staticmethod
    def locale_setup(self):
        locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")


class replace:

    @staticmethod
    def text(self, new_text, label):
        label.setText(str(new_text))

    @staticmethod
    def img(self, image_name, label):
        pixmap = QPixmap(image_name)
        label.setPixmap(pixmap)

    @staticmethod
    def icon(self, icon_name, label):
        icon = QIcon(icon_name)
        label.setIcon(icon)

class load:

    def complete_header(self):
        replace.icon(self, os.path.join(ICON_PATH, r"home.svg"), self.findChild(QPushButton, "home_Button"))
        replace.icon(self, os.path.join(ICON_PATH, r"user.svg"), self.findChild(QPushButton, "acc_Button"))
        replace.icon(self, os.path.join(ICON_PATH, r"shopping-cart.svg"),
                     self.findChild(QPushButton, "shopping_Button"))

        conf.locale_setup(self)

        def getCurUser():
                return Helper_Accounts.UserHandler.get_current_user()[2]
        try:
            gCU = getCurUser()
        except:
            # No valid Userdata found. Probably index out of range
            replace.text(self, "Budget not found!", self.findChild(QLabel, "budget_label"))
        else:
            replace.text(self, str(locale.currency(int(gCU), grouping=True)), self.findChild(QLabel, "budget_label"))
            
        self.acc_Button.clicked.connect(lambda: switches.switch_to.nutzer(self))
        self.shopping_Button.clicked.connect(lambda: switches.switch_to.shopping_cart(self))
        self.home_Button.clicked.connect(lambda: switches.switch_to.startseite(self))



    def logout_button(self, button):
        button.clicked.connect(lambda: switches.switch_to.login(self))

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



    def product_pic(self, row):

        pfad = os.path.join(PIC_PATH, r"Traktoren")

        if row[2] == "z":
            pfad = os.path.join(PIC_PATH, r"Zubehör")

        gesucht = row[0]

        for dateiname in os.listdir(pfad):
            if gesucht in dateiname:
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
