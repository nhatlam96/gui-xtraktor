import random
import csv

# Zufallszahl 1
def isInterested(threshold = 0.6):
    interest = random.uniform(0, 1)
    return False if interest < threshold else True

# Zufallszahl 2
def genKaufangebot(curGebPreis):
    mod = random.uniform(0.70, 1.1)
    Kaufangebot = round(curGebPreis * mod)
    return Kaufangebot
   
# Zufallszahl 3 
def increasedBudget(curBudget, years = 1):
    newBudget = curBudget
    for each in range(years):
        increase = random.randint(0, 50_001)
        newBudget += increase
    return newBudget

def calcSumme(modellnummer, geraeteTyp, anzahl, accountname):
    
    if geraeteTyp == "Trak":
        pass
        
    if geraeteTyp == "Zube":
        pass
        
    with open('some.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
        
    with open('some.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows() # insert here someiterable
    
    # budget cheken, ist genug da?
    # lagerbestand checken, genug da?
    # lagerbestand abziehen
    
    return # summe

