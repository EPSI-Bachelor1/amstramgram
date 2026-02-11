from Enfant import Enfant
from abc import ABC, abstractmethod

class Ronde(ABC):
    def __init__(self):
        self.__liste = []
        self.__index = -1

    def vide(self):
        return self.__liste == []
    
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
    '''
    laRonde = Ronde()



    laRonde.afficher()'''

    #unittest.main()

    try:
        laRonde =Ronde()
        
        laRonde.ajouter(Enfant("ASK", "Antoine", 2008, "Yoshi"))
        laRonde.ajouter(Enfant("BART", "Maëlys", 2008, "Maëlys"))
        laRonde.ajouter(Enfant("BOURT ", "Théo", 2008, "Teddy"))
        laRonde.ajouter(Enfant("CHESNEAU", "Antonin", 2008, "Mahé"))
        laRonde.ajouter(Enfant("EDELY", "Lola", 2008, "Nunu"))
        laRonde.ajouter(Enfant("JANOT", "Achyl", 2008, "Amby"))
        laRonde.ajouter(Enfant("LE FRANC", "Nathan", 2008, "Bob"))
        laRonde.ajouter(Enfant("PERNOT", "Mahé", 2008, "Antonin"))
        laRonde.ajouter(Enfant("PEROTIN", "Evan", 2008, "Billy Boum - Babouche"))
        laRonde.ajouter(Enfant("POPOV", "Yann", 2008, "Pica"))
        laRonde.ajouter(Enfant("VOLMERANGE", "Julien", 2008, "Openda"))

        e =laRonde.amstramgram()
        e.afficher()
        laRonde.sortir()

        e = laRonde.amstramgram()
        e.afficher()
        laRonde.sortir()


    except RondeVideError as ex:
        print ("ya un gros blème :", ex)    
        
    except PasAssezDEnfantError  as ex:
        print ("ya un petit blème :", ex)

    except Exception  as ex:
        print ("ya un autre blème :", ex)
