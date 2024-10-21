from abc import ABC

class Lutador(ABC):
    nome: str
    energia: float

    def __init__(self, nome):
        self.nome = nome
        self.energia = 100

    def __str__(self):
        return f'Nome: {self.nome} Energia: {self.energia:.2f} %'

    def soco(self, oponente):
        oponente.energia -= 5.50

class Boxeador(Lutador):
    def cruzado(self, oponente):
        oponente.energia -= 1.20

    def gancho(self, oponente):
        oponente.energia -= 20.80

class Muay_Thai(Boxeador):
    def chute_alto(self, oponente):
        oponente.energia -= 15.40

class Jujitsu(Lutador):
    def chave_braco(self, oponente):
        oponente.energia -= 100.00

class MMA(Muay_Thai, Jujitsu):
    def superman_punch(self, oponente):
        oponente.energia -= 53.20