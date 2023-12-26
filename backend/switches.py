from Nutzerprofil import UserprofileWindow
from Produktansicht import ProductWindow
from Register import Register
from Startseite import Startseite
from accessoriesWindow import accessoriesWindow
from Login import Login
from Warenkorb import WarenkorbWindow
from Sell import SellWindow
from Gebrauchtwaren import GebrauchtwarenWindow
from GebrauchtwarenAccessories import GebrauchtwarenWindowAccessories

class switch_to:

    @staticmethod
    def register(old_window):
        if old_window is not None:
            old_window.close()
        window = Register()
        window.show()

    @staticmethod
    def product(old_window):
        if old_window is not None:
            old_window.close()
        window = ProductWindow()
        window.show()

    @staticmethod
    def startseite(old_window):
        if old_window is not None:
            old_window.close()
        window = Startseite()
        window.show()

    @staticmethod
    def login(old_window):
        if old_window is not None:
            old_window.close()
        window = Login()
        window.show()

    @staticmethod
    def nutzer(old_window):
        if old_window is not None:
            old_window.close()
        window = UserprofileWindow()
        window.show()

    @staticmethod
    def accessories(old_window):
        if old_window is not None:
            old_window.close()
        window = accessoriesWindow()
        window.show()

    @staticmethod
    def shopping_cart(old_window):
        if old_window is not None:
            old_window.close()
        window = WarenkorbWindow()
        window.show()


    @staticmethod
    def Inventar(old_window):
        if old_window is not None:
            old_window.close()
        window = SellWindow()
        window.show()

    @staticmethod
    def Sell_item(old_window):
        if old_window is not None:
            old_window.close()
        window = GebrauchtwarenWindow()
        window.show()

    @staticmethod
    def Sell_item_Access(old_window):
        if old_window is not None:
            old_window.close()
        window = GebrauchtwarenWindowAccessories()
        window.show()
