import locale
import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import switches
import csv
import Helper

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


# Wie Helper, aber besser


class conf:

    @staticmethod
    def locale_setup(self):
        locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")


class replace:

    @staticmethod
    def text(self, new_text, label):
        label.setText(new_text)

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


        # Brauche Starteseite ... immernoch zu viele abhängigkeiten
        """replace.text(self, str(locale.currency(int(Helper.UserHandler.get_current_user()[2]), grouping=True)),
                             self.findChild(QLabel, "budget_label")
                             )"""

        self.acc_Button.clicked.connect(lambda: switches.switch_to.nutzer(self))
        self.shopping_Button.clicked.connect(lambda: switches.switch_to.shopping_cart(self))
        self.home_Button.clicked.connect(lambda: switches.switch_to.startseite(self))

    def logout_button(self, button):
        button.clicked.connect(lambda: switches.switch_to.login(self))

    def traktor_data(self, placeholder):
        csv_path = os.path.join(CSV_PATH, r"mobile Arbeitsmaschinen Landwirtschaft.csv")

        with open(csv_path, mode="r") as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                if row[1] == placeholder:
                    return row

    def zub_data(self, model):
        pfad = os.path.join(CSV_PATH, r"Zubehör.csv")

        with open(pfad, mode="r") as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                for column in row:
                    if model == column:
                        return row

