from controllers.abstract import *
from models.partidos import *
from repositories.partidos import *


class ControladorPartidos(AbstractController):

    def __init__(self):
        self.repositorio = RepositorioPartidos(model=Partidos, inexistente=PartidoInexistente)

    def trae_todo(self):
        return self.repositorio.trae_todo()

    def trae_elemento(self, _id):
        return self.repositorio.trae_elemento(_id)

    def crea(self, body):
        creada = Partidos(
            nombre=body["nombre"],
            lema=body["lema"],
        )
        return self.repositorio.guarda(creada)

    def actualiza(self, _id, body):
        encontrada = self.trae_elemento(_id)
        encontrada.lema = body["lema"]
        return self.repositorio.guarda(encontrada)

    def borra(self, _id):
        encontrada = self.trae_elemento(_id)
        return self.repositorio.borra(encontrada)

    def total(self):
        return self.repositorio.total()
