import random
import csv
import os.path
# import dis # show byte code with dis.dis(<function>)

CSV_PATH = os.path.join("..", "resources", "csv")

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

def getSumme(geraeteArt, geraeteTyp, anzahl, account):
    
    traktorenFile = os.path.join(CSV_PATH, r"mobile Arbeitsmaschinen Landwirtschaft.csv")
    zubehoerFile = os.path.join(CSV_PATH, r"Zubehör.csv")
    accountsFile = os.path.join(CSV_PATH, r"Accounts.csv")
    
    def getGeraeteSumme():  
        if geraeteArt == "Traktor":
            with open(traktorenFile, newline='') as file:
                for row in csv.reader(file):
                    if geraeteTyp in row:
                        preis = int(row[4])
                        summe = anzahl * preis 
                        if anzahl <= int(row[6]): # auf Lager
                            return summe
                        else:
                            return False
                return False      
        elif geraeteArt == "Zubehör":
            with open(zubehoerFile, newline='') as file:
                for row in csv.reader(file):
                    if geraeteTyp in row:
                        preis = int(row[1])
                        summe = anzahl * preis
                        if anzahl <= int(row[2]): # Bestand
                            return summe
                        else:
                            return False
                return False
                    
    def accountCanAfford(summe):
        with open(accountsFile, newline='') as file:
            for row in csv.reader(file):
                if account in row:
                    if summe <= int(row[2]): # Budget
                        return "can afford"
                    else:
                        return "can not afford"
            return "account not found"
        
    result = getGeraeteSumme()
    summe = result if result else False
    canAff = accountCanAfford(summe) if summe else False
    return summe, canAff
    
# print(getSumme(geraeteArt = "Traktor", 
#                   geraeteTyp = "Profi_6000", 
#                   anzahl = 5,
#                   account= "Klaus"))
       
    # budget checken, ist genug da?
    # lagerbestand checken, genug da?
    # lagerbestand abziehen
    # return summe
        
        
    # with open('some.csv', 'w', newline='') as file:
        # writer = csv.writer(file)
        # writer.writerows() # insert here someiterable
    
    

