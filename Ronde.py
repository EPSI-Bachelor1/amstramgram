from Enfant import Enfant
from abc import ABC, abstractmethod

class Ronde(ABC):
    def __init__(self):
        self.__liste = []
        self.__index = -1

    def vide(self):
        return self.__liste == []
    
    def ploufplouf (self):
        if self.vide():
            raise RondeVideError("la ronde est vide !")
        else:
            self.__index=0

    def ajouter (self, enfant):
        self.__liste.append(enfant)

    def combien(self):
        return len(self.__liste)

    def getEnfantCourant(self):
        return self.__liste[self.__index]
        
    def avancer(self):
        if self.vide():
            raise RondeVideError("la ronde est vide !")

        if self.combien() == 1:
            raise PasAssezDEnfantError("Il faut etre au moins 2 pour jouer à la ronde")

        #ici on est sur qu'il y a au moins 2 enfants dans la ronde
        self.__index = (self.__index+1) % self.combien()

        return self.__liste[self.__index]

    @abstractmethod
    def jouer(self):
        ... # ou pass

    def sortir(self):
        if self.vide():
            raise RondeVideError("impossible de sortir un enfant d'une ronde vide!")

        enfant = self.__liste[self.__index]

        del self.__liste[self.__index]

        # et __index ?
        if self.vide():
            self.__index=-1
        elif self.__index == self.combien():
            self.__index = 0

        return enfant
    
    def afficher(self):

        print(self.__index)
        for e in self.__liste:
            e.afficher()


# exceptions possibles
class RondeVideError(Exception):
    pass

class PasAssezDEnfantError(Exception):
    pass

import unittest
import random

class RondeTest(unittest.TestCase):
    # constructeur init 
    def test_quandOnCreeUneRondeElleEstVide(self):
        r = Ronde()
        self.assertEqual(r.vide() ,True)

    def test_quandOnCreeUneRondeElleContient0Enfant(self):
        r = Ronde()
        self.assertEqual(r.combien(), 0)

    def test_quandOnAjouteUnEnfantDansUneRondeVideCaFaitUnEnfant(self):
        r = Ronde()
        r.ajouter(Enfant("nom", "prenom", 2000, "doudou"))
        self.assertEqual(r.combien(), 1)

    def test_quandOnAjouteUnEnfantDansUneRondePasVideCaFaitUnEnfantDePlus(self):
        r = Ronde()

        n1=r.combien()

        r.ajouter(Enfant("nom", "prenom", 2000, "doudou"))

        self.assertEqual(r.combien(), n1+1)

if __name__ == "__main__":
    unittest.main()
