import os.path
import sys
import locale
import Helper, Helper2, Helper3

from PyQt5.QtWidgets import *
from PyQt5 import uic
    
class WarenkorbWindow(QMainWindow):
    def __init__(self):
        super().__init__() # vereinfacht das Erstellen weiterer Subklassen
        uic.loadUi(os.path.join("..", "frontend", "Warenkorb.ui"), self)


        Helper2.conf.locale_setup(self)
        Helper2.load.complete_header(self)

        # shopping_list = Helper.BuyHandler.get_current_shoppinglist()
        shopping_list = [["Fendt","Vario_1050","521","60","367000","2015","8"],
                         ["Fendt","Vario_1038","395","60","298000","2015","2"]]     # zu Testzwecke

        self.add_widget(shopping_list)

        self.show()

    def add_widget(self, liste):
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

            label1 = QLabel("Bild")
            picture_layout.addWidget(label1)

            info_layout = QVBoxLayout()
            inner_layout.addLayout(info_layout)

            label2 = QLabel("Name")
            label3 = QLabel("Beschreibung")

            info_layout.addWidget(label2)
            info_layout.addWidget(label3)


            value_layout = QVBoxLayout()
            inner_layout.addLayout(value_layout)

            label4 = QSpinBox()
            label5 = QPushButton("Entfernen")
            label6 =QLabel("Preis")

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
            else:
                print("Label ist None")

        return button_click_handler





# if main program, run app, otherwise just import class
if __name__ == "__main__":
    app = QApplication(sys.argv) # construct QApp before QWidget
    window = WarenkorbWindow()
    window.show()  # class Mainwindow aufrufen
    sys.exit(app.exec_()) # exit cleanly


