from Personne import Personne


class Enfant(Personne):
    def __init__(self,nom, prenom, adn, doudou):
        super().__init__(nom, prenom, adn)
        self.__doudou = doudou

    def getDoudou(self):
        return self.__doudou
    
    def setDoudou(self, nouvelleValeur):
        self.__doudou = nouvelleValeur

    def afficher(self):
        print(f"{self.getPrenom()} ({self.calculerAge()} ans) et mon doudou est {self.__doudou}")

if __name__ == "__main__":
    elle = Enfant("dupont", "céline", 2000, "dora l'exploratrice")
    print(elle.Nom)
    elle.Nom ="durant"
    elle.Doudou = "Buzz l'éclair"

    elle.afficher()
