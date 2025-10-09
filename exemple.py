# fct
from  datetime import *

def jmaActuels():
    dateActuelle = date.today()
    return dateActuelle.day, dateActuelle.month, dateActuelle.year

def calculerAge(annee):
    anneeActuelle = 2025
    a = anneeActuelle - annee
    return a

# main

j,m,a = jmaActuels()
print(j,"/",m,"/",a)