import os

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

import Helper
import Helper2
import Helper_Accounts



class FilterHandler:
    Filter_dict = {
        "Hersteller": '',
        "Typ": '',
        "Baujahr": ['', ''],
        "Leistung": ['', ''],
        "Geschwindigkeit": ['', ''],
        "Preis": ['', '']
    }

    @staticmethod
    def get_Filter():
        return FilterHandler.Filter_dict

    @staticmethod
    def set_Filter(her=None, typ=None, bau=None, lei=None, ges=None, pre_min=None, pre_max=None):
        # Überprüfe, ob der Wert geändert wurde, ansonsten bleibt er unverändert
        if her is not None:
            FilterHandler.Filter_dict["Hersteller"] = her
        if typ is not None:
            FilterHandler.Filter_dict["Typ"] = typ
        if bau is not None:
            FilterHandler.Filter_dict["Baujahr"] = bau
        if lei is not None:
            FilterHandler.Filter_dict["Leistung"] = lei
        if ges is not None:
            FilterHandler.Filter_dict["Geschwindigkeit"] = ges
        if pre_min is not None:
            FilterHandler.Filter_dict["Preis"][0] = pre_min
        if pre_max is not None:
            FilterHandler.Filter_dict["Preis"][1] = pre_max
