import locale
import os.path

from PyQt5 import uic
from PyQt5.QtWidgets import *

import Helper
import Helper2
import Helper_Accounts
import switches

CSV_PATH = os.path.join("..", "resources", "csv")
PIC_PATH = os.path.join("..", "resources", "pictures")
ICON_PATH = os.path.join("..", "resources", "icons")


class SellWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Sell.ui"), self)

        # Übergabeparameter
        Helper.InvHandler.def_inv()
        self.inventar_liste = Helper.InvHandler.get_inv()
        print(self.inventar_liste)
        self.info_liste = Helper2.load.product_info(self, self.inventar_liste)
        print(self.info_liste)
        self.bidders_liste = Helper_Accounts.get_bidders()

        # Lokale Währungsumgebung laden
        Helper2.conf.locale_setup(self)

        # Signale
        self.t_Button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.z_Button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        # Buttons von dyn. Layout
        self.buttons_tab1 = {}

        # UI laden
        self.load_ui()

        self.showFullScreen()
        self.show()

    def load_ui(self):

        Helper2.load.complete_header(self)
        self.create_content()
        self.add_bidders_tab()

    def create_content(self):

        scroll_area = self.findChild(QScrollArea, "scrollArea")
        scroll_area2 = self.findChild(QScrollArea, "scrollArea_2")

        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        content_widget2 = QWidget()
        layout2 = QVBoxLayout(content_widget2)

        for x in range(len(self.inventar_liste)):
            new_widget = QWidget()
            new_widget.setMaximumHeight(200)
            new_widget.setStyleSheet("""
                QWidget {
                    border-radius: 10px; 
                    border: 2px solid rgb(46, 204, 113);
                }
            """)
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
                label2 = QLabel(f"Zubehör | {self.inventar_liste[x][0]}")
            else:
                label2 = QLabel()
            label2.setStyleSheet("color: white; font-size: 16px; font-weight: 500; border: none;")
            info_layout.addWidget(label2, 1)

            desc_layout = QVBoxLayout()
            info_layout.addLayout(desc_layout, 3)

            if self.inventar_liste[x][2] == "z":
                pass
            else:
                ps = QLabel(f"PS: {self.info_liste[x][2]}")
                km = QLabel(f"Km/h: {self.info_liste[x][3]}")
                baujahr = QLabel(f"Baujahr: {self.info_liste[x][5]}")

                ps.setStyleSheet("color: white; font-size: 16px; font-weight: 500; border: none;")
                km.setStyleSheet("color: white; font-size: 16px; font-weight: 500; border: none;")
                baujahr.setStyleSheet("color: white; font-size: 16px; font-weight: 500; border:none;")

                desc_layout.addWidget(ps)
                desc_layout.addWidget(km)
                desc_layout.addWidget(baujahr)

            value_layout = QVBoxLayout()
            inner_layout.addLayout(value_layout, 3)

            anz_layout = QHBoxLayout()
            value_layout.addLayout(anz_layout)

            label4 = QLabel(f"Im Besitz: {self.inventar_liste[x][1]} Stück")
            label4.setStyleSheet("color: white; font-size: 16px; font-weight: 500; border: none;")

            spinbox = QSpinBox()
            spinbox.setSuffix(" Stück")
            spinbox.setPrefix("    ")
            spinbox.setMaximum(int(self.inventar_liste[x][1]))

            spinbox.setStyleSheet("""
                background-color: rgb(109, 135, 100);
                color: white;
                min-height: 30px;
                font-size: 16px;
                font-weight: 500;
                border: none;
                border-radius: none;
            """)
            label5 = QPushButton("Verkaufen")

            label5.setStyleSheet("""
                QPushButton {
                    background-color: rgb(230, 126, 34);
                    border-radius: 10px;
                    min-height: 35px;
                    color: white;
                    font-size: 16px;
                    font-weight: 500;
                    border:none;
                }
                QPushButton:hover {
                    cursor: pointer;
                    background-color: rgb(241, 196, 15);
                }
                
                QPushButton:pressed {
                    padding-left: 3px;
                    padding-bottom: 3px;
                }
            """)
            self.buttons_tab1[x] = label5
            label5.clicked.connect(lambda nr=x, label=self.inventar_liste[x][0], typ=self.inventar_liste[x][2],
                                          zeit=self.inventar_liste[x][4], user=self.inventar_liste[x][3],
                                          spin=spinbox: self.make_button_click_handler(label, spin.value(), typ, user,
                                                                                       zeit))

            value_innerlayout = QHBoxLayout()

            label6 = QLabel(f"Wert: {locale.currency(int(self.convert_preis(x)), grouping=True)}")

            label6.setStyleSheet("color: red; font-size: 16px; font-weight: 500; border:none;")

            label7 = QLabel(
                f"Alter: {int(Helper.get_time_difference_since_program_time(self.inventar_liste[x][4]))} Jahre")
            label7.setStyleSheet("color: white; font-size: 16px; font-weight: 500; border: none;")

            value_innerlayout.addWidget(label7)
            value_innerlayout.addWidget(label6)

            anz_layout.addWidget(label4)
            anz_layout.addWidget(spinbox)

            value_layout.addWidget(label5)
            value_layout.addLayout(value_innerlayout)

            if self.inventar_liste[x][2] == "t":
                layout.addWidget(new_widget)
            else:
                layout2.addWidget(new_widget)

        scroll_area.setWidget(content_widget)
        scroll_area2.setWidget(content_widget2)

    def add_bidders_tab(self):

        scroll_area = self.findChild(QScrollArea, "bidders_scrollArea")
        scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: rgb(52, 73, 94);
                border: 4px solid rgb(46, 204, 113);
                border-radius: 10px;
            }
        """)
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: rgb(52, 73, 94);")
        layout = QVBoxLayout(content_widget)

        for item in self.bidders_liste:
            new_widget = QWidget()
            new_widget.setMaximumHeight(100)

            inner_layout = QHBoxLayout(new_widget)

            label1 = QLabel(item[0])
            label1.setStyleSheet("color: white; font-size: 16px; font-weight: 500; border: none;")
            label2 = QLabel(locale.currency(int(item[3]), grouping=True))
            label2.setStyleSheet("color: white; font-size: 16px; font-weight: 500;")
            inner_layout.addWidget(label1)
            inner_layout.addWidget(label2)

            layout.addWidget(new_widget)

        scroll_area.setWidget(content_widget)

    def make_button_click_handler(self, label, anz, typ, user, zeit):

        if anz > 0:
            print(self.inventar_liste[0])
            Helper.current_Sell_Handler.add_sell_item(label, anz, typ, user, zeit)
            if typ == "t":
                switches.switch_to.Sell_item()
            else:
                switches.switch_to.Sell_item_Access()

    def convert_preis(self, row):

        preis = int(self.info_liste[row][4]) if self.inventar_liste[row][2] == "t" else int(self.info_liste[row][1])
        loss = int(Helper2.load.loss(self.info_liste[row][0])) if self.inventar_liste[row][2] == "t" else int(
            Helper2.load.loss("Zusatz"))
        jahre_anz = self.inventar_liste[row][4] if self.inventar_liste[row][2] == "z" else f"{self.info_liste[row][-2]}-01-01 12:00:00"
        jahre = int(Helper.get_time_difference_since_program_time(jahre_anz))
        verlustrate = (100 - loss) / 100
        conv_preis = int(float(preis) * float(verlustrate ** jahre))
        neu_preis = int(conv_preis)

        return neu_preis
