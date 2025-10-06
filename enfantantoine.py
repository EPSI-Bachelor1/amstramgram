<<<<<<< HEAD:enfantantoine.py
class Enfant:
    # constructeur
    def __init__(self, nom, prenom, adn):
        self.__nom = nom
        self.__prenom = prenom
        self.__adn = adn
        self.tel = "07452809052"
    # Accesseurs
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom

    def get_adn(self):
        return self.__adn
    

    def set_nom(self, nouveau_nom):
        self.__nom = nouveau_nom

    def set_prenom(self, nouveau_prenom):
        self.__prenom = nouveau_prenom

    def set_adn(self, nouveau_adn):
        self.__adn = nouveau_adn
    
    # autres methodes
    def calculer_age(self):
        age = 2024 - self.__adn
        return age

    def __str__(self):
        return f"{self.__prenom} ({self.calculer_age()} ans)."
                

    
        
    
    
=======

class Enfant:
    # constructeur
    def __init__(self, nom, prenom, adn):
        self.__nom = nom
        self.__prenom = prenom
        self.__adn = adn
        self.tel="06..."
        
        self.tel = "06.11.78.64.90"

        1
    # Accesseurs
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom

    def get_adn(self):
        return self.__adn
    

    def set_nom(self, nouveau_nom):
        self.__nom = nouveau_nom

    def set_prenom(self, nouveau_prenom):
        self.__prenom = nouveau_prenom

    def set_adn(self, nouveau_adn):
        self.__adn = nouveau_adn

    
    # autres methodes
    def calculer_age(self):
        age = 2024 - self.__adn
        return age

    def __str__(self):
        return f"{self.__prenom} ({self.calculer_age()} ans)."
                

    
        
    
    
>>>>>>> 6e76b1a2bcea36a0f5838318c835582a0ffe23b1:enfant.py
