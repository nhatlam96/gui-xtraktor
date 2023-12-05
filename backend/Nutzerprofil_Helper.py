import csv
import os

ACCOUNTS_FILE_PATH = os.path.join("..", "resources", "csv", "Accounts.csv")


def display_userprofile(self, user):
    with open(ACCOUNTS_FILE_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == user:
                self.loginStatusLabel.setText(row['role'])
                self.usernameLabel.setText(row['username'])
                self.passwordLineEdit.setText(row['password'])
                self.budgetLineEdit.setText(row['budget'])


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
