import datetime

def calculerAge(jourNaissance, moisNaissance, anneeNaissance):
    dateActuelle = datetime.date.today()
    if moisNaissance > dateActuelle.month:
        # anniversaire passé
        age = dateActuelle.year - anneeNaissance

    elif moisNaissance < dateActuelle.month :
        # anniversaire non passé
        age = dateActuelle.year - anneeNaissance - 1
    else:
        # meme mois : il faut regarder le jour de naissance

        if jourNaissance < dateActuelle.day :
            # anniversaire passé
            age = dateActuelle.year-anneeNaissance
        elif jourNaissance > dateActuelle.day :
            # anniversaire pas passé
            age = dateActuelle.year-anneeNaissance -1
        else:
            age = dateActuelle.year-anneeNaissance

    return age

def test_calculerAge_02061966():
    # 1 Arrange : preparer les données de test
    jourNaissanceTest, moisNaissanceTest, anneeNaissanceTest = 2, 6, 1966
    resultatAttendu = 59        # expected

    # 2 Act : on execute la fonction à tester   actual
    resultatObtenu = calculerAge(jourNaissanceTest, moisNaissanceTest, anneeNaissanceTest)

    # 3 Assert : on compare résultat attendu et résultat obtenu
    if resultatObtenu == resultatAttendu:
        print("OK - test_calculerAge_02061966 !")
    else:
        print("ERREUR... - test_calculerAge_02061966 attendu :", resultatAttendu, " obtenu :", resultatObtenu)


# instruction de test
if __name__ == "__main__":
    test_calculerAge_02061966