from abc import ABC, abstractmethod


class AbstractController(ABC):

    @abstractmethod
    def trae_todo(self):
        pass

    @abstractmethod
    def trae_elemento(self, elemento):
        pass

    @abstractmethod
    def crea(self, body):
        pass

    @abstractmethod
    def actualiza(self, elemento, body):
        pass
    @abstractmethod
    def borra(self, elemento):
        pass

    @abstractmethod
    def total(self):
        pass
