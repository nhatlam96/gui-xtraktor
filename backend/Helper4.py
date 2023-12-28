import csv
import os

CSV_PATH = os.path.join("..", "resources", "csv")


class FilterHandler:
    Filter_dict = {
        "Hersteller": '',
        "Typ": '',
        "Baujahr": '',
        "Leistung": '',
        "Geschwindigkeit": '',
        "Preis": ['', '']
    }

    @staticmethod
    def get_Filter():
        return FilterHandler.Filter_dict

    @staticmethod
    def clear_Filter():
        FilterHandler.Filter_dict = {
            "Hersteller": '',
            "Typ": '',
            "Baujahr": '',
            "Leistung": '',
            "Geschwindigkeit": '',
            "Preis": ['', '']
        }

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


class load:

    @staticmethod
    def hersteller_dict():
        hersteller_dict = {}
        pfad = os.path.join(CSV_PATH, "mobile Arbeitsmaschinen Landwirtschaft.csv")

        with open(pfad, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                hersteller = row['Hersteller']
                model = row['Typ']
                if hersteller not in hersteller_dict:
                    hersteller_dict[hersteller] = [model]
                else:
                    hersteller_dict[hersteller].append(model)

        return hersteller_dict

    @staticmethod
    def get_all_model():
        model_list = []
        for models in load.hersteller_dict().values():
            model_list.extend(models)
        return model_list

    @staticmethod
    def get_model(hersteller):
        return load.hersteller_dict().get(hersteller, [])
