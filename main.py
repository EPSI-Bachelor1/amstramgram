from  fonctions import *

jourNaissance = int(input("quel jour ?"))
moisNaissance = int(input("de quel mois (1=jan ... 12=déc) ?"))
anneeNaissance = int (input("en quelle année etes-vous né(e) ? "))

age = calculerAge(jourNaissance, anneeNaissance, moisNaissance)2


print("vous avez", age, "ans")
