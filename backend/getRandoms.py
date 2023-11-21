import random

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