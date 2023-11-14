import csv
import itertools
import os.path

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

ACCOUNTS_FILE_PATH = os.path.join("..", "resources", "csv", "Accounts.csv")


def updateMainWindowSize(main_window, width, height):
    main_window.setFixedSize(width, height)


def checkCredentials(username, password):
    with open(ACCOUNTS_FILE_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in itertools.islice(reader, 1):  # Skip the header row
            if row['username'] == username and row['password'] == password:
                return True
    return False


def showToast(message, icon):
    toast = QMessageBox()
    toast.setIcon(icon)
    toast.setText(message)
    toast.setWindowTitle("Notification")
    toast.setStandardButtons(QMessageBox.Ok)

    timer = QTimer(toast)
    # https://youtrack.jetbrains.com/issue/PY-24183/PyQt5-cannot-find-refernece-connect-in-funciton
    # https://stackoverflow.com/questions/64505166/cannot-find-reference-connect-in-function
    # noinspection PyUnresolvedReferences
    timer.timeout.connect(toast.close)
    timer.start(1750)

    toast.exec_()


def usernameExists(username):
    with open(ACCOUNTS_FILE_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in itertools.islice(reader, 1):  # Skip the header row
            if row['username'] == username:
                return True
    return False


def addUserToCSV(username, password, budget, role):
    with open(ACCOUNTS_FILE_PATH, mode='a', newline='') as csvfile:
        fieldnames = ['username', 'password', 'budget', 'role']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'username': username, 'password': password, 'budget': budget, 'role': role})


def validateInputs(username, password, budget, role):
    if not (2 <= len(username) <= 16 and 2 <= len(password) <= 16):
        return "Username and password must be between 2 and 16 characters."

    try:
        int(budget)  # Check if budget is a valid integer
    except ValueError:
        return "Budget must be a valid integer."

    if role == "Please select profile...":
        return "Please select a profile."

    return "success"
