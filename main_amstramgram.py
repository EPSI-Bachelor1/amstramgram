# La comptine de notre enfance. Plouf plouf ...
from jeu import *

n = int(input("cb d'enfants vont jouer ?"))
le_jeu = Jeu(n)
le_jeu.ploufplouf()
le_jeu.jouer()
print(le_jeu.get_gagnant())



