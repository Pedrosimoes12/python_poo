from golpes import Soco
from abc import ABC, ABCMeta, abstractmethod

class Arma(ABC):
    destruicao: float

    def __init__(self, destruicao):
        self.destruicao = destruicao

    def agredir(self, j):
        j.energia -= 5

    def __str__(self):
        return f'Destruição: {self.destruicao:.2f}'

class Faca(Arma):
    lamina : int

    def __init__(self):
        super().__init__(15)
        self.lamina = 10

    def agredir(self, j):
        if self.lamina > 0:
            self.lamina -= 1
            j.energia -= self.destruicao
        else:
            super().agredir(j)

class Soco_Ingles(Faca, Soco):

    def agredir(self, j):
        super().agredir(j)
        self.golpear(j)

class Disparavel(metaclass = ABCMeta):

    @abstractmethod
    def disparar(self, j):
        pass

    @abstractmethod
    def recarregar(self):
        pass

class Revolver(Arma):
    cartuchos : int

    def __init__(self):
        super().__init__(20)
        self.cartuchos = 6

    def disparar(self, j):
        if self.cartuchos > 0:
            self.cartuchos -= 1
            j.energia -= self.destruicao

    def recarregar(self):
        self.cartuchos = 6

class Lanca_Chamas(Arma):
    gas : float

    def __init__(self):
        super().__init__(30)
        self.gas = 100

    def disparar(self, j):
        if self.gas > 0:
            self.gas -= 5.5
            j.energia -= self.destruicao
        else:
            super().agredir(j)

    def recarregar(self):
        self.gas = 100


#recommit