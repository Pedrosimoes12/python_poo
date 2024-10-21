from atletas import *

if __name__ == "__main__":
    bolt = Corredor("Usain Bolt", 38, 86.0)
    print(bolt)
    print(bolt.aquecer())
    print(bolt.correr())

    phelps = Nadador("Michael Phelps", 39, 88.0)
    print(phelps)
    print(phelps.aquecer())
    print(phelps.nadar())

    quintana = Ciclista("Nairo Quintana", 34, 59.0)
    print(quintana)
    print(quintana.aquecer())
    print(quintana.pedalar())

    keller = Triatleta("Fernanda Keller", 61, 56.0)
    print(keller)
    print(keller.aquecer())
    print(keller.realizar_maratona())

    print(Triatleta.__mro__)