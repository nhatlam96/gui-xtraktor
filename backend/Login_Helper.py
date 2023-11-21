import csv
import os.path

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

ACCOUNTS_FILE_PATH = os.path.join("..", "resources", "csv", "Accounts.csv")


def update_main_window_size(main_window, width, height):
    main_window.setFixedSize(width, height)


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
    with open(ACCOUNTS_FILE_PATH, mode='a', newline='') as csvfile:
        fieldnames = ['username', 'password', 'budget', 'role']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'username': username, 'password': password, 'budget': budget, 'role': role})


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
