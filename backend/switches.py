from PyQt5.QtWidgets import QApplication

from Nutzerprofil import UserprofileWindow
from Produktansicht import ProductWindow
from Register import Register
from Startseite import Startseite
from accessoriesWindow import accessoriesWindow
from Login import Login
from Warenkorb import WarenkorbWindow
from Sell import SellWindow
from Gebrauchtwaren import GebrauchtwarenWindow
from Gebrauchtwaren_Accessories import GebrauchtwarenWindowAccessories


class WindowHandler:
    open_windows = {}
    windows_dict = {}

    @staticmethod
    def check_window(alias):

        # True status heißt, das Fenster ist geöffnet
        # True return heißt, fenster darf geöffnet werden

        if alias not in WindowHandler.open_windows:
            print("ADD")
            WindowHandler.open_windows[alias] = True
            return True
        elif WindowHandler.open_windows[alias] is True:
            print("TRUE")
            return False
        else:
            WindowHandler.open_windows[alias] = True
            print("FALSE")
            return True

    @staticmethod
    def release_window(alias):
        print("RELEASE")
        WindowHandler.open_windows[alias] = False

    @staticmethod
    def register_window(alias, instanz):
        # Diese Methode fügt das Fenster dem windows_dict hinzu
        WindowHandler.windows_dict[alias] = instanz

    @staticmethod
    def release_all_except(alias):
        print("RELEASE ALL EXCEPT")
        print(WindowHandler.windows_dict)
        for key in WindowHandler.windows_dict.keys():
            if key != alias:
                WindowHandler.windows_dict[key].close()
        WindowHandler.windows_dict = {alias: WindowHandler.windows_dict.get(alias)}
        WindowHandler.open_windows_dict = {}

    @staticmethod
    def release_all():
        print("RELEASE ALL")
        for key in WindowHandler.windows_dict.keys():
            WindowHandler.windows_dict[key].close()
        WindowHandler.open_windows_dict = {}


class switch_to:

    @staticmethod
    def register(old_window=None):
        if old_window is not None:
            old_window.close()
        Register()

    @staticmethod
    def product():
        if WindowHandler.check_window(ProductWindow) is True:
            window = ProductWindow()
            window.show()
            WindowHandler.register_window(ProductWindow, window)
        else:
            WindowHandler.release_window(ProductWindow)
            switch_to.product()

    @staticmethod
    def startseite(old_window=None):
        if WindowHandler.check_window(Startseite) is True:
            if old_window is not None:
                old_window.close()
            window = Startseite()
            window.show()
            WindowHandler.register_window(Startseite, window)
            WindowHandler.release_all_except(Startseite)

        else:
            if old_window is not None:
                old_window.close()
            WindowHandler.release_all_except(Startseite)

    @staticmethod
    def login(old_window=None):
        if old_window is not None:
            old_window.close()
        window = Login()
        window.show()
        WindowHandler.register_window(Login, window)
        WindowHandler.release_all_except(Login)

    @staticmethod
    def nutzer():
        if WindowHandler.check_window(UserprofileWindow) is True:
            window = UserprofileWindow()
            window.show()
            WindowHandler.register_window(UserprofileWindow, window)

    @staticmethod
    def accessories():
        if WindowHandler.check_window(accessoriesWindow) is True:
            window = accessoriesWindow()
            window.show()
            WindowHandler.register_window(accessoriesWindow, window)

    @staticmethod
    def shopping_cart():
        window = WarenkorbWindow()
        window.show()
        WindowHandler.register_window(WarenkorbWindow, window)
        WindowHandler.release_all_except(WarenkorbWindow)

    @staticmethod
    def Inventar(old_window):
        if old_window is not None:
            old_window.close()
        WindowHandler.release_all()
        window = SellWindow()
        window.show()
        WindowHandler.register_window(SellWindow, window)

    @staticmethod
    def Sell_item():
        if WindowHandler.check_window(GebrauchtwarenWindow) is True:
            window = GebrauchtwarenWindow()
            window.show()
            WindowHandler.register_window(GebrauchtwarenWindow, window)

    @staticmethod
    def Sell_item_Access():
        if WindowHandler.check_window(GebrauchtwarenWindowAccessories) is True:
            window = GebrauchtwarenWindowAccessories()
            window.show()
            WindowHandler.register_window(GebrauchtwarenWindow, window)
