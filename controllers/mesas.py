from controllers.abstract import *
from models.mesas import *
from repositories.mesas import *


class ControladorMesas(AbstractController):

    def __init__(self):
        self.repositorio = RepositorioMesas(model=Mesas, inexistente=MesaInexistente)

    def trae_todo(self):
        return self.repositorio.trae_todo()

    def trae_elemento(self, _id):
        return self.repositorio.trae_elemento(_id)

    def crea(self, body):
        creada = Mesas(
            num_mesa=body["num_mesa"],
            ced_inscritas=body["ced_inscritas"],
        )
        return self.repositorio.guarda(creada)

    def actualiza(self, _id, body):
        encontrada = self.trae_elemento(_id)
        encontrada.cedulas_inscritas = body["ced_inscritas"]
        return self.repositorio.guarda(encontrada)

    def borra(self, _id):
        encontrada = self.trae_elemento(_id)
        return self.repositorio.borra(encontrada)

    def total(self):
        return self.repositorio.total()
