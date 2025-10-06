from ronde import *
from enfant import *

class Jeu:
    # constructeur
    def __init__(self, nbEnfants, i):
        nbEnfants = nbEnfants+i
        self.__laRonde = Ronde()
        self.saisir(nbEnfants)
        
    def saisir(self, n):
        for i in range(n):
            print("enfant n°",i)
            last_name = input("Nom ? ")
            first_name = input("Prenom ?")
            adn = int(input("Adn ?"))
            un_enfant = Enfant(last_name,first_name,adn)
            self.__laRonde.ajouter(un_enfant)
    
    def ploufplouf(self):
        pass

    def jouer(self):
        #tant que le jeu n'est pas fini
        while not self.termine():
            # am-stram-gram...
            self.__laRonde.am_stram_gram()
            perdant = self.__laRonde.sortir()
            print(perdant, "a perdu ...")

    def termine(self):
        return self.__laRonde.combien()== 1 

    def get_gagnant(self):
        if self.__laRonde.combien() != 1:
            raise Exception("pas de gagnant ! Le jeu n'est pas terminé.")
        else:
            enfants = self.__laRonde.get_enfants()
            return enfants[0]





        


