import locale
import os.path
import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize
import Helper
import Helper_Accounts
import switches
import Helper2

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class FullScreenImage(QMainWindow):
    def __init__(self, image_path):
        super().__init__()
        self.setGeometry(QApplication.desktop().screenGeometry())
        self.setWindowTitle("Full Screen Image")
        label = QLabel(self)
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        label.setAlignment(Qt.AlignCenter)
        label.mousePressEvent = self.close_fullscreen

    def close_fullscreen(self, event):
        self.close()


class ProductWindow(QMainWindow):
    def __init__(self):
        super().__init__() # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "ProductWindow.ui"), self)

        # Simulierte übergabeparameter
        platzhalter = Helper.ProductHandler.current_product

        platzhalter = Helper.ProductHandler.current_product
        product = Helper2.load.traktor_data(self, platzhalter)
        print(type(product))
        acc_platzhalter = Helper_Accounts.UserHandler.get_current_user()[0]  # bekommt acc von startseite
        acc = self.load_acc(acc_platzhalter)
        loss = int(self.load_loss(product[0]))
        z_list = self.load_zub(product[0])  # kompatibles Zubehoer []

        self.buttons = {}  # speichert array von buttonaktionen für dyn. layout
        self.anz = 0
            
        self.buttons = {}   # speichert array von buttonaktionen für dyn. layout
        self.anz = 0

        # Währungsumgebung laden
        Helper2.conf.locale_setup(self)

        # dynamisches Widget laden
        self.add_widget(z_list, product)

        # Produktseite laden
        if product is None: product = [i*0 for i in range(10)]
        self.load_ui(product, acc)
        self.load_lager(product)
        self.load_pic(product)

        # Aktionen
        self.buy_Button.clicked.connect(lambda: self.buy(product[1], self.anz))
        self.spinBox.valueChanged.connect(lambda value: self.calc_wert(product[4], loss, value))
        self.spinBox_2.valueChanged.connect(lambda value: self.set_anz(value))


        # Connect the mousePressEvent to the picture label
        picture_label = self.findChild(QLabel, "picture")
        picture_label.mousePressEvent = lambda event: self.show_fullscreen(event, picture_label.pixmap())

        self.show()

    @staticmethod
    def show_fullscreen(event, pixmap):
        if event.button() == Qt.LeftButton:
            fullscreen_window = FullScreenImage(pixmap)
            fullscreen_window.show()

    def load_ui(self, product, user):
        Helper2.conf.locale_setup(self)
        Helper2.replace.text(self,
            f"{product[0]} - {product[1]}", self.findChild(QLabel, "name_label")
        )
        Helper2.replace.text(self,
            locale.currency(int(product[4]), grouping=True), self.findChild(QLabel, "preis_status")
        )
        Helper2.replace.text(self, product[2], self.findChild(QLabel, "ps_status"))
        Helper2.replace.text(self, product[3], self.findChild(QLabel, "kmh_status"))
        Helper2.replace.text(self, product[5], self.findChild(QLabel, "baujahr_status"))
        Helper2.load.complete_header(self)

    def set_anz(self, value):
        self.anz = value
        print(self.anz)

    def load_zub(self, model):
        pfad = os.path.join(CSV_PATH, r"Zubehör.csv")

        with open(pfad, mode="r") as file:
            csv_reader = csv.reader(file)
            data_list = []  # welche werte wichtig? andere methode? ohne zwischenspeicher?

            for row in csv_reader:
                for column in row:
                    if model == column:
                        data_list.append(row)
                        break

            print(data_list)  # zu testzweck
            return data_list

    def load_loss(self, platzhalter):
        pfad = os.path.join(CSV_PATH, r"Wertminderung.csv")
        with open(pfad, mode="r") as file:
            for row in csv.reader(file):
                if row[0] == platzhalter:
                    return int(row[1])
            return 0
        
    def load_lager(self, row):
        if int(row[6]) > 0:
            Helper2.replace.img(self,
                os.path.join(ICON_PATH, r"check.svg"),
                self.findChild(QLabel, "bestand_icon")
            )
            return True
        else:
            Helper2.replace.img(self,
                os.path.join(ICON_PATH, r"cross.svg"),
                self.findChild(QLabel, "bestand_icon")
            )
            self.buy_Button.setDisabled(True)
            Helper2.replace.text(self, "ausverkauft", self.findChild(QPushButton, "buy_Button"))
            return False

    def load_pic(self, row):
        gesucht = str(row[1])
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
            label3 = QLabel(locale.currency(int(zusatz[x][1]), grouping=True))

            button = QPushButton("Mehr info")
            self.buttons[x] = button

            button.clicked.connect(self.make_button_click_handler(label1))

            inner_layout.addWidget(label1)
            inner_layout.addWidget(label2)
            inner_layout.addWidget(label3)
            inner_layout.addWidget(button)

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

    def calc_wert(self, product, loss, jahre):
        normalPreis = int(product)
        verlustRate = (100-loss)/100
        new_value = normalPreis * (verlustRate)**jahre
        # Zinseszinzprinzip:
        # Endbetrag = Kapital×(Zinsesrate) hoch Jahresanzahl
        
        Helper2.replace.text(self, 
                             locale.currency(new_value, grouping=True),
                             self.findChild(QLabel, "wert_status"),
        )

    @staticmethod
    def buy(model, anz):  # weiterleiten an warenkorb mit parameter (user name, product modell)
        if anz > 0:
            # TODO toast: sie haben x Model gekauft
            Helper.show_toast(f"Sie haben {anz}x {model} dem Warenkorb hinzugefügt.", QMessageBox.Information,
                              QMessageBox.Ok, 2000)
            print("aufruf buy()")
            Helper.BuyHandler.add_to_current_shoppinglist(model, anz, "t")
            print(Helper.BuyHandler.get_current_shoppinglist())
