from lutadores import *

if __name__ == "__main__":
    l1 = Boxeador("Jake Paul")
    l2 = Boxeador("Mike Tyson")
    l3 = MMA("Charles do Bronxs")
    l4 = Muay_Thai("Felipe Lobo")

    print('--------------LUTA 1--------------')

    l1.gancho(l2)
    print(l1)
    print(l2)
    l2.cruzado(l1)
    print(l1)
    print(l2)

    print('--------------LUTA 2--------------')

    l3.gancho(l4)
    l3.superman_punch(l4)
    print(l3)
    print(l4)

    l4.soco(l3)
    l4.chute_alto(l3)
    print(l3)
    print(l4)

    l3.chave_braco(l4)
    print(l3)
    print(l4)
