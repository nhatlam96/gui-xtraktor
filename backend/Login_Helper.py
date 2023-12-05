import csv
import os.path

from PyQt5.QtWidgets import QLineEdit

ACCOUNTS_FILE_PATH = os.path.join("..", "resources", "csv", "Accounts.csv")


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


def validate_inputs(username, password, budget, role):
    if not (2 <= len(username) <= 16 and 2 <= len(password) <= 16):
        return "Username and password must be between 2 and 16 characters."

    try:
        int(budget)  # Check if budget is a valid integer
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
