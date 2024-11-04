from armas import *
from golpes import *
from fps import *

s1 = Soco()
c2 = Chute()
a1 = Arma(5)
f1 = Faca()
r1 = Revolver()
lc1 = Lanca_Chamas()
si1 = Soco_Ingles()
j1 = Jogador("Pedro", 150)
j2 = Jogador("Rhuan", 150)

j1.add_armas(r1)
j1.add_armas(lc1)
j2.add_armas(r1)

print(j1)
print(j2)

j1.atirar(j1.armas[1], j2)
j2.atirar(j1.armas[0], j1)

print(j1)
print(j2)
