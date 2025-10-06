from enfant import *
moi = Enfant("MALONADO", "michel", 1966)


moi.__nom = "Maldo" # Double underscore
print(moi.__nom)

print(moi.tel) 
print(moi.get_prenom())
print(moi._Enfant__nom)