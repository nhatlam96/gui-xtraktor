import os

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

CSV_PATH = os.path.join("..", "resources", "csv")


class AccessoriesHandler:
    current_acc: str = ""

    @staticmethod
    def get_current_acc():
        return AccessoriesHandler.current_acc

    @staticmethod
    def set_current_acc(Accessory):
        AccessoriesHandler.current_acc = Accessory


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


def show_toast(message, icon, button, time_in_ms):
    toast = QMessageBox()
    toast.setText(message)
    toast.setIcon(icon)
    toast.setStandardButtons(button)
    toast.setWindowTitle("Notification")

    timer = QTimer(toast)
    # https://stackoverflow.com/questions/64505166/cannot-find-reference-connect-in-function
    # noinspection PyUnresolvedReferences
    timer.timeout.connect(toast.close)
    timer.start(time_in_ms)

    toast.exec_()


def show_toast_confirmation(self, question):
    return QMessageBox.question(self, "Confirmation", question, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
