from abc import ABC, abstractmethod
from typing import List

class Operacao(ABC):
    operador : float

    def __init__(self, n : float):
        self.operador = n

    @abstractmethod
    def calcular(self, n : float):
        pass

    @abstractmethod
    def calcularinverso(self, n : float):
        pass

class Adicao(Operacao):
    def calcular(self, n : float):
        return n + self.operador

    def calcularinverso(self, n : float):
        return n - self.operador

class Subtracao(Operacao):
    def calcular(self, n : float):
        return n - self.operador

    def calcularinverso(self, n : float):
        return n + self.operador

class Multiplicacao(Operacao):
    def calcular(self, n : float):
        return n * self.operador

    def calcularinverso(self, n : float):
        return n / self.operador

class Divisao(Operacao):
    def calcular(self, n : float):
        return n / self.operador

    def calcularinverso(self, n : float):
        return n * self.operador

class Calculadora:
    resultado : float
    operacoes : List[Operacao]

    def __init__(self):
        self.resultado = 0
        self.operacoes : List[Operacao] = []

    def add_operacao(self, o : Operacao):
        self.operacoes.append(o)

    def calcular_total(self):
        calculo = 0
        for o in self.operacoes:
            calculo = o.calcular(calculo)
        self.resultado = calculo

    def desfazer_ultima(self):
        o = self.operacoes.pop()
        self.resultado = o.calcularinverso(self.resultado)