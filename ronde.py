#from enfant import *

class Ronde:
    contine = ["AM", "STRAM", "GRAM", "PIC", "ET PIC", "ET COLL", "ET GRAM", "BOURRE", "ET BOURRE", "ET RA", "TA TAM", "AM", "STRAM", "GRAM"]

    # le constructeur
    def __init__(self):
        self.__position = 0 # la liste d'enfants est vide
        self.__lesEnfants = []

        
   # les accesseurs
    def get_position(self):
        return self.__position

    def get_enfants(self):
        return self.__lesEnfants

    # affichage (tostring)
    def __str__(self):
        return self.__lesEnfants

    
    # autres methodes
    def ajouter(self, unEnfant):
        self.__lesEnfants.append(unEnfant)

    def combien(self):
        return len(self.__lesEnfants)

    def avancer(self):
        self.__position = (self.__position + 1) % self.combien()

    def am_stram_gram(self):
        for i in range(len(Ronde.contine)-1):
            self.avancer()
            print(Ronde.contine[i])

    def sortir(self):
        return self.__lesEnfants.pop(self.__position)


    
