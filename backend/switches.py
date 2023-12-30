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

    @staticmethod
    def check_window(window_instance):

        # True status heißt, das Fenster ist geöffnet
        # True return heißt, fenster darf geöffnet werden

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
    def product():
        if WindowHandler.check_window(ProductWindow) is True:
            window = ProductWindow()
            window.show()
        else:
            WindowHandler.release_window(ProductWindow)
            switch_to.product()

    @staticmethod
    def startseite(old_window):
        if WindowHandler.check_window(Startseite) is True:
            old_window.close()
            window = Startseite()
            window.show()
        else:
            old_window.close()



    @staticmethod
    def login(old_window):
        if old_window is not None:
            old_window.close()
        Login()

    @staticmethod
    def nutzer(old_window):
        if WindowHandler.check_window(UserprofileWindow) is True:
            window = UserprofileWindow()
            window.show()


    @staticmethod
    def accessories(old_window):
        if WindowHandler.check_window(accessoriesWindow) is True:
            window = accessoriesWindow()
            window.show()
        else:
            WindowHandler.release_window(accessoriesWindow)
            switch_to.accessories()

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
    def Sell_item():
        if WindowHandler.check_window(GebrauchtwarenWindow) is True:
            window = GebrauchtwarenWindow()
            window.show()
    @staticmethod
    def Sell_item_Access():
        if WindowHandler.check_window(GebrauchtwarenWindowAccessories) is True:
            window = GebrauchtwarenWindowAccessories()
            window.show()
