from armas import Arma, Disparavel
from golpes import Golpe
from typing import List

class Jogador():
    nome : str
    energia : float
    armas : List[Arma]

    def __init__(self, nome, energia):
        self.nome = nome
        self.energia = energia
        self.armas : List[Arma] = []

    def add_armas(self, a : Arma):
        self.armas.append(a)

    def atirar(self, d : Disparavel, j):
        d.disparar(j)

    def municiar(self, d : Disparavel):
        d.recarregar()

    def __str__(self):
        info = f'Nome: {self.nome}, Energia: {self.energia}'
        return info


