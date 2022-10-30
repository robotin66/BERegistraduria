from controllers.abstract import AbstractController
from models.mesas import Mesas


class ControladorMesa(AbstractController):

    def __init__(self):
        self._lista = []

    def trae_todas(self):
        return self._lista

    def trae_elemento(self, num_mesa):
        indice = self._busca_elemento(num_mesa)
        return self._lista[indice]

    def crea(self, body):
        creada = Mesas(
            _id=body["_id"],
            num_mesa=body["num_mesa"],
            ced_inscritas=body["ced_inscritas"],
        )
        self._lista.append(creada)
        return creada

    def actualiza(self, num_mesa, body):
        indice = self._busca_elemento(num_mesa)
        encontrada = self._lista[indice]
        encontrada._id = body["_id"]
        encontrada.numero_mesa = body["num_mesa"]
        encontrada.cedulas_inscritas = body["ced_inscritas"]
        return encontrada

    def borra(self, num_mesa):
        indice = self._busca_elemento(num_mesa)
        self._lista.pop(indice)

    def total(self):
        return len(self._lista)

    def _busca_elemento(self, elemento):
        for indice, encontrada in enumerate(self._lista):
            if encontrada.numero_mesa == elemento:
                return indice
        raise MesaInexistente

class MesaInexistente(Exception):
    pass
