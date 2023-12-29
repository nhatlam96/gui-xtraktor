from Nutzerprofil import UserprofileWindow

from Produktansicht import ProductWindow

from Register import Register

from Startseite import Startseite

from accessoriesWindow import accessoriesWindow
from accessoriesWindowAnbieter import accessoriesWindowAnbieter

from Login import Login
from Warenkorb import WarenkorbWindow
from Sell import SellWindow
from Gebrauchtwaren import GebrauchtwarenWindow
from Gebrauchtwaren_Accessories import GebrauchtwarenWindowAccessories

class WindowHandler:
    open_windows = {}

    @staticmethod
    def check_window(window_instance):
        if window_instance not in WindowHandler.open_windows:
            print("ADD")
            WindowHandler.open_windows[window_instance] = True
            return True
        elif WindowHandler.open_windows[window_instance] is True:
            print("TRUE")
            return False
        else:
            WindowHandler.open_windows[window_instance] = True
            print("FALSE")
            return True

    @staticmethod
    def release_window(window_instance):
        print("RELEASE")
        WindowHandler.open_windows[window_instance] = False




class switch_to:

    @staticmethod
    def register(old_window):
        if old_window is not None:
            old_window.close()
        Register()

    @staticmethod
    def product(old_window):
        if WindowHandler.check_window(ProductWindow) == True:
            window = ProductWindow()
            window.show()

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
        if WindowHandler.check_window(UserprofileWindow) == True:
            window = UserprofileWindow()
            window.show()


    @staticmethod
    def accessories(old_window):
        if old_window is not None:
            old_window.close()
        accessoriesWindow()

    @staticmethod
    def accessories_Anbieter(old_window):
        if old_window is not None:
            old_window.close()
        accessoriesWindowAnbieter()

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

    @staticmethod
    def Sell_item_Access(old_window):
        if old_window is not None:
            old_window.close()
        window = GebrauchtwarenWindowAccessories()
        window.show()
