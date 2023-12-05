from PyQt5.QtCore import QTimer, QSize
from PyQt5.QtWidgets import QMessageBox

class UserHandler():
    current_user: str = ""

    @staticmethod
    def get_current_user():
        return UserHandler.current_user

    @staticmethod
    def set_current_user(self, user):
        UserHandler.current_user = user


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
    def add_to_current_shoppinglist(product):
        BuyHandler.current_shoppinglist.append(product)

    @staticmethod
    def remove_from_current_shoppinglist(product):
        BuyHandler.current_shoppinglist.remove(product)




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
    
    

    


