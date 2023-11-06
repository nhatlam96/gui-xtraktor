import csv

# Define the user data
user_data = [
    #{"Nutzer": "Klaus", "Passwort": "", "Budget": "3000000"},
    {"Nutzer": "Oskar", "Passwort": "", "Budget": "270000"},
    {"Nutzer": "Benni", "Passwort": "", "Budget": "250000"},
    {"Nutzer": "Daniela", "Passwort": "", "Budget": "200000"},
    {"Nutzer": "Horst", "Passwort": "", "Budget": "550000"},
    {"Nutzer": "Sieglinde", "Passwort": "", "Budget": "800000"},
]

# Specify the CSV file name
csv_file = "Nutzer.csv"

# Write user data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Nutzer", "Passwort", "Budget"])
    writer.writeheader()  # Write the header row

    for user in user_data:
        writer.writerow(user)

print(f"User data has been written to {csv_file}")
