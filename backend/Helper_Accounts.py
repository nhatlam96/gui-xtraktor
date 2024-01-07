import csv
import os
import Helper3

from PyQt5.QtWidgets import QLineEdit

CSV_PATH = os.path.join("..", "resources", "csv")

ACCOUNTS_FILE_PATH = os.path.join("..", "resources", "csv", "Accounts.csv")
BIDDERS_FILE_PATH = os.path.join("..", "resources", "csv", "Bidders.csv")
INVENTAR_FILE_PATH = os.path.join("..", "resources", "csv", "Inventar.csv")
T_INVENTORY_PATH = os.path.join(CSV_PATH, "mobile Arbeitsmaschinen Landwirtschaft.csv")
Z_INVENTORY_PATH = os.path.join(CSV_PATH, "Zubehör.csv")


class UserHandler:
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


def check_credentials(username, password):
    with open(ACCOUNTS_FILE_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # noinspection PyTypeChecker
            if row['username'] == username and row['password'] == password:
                return True
    return False


def username_exists(username):
    with open(ACCOUNTS_FILE_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # noinspection PyTypeChecker
            if row['username'] == username:
                return True
    return False


def get_user_data(username):
    with open(ACCOUNTS_FILE_PATH, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == username:
                return row
    return None


def update_user_data(username, password, budget, role):
    rows = []
    with open(ACCOUNTS_FILE_PATH, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == username:
                # Update the existing user's data
                row['password'] = password
                row['budget'] = budget
                row['role'] = role
            rows.append(row)

    # Write the updated data back to the CSV file
    with open(ACCOUNTS_FILE_PATH, mode='w', newline='') as csvfile:
        fieldnames = ['username', 'password', 'budget', 'role']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def add_user_to_csv(username, password, budget, role):
    # Check if the username already exists in the CSV file
    existing_data = get_user_data(username)

    if existing_data:
        # Update the existing user's data
        update_user_data(username, password, budget, role)
    else:
        # Add a new user to the CSV file
        with open(ACCOUNTS_FILE_PATH, mode='a', newline='') as csvfile:
            fieldnames = ['username', 'password', 'budget', 'role']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'username': username, 'password': password, 'budget': budget, 'role': role})


def validate_inputs(username, password, budget, role):
    if not (2 <= len(username) <= 16 and 2 <= len(password) <= 16):
        return "Username and password must be between 2 and 16 characters."

    try:
        float(budget)  # Check if budget is a valid integer
    except ValueError:
        return "Budget must be a valid integer."

    if role == "Please select profile...":
        return "Please select a profile."

    return "success"


def toggle_password_visibility(self):
    checkbox_value = self.showPasswordCheckBox.isChecked()
    if checkbox_value:
        self.passwordLineEdit.setEchoMode(QLineEdit.Normal)
    else:
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)


def update_userprofile(self, user):
    print("update_userprofile says hello!")
    print(user)
    print(self)
    with open(ACCOUNTS_FILE_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == user:
                row['password'] = self.passwordLineEdit.text()
                row['budget'] = self.budgetLineEdit.text()


def update_userBalance(user, amount):
    with open(ACCOUNTS_FILE_PATH, 'r', newline='') as file:
        data = list(csv.reader(file))

    for row in data:
        if user in row:
            row[2] = str(int(float(row[2]) + amount))
            with open(ACCOUNTS_FILE_PATH, 'w', newline='') as file:
                csv.writer(file).writerows(data)
                return True


# äquivalent zu user, backwards compatibility
def update_accountsBalance(account, amount):
    with open(ACCOUNTS_FILE_PATH, 'r', newline='') as file:
        data = list(csv.reader(file))

    for row in data:
        if account in row:
            row[2] = str(int(float(row[2]) + amount))
            with open(ACCOUNTS_FILE_PATH, 'w', newline='') as file:
                csv.writer(file).writerows(data)
                return True

def update_klausBalance(amount):
    with open(ACCOUNTS_FILE_PATH, 'r', newline='') as file:
        data = list(csv.reader(file))

    for row in data:
        if "Klaus" in row:
            row[2] = str(int(float(row[2]) + amount))
            with open(ACCOUNTS_FILE_PATH, 'w', newline='') as file:
                csv.writer(file).writerows(data)
                return True

def update_biddersBalance(bidder, amount):
    with open(BIDDERS_FILE_PATH, 'r', newline='') as file:
        data = list(csv.reader(file))

    for row in data:
        if bidder in row:
            row[3] = str(int(float(row[3]) - amount)) # müsste eigentlich row[1] sein wenn gebut gefixt wird
            with open(BIDDERS_FILE_PATH, 'w', newline='') as file:
                csv.writer(file).writerows(data)
                return True

def readInventar():  # Get
    user = UserHandler.get_current_user()

    with open(INVENTAR_FILE_PATH, 'r', newline='') as file:
        data = list(csv.reader(file))

    userData = []
    for row in data:
        if user[0] in row:
            userData.append(row)
    return userData


def writeInventar(modell_name, anzahl, t_z, timestamp):
    user = UserHandler.get_current_user()

    with open(INVENTAR_FILE_PATH, 'r', newline='') as file:
        data = list(csv.reader(file))

    # at least one item must be ordered
    if anzahl > 0:
        data.append([modell_name, anzahl, t_z, user[0], timestamp])

    # sort by user (index 3 in each row)
    sorted_inv_by_user = sorted(data, key=lambda data: data[3])
    with open(INVENTAR_FILE_PATH, 'w', newline='') as file:
        csv.writer(file).writerows(sorted_inv_by_user)
        return True

def sellGebrauchtFromInventar(modell, anzahl, t_z, account, timestamp):
    with open(INVENTAR_FILE_PATH, 'r', newline='') as file:
        data = list(csv.reader(file))

    for row in data:
        if modell in row and account in row and timestamp in row:
            print("found", row)
            row[1] = int(row[1]) - anzahl # bestand abziehen weil verkauft
            if row[1] <= 0: # falls nach verkauf leer wäre
                data.remove(row) # eintrag löschen
            break

    # sort by user (index 3 in each row)
    sorted_inv_by_user = sorted(data, key=lambda data: data[3])
    with open(INVENTAR_FILE_PATH, 'w', newline='') as file:
        csv.writer(file).writerows(sorted_inv_by_user)
        return True


# shopping list structure: [['Vario_1050', 2, 't'], ['9R_RT', 3, 't']]
def update_seller_inventories(items_bought):
    # Update inventory for type 't'
    with open(T_INVENTORY_PATH, 'r', newline='') as file:
        t_inventory = list(csv.reader(file))

    for item in items_bought:
        if item[2] == 't':
            for row in t_inventory[1:]:
                if row[1] == item[0]:  # Check if the product name matches
                    row[-1] = str(int(row[-1]) - int(item[1]))  # Update the Lager quantity

    with open(T_INVENTORY_PATH, 'w', newline='') as file:
        csv.writer(file).writerows(t_inventory)

    # Update inventory for type 'z'
    with open(Z_INVENTORY_PATH, 'r', newline='') as file:
        z_inventory = list(csv.reader(file))

    for item in items_bought:
        if item[2] == 'z':
            for row in z_inventory[1:]:
                if row[0] == item[0]:  # Check if the product name matches
                    row[2] = str(int(row[2]) - int(item[1]))  # Update the Bestand quantity

    with open(Z_INVENTORY_PATH, 'w', newline='') as file:
        csv.writer(file).writerows(z_inventory)


def get_bidders():
    with open(BIDDERS_FILE_PATH, mode='r') as csvfile:
        liste = []
        reader = csv.reader(csvfile)
        for row in reader:
            liste.append(row)

        return liste

def update_budgetsPerYear(years):
    # update Users
    with open(ACCOUNTS_FILE_PATH, 'r', newline='') as file:
        users_data = list(csv.reader(file))

    for row in users_data:
        newBudget = Helper3.increasedBudget(float(row[2]), years)
        row[2] = str(int(float(newBudget)))
        
    with open(ACCOUNTS_FILE_PATH, 'w', newline='') as file:
        csv.writer(file).writerows(users_data)
    print("increased users budgets") 
    
    # update Bidders
    with open(BIDDERS_FILE_PATH, 'r', newline='') as file:
        bidders_data = list(csv.reader(file))

    for row in bidders_data:
        newBudget = Helper3.increasedBudget(float(row[1]), years)
        row[1] = str(int(float(newBudget)))
        
    with open(BIDDERS_FILE_PATH, 'w', newline='') as file:
        csv.writer(file).writerows(bidders_data)
    print("increased bidders budgets")