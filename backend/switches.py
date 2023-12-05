import locale
import os.path
import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import Helper
from accessoriesWindow import accessoriesWindow
from Nutzerprofil import UserprofileWindow
from Produktansicht import ProductWindow
from Register import Register
from Startseite import Startseite

class switch_to:

    def accessories(self):
        accessories = accessoriesWindow(self.stacked_widget)
        self.stacked_widget.addWidget(accessories)
        self.stacked_widget.setCurrentWidget(accessories)

    def nutzer(self):
        user = UserprofileWindow(self.stacked_widget)
        self.stacked_widget.addWidget(user)
        self.stacked_widget.setCurrentWidget(user)

    def register(self):
        register = Register(self.stacked_widget)
        self.stacked_widget.addWidget(register)
        self.stacked_widget.setCurrentWidget(register)

    def startseite(self):
        startseite = Startseite(self.stacked_widget)
        self.stacked_widget.addWidget(startseite)
        self.stacked_widget.setCurrentWidget(startseite)

    def product(self):
        product = ProductWindow(self.stacked_widget)
        self.stacked_widget.addWidget(product)
        self.stacked_widget.setCurrentWidget(product)
