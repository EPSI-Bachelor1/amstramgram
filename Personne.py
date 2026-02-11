from datetime import datetime

class Personne:
    def __init__(self, nom, prenom, adn):
        self.__nom = nom
        self.__prenom = prenom
        self.__adn = adn
#proprieté Nom
# on définit la version Get de la propriete Nom
    @property
    def Nom(self):
        return self.__nom

# on définit la version Set de la propriete Nom
    @Nom.setter
    def Nom(self,value):
        self.__nom = value.upper()

    # accesseurs

    def getPrenom(self):
        return self.__prenom

    def setPrenom(self,nouvelleValeur):
        self.__prenom = nouvelleValeur

    def getAdn(self):
        return self.__adn

    def setAdn(self,nouvelleValeur):
        if nouvelleValeur <= 2026:
            self.__adn = nouvelleValeur
        else:
            print("année incorrecte !!")

    def afficher(self):
        print("Bonjour je m'appelle", self.__prenom, self.Nom, " et je suis né en", self.__adn)

    def calculerAge(self):
        return datetime.now().year - self.getAdn()
    
import unittest
class PersonneTest(unittest.TestCase):
    def test_calculerAge_2000(self):
        # test de la méthode calculerAge
        # à partir d'une donnée de test
        # Triple A


        # Etape 1 : Arrange
        # on prépare les données de test et le résultat attendu
        anneeTarget = 2000   # donnée à tester
        personneTarget = Personne("MALDONADO", "michel", anneeTarget)

        ageExpected = 26    # age theorique ou attendu

        # Etape 2 : Act
        ageActual = personneTarget.calculerAge()    # age reel ou obtenu

        # etape 3 : Assert
        self.assertEqual(ageActual, ageExpected)

# MAIN
if __name__ == "__main__":
    unittest.main()


   

