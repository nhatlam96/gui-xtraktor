import locale
import os.path
import csv

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import Helper_Accounts
import Helper
import switches
import Helper2

from Vollbild_Klasse import FullScreenImage

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class ProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "ProductWindow.ui"), self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)

        print("AUFRUF PRODUKT")

        # übergabeparameter
        self.product = Helper2.load.traktor_data(self, Helper.ProductHandler.current_product)
        self.loss = int(Helper2.load.loss(self.product[0]))
        self.z_list = self.load_zub()    # kompatibles. Zubehör
        self.acc = Helper_Accounts.UserHandler.get_current_user()

        # dyn. Layout
        self.buttons = {}   # speichert dict von Button-aktionen für dyn. layout
        self.anz = 0

        # Währungsumgebung laden
        Helper2.conf.locale_setup(self)

        # dynamisches Widget laden
        self.add_widget()

        # Produktseite laden
        self.load_ui()
        self.load_pic(self.product)

        # Aktionen
        self.buy_Button.clicked.connect(lambda: self.buy(self.product[1], self.anz))
        self.wert_spinBox.valueChanged.connect(lambda value: self.calc_wert(value))
        self.anz_spinBox.valueChanged.connect(lambda value: self.check_quantity(value))

        # Mausevent mit Bild verknüpfen
        picture_label = self.findChild(QLabel, "picture")
        picture_label.mousePressEvent = lambda event: self.show_fullscreen(event, picture_label.pixmap())

        self.show()

    def closeEvent(self, event):
        print("Window is closing")
        switches.WindowHandler.release_window(ProductWindow)
        super().closeEvent(event)  # Fenster wird wirklich geschlossen

    @staticmethod
    def show_fullscreen(event, pixmap):
        FullScreenImage.show_fullscreen(event, pixmap)

    def load_ui(self):
        Helper2.conf.locale_setup(self)
        Helper2.replace.text(f"{self.product[0]} - {self.product[1]}",
                             self.findChild(QLabel, "name_label"))
        Helper2.replace.text(locale.currency(int(self.get_preis()), grouping=True),
                             self.findChild(QLabel, "preis_status"))
        Helper2.replace.text(self.product[2], self.findChild(QLabel, "ps_status"))
        Helper2.replace.text(self.product[3], self.findChild(QLabel, "kmh_status"))
        Helper2.replace.text(self.product[5], self.findChild(QLabel, "baujahr_status"))
        Helper2.load.complete_header(self)

        if Helper_Accounts.UserHandler.get_current_user()[3] == "Admin":
            Helper2.replace.text("nachbestellen", self.findChild(QPushButton, "buy_Button"))
            Helper2.replace.text(self.product[6], self.findChild(QLabel, "bestand_icon"))
            self.findChild(QLabel, "bestand_icon").setStyleSheet("""
                color: white; font-size: 20px; font-weight: 700;
            """)
            self.preis_label.setText("EK-Stückpreis:")
        else:
            self.load_lager()

    def calc_preis(self, value):

        preis = self.get_preis()
        new_value = preis * value
        Helper2.replace.text(locale.currency(new_value, grouping=True), self.findChild(QLabel, "ges_status"))

    def get_preis(self):
        jahre = int(Helper.get_time_difference_since_program_time(f"{self.product[5]}-01-01 12:00:00"))
        verlustrate = (100 - self.loss) / 100
        preis = int(float(self.product[4]) * float(verlustrate ** jahre))  # ** -> Potenz
        neu_preis = int(float(preis) * 0.65) if self.acc[3] == "Admin" else int(preis)

        return neu_preis

    def calc_wert(self, jahre):
        normalpreis = int(float(self.product[4]) * 0.65) if self.acc[3] == "Admin" else int(self.product[4])
        verlustrate = (100 - self.loss) / 100
        new_value = int(normalpreis * (verlustrate ** jahre))  # ** -> Potenz
        Helper2.replace.text(locale.currency(new_value - normalpreis, grouping=True),
                             self.findChild(QLabel, "wert_status"))
        Helper2.replace.text(locale.currency(new_value, grouping=True), self.findChild(QLabel, "rest_status"))

    def load_zub(self):
        pfad = os.path.join(CSV_PATH, r"Zubehör.csv")

        with open(pfad, mode="r") as file:
            csv_reader = csv.reader(file)
            data_list = []
            for row in csv_reader:
                for column in row:
                    if self.product[0] == column:
                        data_list.append(row)
                        break

            return data_list

    def load_lager(self):
        if int(self.product[6]) > 0:
            Helper2.replace.img(os.path.join(ICON_PATH, r"check.svg"), self.findChild(QLabel, "bestand_icon"))
            self.bestand_icon.setMaximumSize(32, 32)
            return True
        else:
            Helper2.replace.img(os.path.join(ICON_PATH, r"cross.svg"), self.findChild(QLabel, "bestand_icon"))
            self.bestand_icon.setMaximumSize(32, 32)
            self.buy_Button.setDisabled(True)
            Helper2.replace.text("ausverkauft", self.findChild(QPushButton, "buy_Button"))
            return False

    def load_pic(self, row):
        gesucht = str(row[1])

        pfad = os.path.join(PIC_PATH, r"Traktoren")
        for dateiname in os.listdir(pfad):
            if gesucht in dateiname:
                voll_pfad = os.path.join(pfad, dateiname)
                Helper2.replace.img(voll_pfad, self.findChild(QLabel, "picture"))

    @staticmethod
    def load_zpic(name):
        gesucht = name
        pfad = os.path.join(PIC_PATH, r"Zubehör")

        for dateiname in os.listdir(pfad):
            if gesucht in dateiname:
                voll_pfad = os.path.join(pfad, dateiname)
                pixmap = QPixmap(voll_pfad)
                scaled_pixmap = pixmap.scaled(64, 64)
                return scaled_pixmap

    @staticmethod
    def load_acc(user):
        pfad = os.path.join(CSV_PATH, r"Accounts.csv")

        with open(pfad, mode="r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == user:
                    return row

    def add_widget(self):

        scroll_area = self.findChild(QScrollArea, "dyn_scrollarea")

        # neues Widget als Container für einzelne Widgets
        content_widget = QWidget()
        layout = QHBoxLayout(content_widget)

        for x in range(len(self.z_list)):

            # neues Widget für jedes Item
            new_widget = QWidget()
            inner_layout = QVBoxLayout(new_widget)  # v-layout für widget
            new_widget.setStyleSheet("""
                QWidget {
                       border: 2px solid rgb(127, 140, 141);
                       border-radius: 5px;
                }
            """)

            label1 = QLabel(self.z_list[x][0])
            label1.setStyleSheet("color: white; font-size: 16px; font-weight: 500; border: none;")
            label2 = QLabel()
            label2.setStyleSheet("border: none;")
            label2.setPixmap(self.load_zpic(self.z_list[x][0]))
            if self.acc[3] == "Admin":
                label3 = QLabel(f"EK-P: {locale.currency(int(float(self.z_list[x][1]) * 0.65), grouping=True)}")
            else:
                label3 = QLabel(f"{locale.currency(int(self.z_list[x][1]), grouping=True)}")
            label3.setStyleSheet("color: white; font-size: 16px; font-weight: 500; border: none;")
            button = QPushButton("Mehr info")
            button.setStyleSheet("""
                 QPushButton{
                    border-radius: 10px;
                    background-color: rgb(100, 221, 23);
                    color: white;
                    font-weight: bold;
                    min-height: 30px;
                    border: none;
                }
                QPushButton:hover {
                    background-color: rgb(178, 255, 89);
                    opacity: 0.8;
                }
                QPushButton:pressed {
                    padding-left: 3px;
                    padding-bottom: 3px;
                }
            """)
            self.buttons[x] = button

            button.clicked.connect(self.button_handler(label1))

            inner_layout.addWidget(label1)
            inner_layout.addWidget(label2)
            inner_layout.addWidget(label3)
            inner_layout.addWidget(button)

            layout.addWidget(new_widget)  # widget dem container hinzufügen

            # erstellten Container einfügen in QScrollArea
            scroll_area.setWidget(content_widget)

    @staticmethod
    def button_handler(label):
        def button_click_handler():
            if label is not None:
                Helper.AccessoriesHandler.set_current_acc(label.text())
                switches.switch_to.accessories()
            else:
                print("Label ist None")

        return button_click_handler

    def check_quantity(self, value):
        print(f"Produktansicht: {self.product}")
        available_quantity = int(self.product[6])
        current_shopping_list = Helper.BuyHandler.get_current_shoppinglist()

        total_quantity = sum(item[1] for item in current_shopping_list if item[0] == self.product[1])

        if total_quantity + value > available_quantity:
            adjusted_quantity = min(value, available_quantity - total_quantity)
            self.anz_spinBox.setValue(adjusted_quantity)
            self.anz = adjusted_quantity
            message = f"Not enough quantity in the Lager for {self.product[1]}."
            Helper.show_toast(message, QMessageBox.Warning, QMessageBox.Ok, 2300)
        else:
            self.anz_spinBox.setValue(value)
            self.anz = value

    def buy(self, model, anz):
        if anz > 0:
            current_shopping_list = Helper.BuyHandler.get_current_shoppinglist()

            # falls vorhanden, Anzahl in shopping liste erhöhen
            for item in current_shopping_list:
                if item[0] == model:
                    item[1] += anz
                    Helper.show_toast(f"Quantität von {model} im Warenkorb wurde aktualisiert.",
                                      QMessageBox.Information, QMessageBox.Ok, 1750)
                    self.anz_spinBox.setValue(0)
                    print(Helper.BuyHandler.get_current_shoppinglist())
                    return

            # neues Produkt dem Warenkorb hinzufügen
            Helper.show_toast(f"Sie haben {anz}x {model} dem Warenkorb hinzugefügt.",
                              QMessageBox.Information, QMessageBox.Ok, 2500)
            Helper.BuyHandler.add_to_current_shoppinglist(model, anz, "t")
            self.anz_spinBox.setValue(0)
            print(Helper.BuyHandler.get_current_shoppinglist())
        else:
            Helper.show_toast("Bitte Quantität erhöhen", QMessageBox.Warning, QMessageBox.Ok, 1750)
