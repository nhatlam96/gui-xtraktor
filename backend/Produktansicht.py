import locale
import os
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic, Qt
from PyQt5.QtGui import *


CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class ProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi(r"..\frontend\ProductWindow.ui", self)
        uic.loadUi(os.path.join("..", "frontend", "ProductWindow.ui"), self)
        # Simulierte übergabeparameter
        platzhalter = "9R_RT"
        product = self.load_data(platzhalter)
        acc_platzhalter = "Sieglinde"
        acc = self.load_acc(acc_platzhalter)
        loss = int(self.load_loss(product[0]))
        z_list = self.load_zub(product[0])  # kompatibles Zubehoer []

        # Währungsumgebung laden
        self.locale_setup()

        # dynamisches Widget laden
        self.add_widget(z_list, product)

        # Produktseite laden
        self.load_ui(product, acc)
        self.load_lager(product)
        self.load_pic(product)

        # Aktionen
        self.buy_Button.clicked.connect(self.buy)
        self.spinBox.valueChanged.connect(
            lambda value: self.calc_wert(product[4], loss, value)
        )
        self.shopping_Button.clicked.connect(lambda: self.change_widget("test", "Home"))
        self.acc_Button.clicked.connect(lambda: self.change_widget("test", "Home"))
        self.home_Button.clicked.connect(lambda: self.change_widget("test", "Home"))

        self.show()

    def locale_setup(self):
        locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")

    def replace_text(self, new_text, label):
        label.setText(new_text)

    def replace_img(self, image_name, label):
        pixmap = QPixmap(image_name)
        label.setPixmap(pixmap)

    def replace_icon(self, icon_name, label):
        icon = QIcon(icon_name)
        label.setIcon(icon)

    def load_ui(self, product, user):
        self.replace_text(
            f"{product[0]} - {product[1]}", self.findChild(QLabel, "name_label")
        )
        self.replace_text(
            locale.currency(int(product[4].replace(".", "")), grouping=True),
            self.findChild(QLabel, "preis_status"),
        )
        self.replace_text(
            f"Budget:  {locale.currency(int(user[2]), grouping=True)}",
            self.findChild(QLabel, "budget_label"),
        )
        self.replace_text(product[2], self.findChild(QLabel, "ps_status"))
        self.replace_text(product[3], self.findChild(QLabel, "kmh_status"))
        self.replace_text(product[5], self.findChild(QLabel, "baujahr_status"))
        self.replace_icon(
            os.path.join(ICON_PATH, r"home.svg"),
            self.findChild(QPushButton, "home_Button"),
        )
        self.replace_icon(
            os.path.join(ICON_PATH, r"user.svg"),
            self.findChild(QPushButton, "acc_Button"),
        )
        self.replace_icon(
            os.path.join(ICON_PATH, r"shopping-cart.svg"),
            self.findChild(QPushButton, "shopping_Button"),
        )

    def load_data(self, placeholder):
        csv_path = os.path.join(CSV_PATH, r"mobile Arbeitsmaschinen Landwirtschaft.csv")

        with open(csv_path, mode="r") as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                if row[1] == placeholder:
                    return row

    def load_zub(self, model):
        pfad = os.path.join(CSV_PATH, r"Zubehör.csv")

        with open(pfad, mode="r") as file:
            csv_reader = csv.reader(file)
            data_list = (
                []
            )  # welche werte wichtig? andere methode? ohne zwischenspeicher?

            for row in csv_reader:
                for column in row:
                    if model == column:
                        data_list.append(row)
                        break

            print(data_list)  # zu testzweck
            return data_list

    def load_loss(self, platzhhalter):
        pfad = os.path.join(CSV_PATH, r"Wertminderung.csv")

        with open(pfad, mode="r") as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                if row[0] == platzhhalter:
                    return row[1]

    def load_lager(self, row):
        if int(row[6]) > 0:
            self.replace_img(
                os.path.join(ICON_PATH, r"check.svg"),
                self.findChild(QLabel, "bestand_icon"),
            )
            return True
        else:
            self.replace_img(
                os.path.join(ICON_PATH, r"cross.svg"),
                self.findChild(QLabel, "bestand_icon"),
            )
            self.buy_Button.setDisabled(True)
            self.replace_text("ausverkauft", self.findChild(QPushButton, "buy_Button"))
            return False

    def load_pic(self, row):
        gesucht = row[1]
        pfad = os.path.join(PIC_PATH, r"Traktoren")

        for dateiname in os.listdir(pfad):
            if gesucht in dateiname:
                voll_pfad = os.path.join(pfad, dateiname)
                self.replace_img(voll_pfad, self.findChild(QLabel, "picture"))

    def load_zpic(self, name):
        gesucht = name
        pfad = os.path.join(PIC_PATH, r"Zubehör")

        for dateiname in os.listdir(pfad):
            if gesucht in dateiname:
                voll_pfad = os.path.join(pfad, dateiname)
                pixmap = QPixmap(voll_pfad)
                scaled_pixmap = pixmap.scaled(64, 64)
                return scaled_pixmap

    def load_acc(self, user):
        pfad = os.path.join(CSV_PATH, r"Accounts.csv")

        with open(pfad, mode="r") as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                if row[0] == user:
                    return row

    def add_widget(self, zusatz, product):
        # dynamisches Layout laden
        scroll_area = self.findChild(QScrollArea, "dyn_scrollarea")

        # neues Widget als Container für einzelne Widgets
        content_widget = QWidget()

        # QHBoxLayout erstellen für Container
        layout = QHBoxLayout(content_widget)

        for x in range(len(zusatz)):
            new_widget = QWidget()
            inner_layout = QVBoxLayout(new_widget)  # v-layout für widget

            label1 = QLabel(zusatz[x][0])
            label2 = QLabel()
            label2.setPixmap(self.load_zpic(zusatz[x][0]))
            label3 = QLabel(locale.currency(int(zusatz[x][-2]), grouping=True))

            button1 = QPushButton("Mehr info")

            inner_layout.addWidget(label1)
            inner_layout.addWidget(label2)
            inner_layout.addWidget(label3)
            inner_layout.addWidget(button1)

            layout.addWidget(new_widget)  # widget dem container hinzufuegen

            # erstellten Container einfuegen in QScrollArea
            scroll_area.setWidget(content_widget)

    """ # feature muss noch überarbeitet werden
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.showFullScreen()
            self.picture.setPixmap(self.picture.pixmap().scaledToWidth(self.width()))  # Bild auf die Fensterbreite skalieren
    """

    def calc_wert(self, product, loss, value):
        preis = int(product.replace(".", ""))
        new_value = (
            -(value * (preis * loss / 100))
            if (value * (preis * loss / 100)) < preis
            else -preis
        )
        self.replace_text(
            locale.currency(new_value, grouping=True),
            self.findChild(QLabel, "wert_status"),
        )

    def buy(
        self, acc
    ):  # weiterleiten an warenkorb mit parameter (user name, product modell)
        pass  # Warenkorb.ui nötig

    def change_widget(self, acc, page):  # page = wohin als nächstes
        pass


def main():
    app = QApplication([])
    window = ProductWindow()
    app.exec_()


main()
