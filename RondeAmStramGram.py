from Enfant import Enfant
from Ronde import *

class RondeAmStramGram(Ronde):
    comptine = ["am", "stram", "gram", "pic", "et pic", "et coll", "et gram",
                         "bourre", "et bourre", "et ra", "tatam", "am", "stram", "gram",
                         "pic", "dam"]
    def __init__(self):
        super().__init__()

    def jouer(self):
        for i in range(0,len(RondeAmStramGram.comptine)):
            self.avancer()
        return self.getEnfantCourant()

if __name__ == "__main__":
    try:
        laRonde =RondeUnPetitCOchon()
        
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

        e =laRonde.jouer()
        e.afficher()
        laRonde.sortir()

        e = laRonde.jouer()
        e.afficher()
        laRonde.sortir()


    except RondeVideError as ex:
        print ("ya un gros blème :", ex)    
        
    except PasAssezDEnfantError  as ex:
        print ("ya un petit blème :", ex)

    except Exception  as ex:
        print ("ya un autre blème :", ex)
