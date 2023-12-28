from Nutzerprofil import UserprofileWindow
from Produktansicht import ProductWindow
from Register import Register
from Startseite import Startseite
from accessoriesWindow import accessoriesWindow
from Login import Login
from Warenkorb import WarenkorbWindow
from Sell import SellWindow
from Gebrauchtwaren import GebrauchtwarenWindow

"""from GebrauchtwarenAccessories import GebrauchtwarenWindowAccessories"""


class switch_to:

    @staticmethod
    def register(old_window):
        if old_window is not None:
            old_window.close()
        Register()

    @staticmethod
    def product(old_window):
        if old_window is not None:
            old_window.close()
        ProductWindow()

    @staticmethod
    def startseite(old_window):
        if old_window is not None:
            old_window.close()
        Startseite()

    @staticmethod
    def login(old_window):
        if old_window is not None:
            old_window.close()
        Login()

    @staticmethod
    def nutzer(old_window):
        if old_window is not None:
            old_window.close()
        UserprofileWindow()

    @staticmethod
    def accessories(old_window):
        if old_window is not None:
            old_window.close()
        accessoriesWindow()

    @staticmethod
    def shopping_cart(old_window):
        if old_window is not None:
            old_window.close()
        WarenkorbWindow()

    @staticmethod
    def Inventar(old_window):
        if old_window is not None:
            old_window.close()
        SellWindow()

    @staticmethod
    def Sell_item(old_window):
        if old_window is not None:
            old_window.close()
        GebrauchtwarenWindow()

    """@staticmethod
    def Sell_item_Access(old_window):
        if old_window is not None:
            old_window.close()
        window = GebrauchtwarenWindowAccessories()
        window.show()"""
