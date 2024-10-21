from abc import ABC, ABCMeta, abstractmethod

class Atleta(ABC):
    nome : str
    idade : int
    peso : float

    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def aquecer(self):
        return "Aquecendo.. "

    def __str__(self):
        info = f'Nome: {self.nome}, peso: {self.peso}, idade: {self.idade}'
        return info

class Corredor(Atleta):
    def correr(self):
        return "Correndo.. "

class Nadador(Atleta):
    def nadar(self):
        return "Nadando.. "

class Ciclista(Atleta):
    def pedalar(self):
        return "Pedalando.. "

class Triatleta(Corredor, Nadador, Ciclista):
    def realizar_maratona(self):
        info = self.nadar()
        info += self.pedalar()
        info += self.correr()
        return info