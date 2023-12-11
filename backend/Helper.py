from PyQt5.QtCore import QTimer, QSize
from PyQt5.QtWidgets import QMessageBox
import csv
import os

CSV_PATH = os.path.join("..", "resources", "csv")


class UserHandler():
    current_user = []

    @staticmethod
    def get_current_user():
        return UserHandler.current_user

    @staticmethod
    def set_current_user(self, user):
        pfad = os.path.join(CSV_PATH, r"Accounts.csv")

        with open(pfad, mode="r") as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                if row[0] == user:
                    UserHandler.current_user = row
                    break


class AccessoriesHandler:
    current_acc: str = ""

    @staticmethod
    def get_current_acc():
        return AccessoriesHandler.current_acc

    @staticmethod
    def set_current_acc(Accessorie):
        AccessoriesHandler.current_acc = Accessorie


class ProductHandler:
    current_product: str = ""

    @staticmethod
    def get_current_product():
        return ProductHandler.current_product

    @staticmethod
    def set_current_product(product, anz):
        ProductHandler.current_product = product


class BuyHandler:
    current_shoppinglist = []

    @staticmethod
    def get_current_shoppinglist():
        return BuyHandler.current_shoppinglist

    @staticmethod
    def add_to_current_shoppinglist(product, anz, typ):
        for item in BuyHandler.current_shoppinglist:
            if product == item[0]:
                item[1] += anz
                break
        else:
            BuyHandler.current_shoppinglist.append([product, anz, typ])

    @staticmethod
    def remove_from_current_shoppinglist(product):
        if BuyHandler.current_shoppinglist:
            for item in BuyHandler.current_shoppinglist:
                if item[0] == product:
                    BuyHandler.current_shoppinglist.remove(item)
                    break


def show_toast(message, icon, button):
    toast = QMessageBox()
    toast.setIcon(icon)
    toast.setText(message)
    toast.setWindowTitle("Notification")
    toast.setStandardButtons(button)

    timer = QTimer(toast)
    # https://youtrack.jetbrains.com/issue/PY-24183/PyQt5-cannot-find-refernece-connect-in-funciton
    # https://stackoverflow.com/questions/64505166/cannot-find-reference-connect-in-function
    # noinspection PyUnresolvedReferences
    timer.timeout.connect(toast.close)
    timer.start(1750)

    toast.exec_()
