from controllers.abstract import *
from models.candidatos import *
from repositories.candidatos import *
from repositories.partidos import *


class ControladorCandidatos(AbstractController):

    def __init__(self):
        self.repo_candi = RepositorioCandidatos(Candidatos, CandidatoInexistente)
        self.repo_parti = RepositorioPartidos(Partidos, PartidoInexistente)

    def trae_todo(self):
        return self.repo_candi.trae_todo()

    def trae_elemento(self, _id):
        return self.repo_candi.trae_elemento(_id)

    def crea(self, body):
        partido_doc = body.get("partido", {})
        body["partido"] = self.repo_parti.trae_elemento(partido_doc.get("_id")).pasa_json()
        return self.repo_candi.guarda(Candidatos.factory(body))

    def actualiza(self, _id, body):
        partido_doc = body.get("partido", {})
        encontrada = self.repo_candi.trae_elemento(_id)
        encontrada.resolucion = body["resolucion"]
        encontrada.cedula = body["cedula"]
        encontrada.nombre = body["nombre"]
        encontrada.apellido = body["apellido"]
        encontrada.partido = self.repo_parti.trae_elemento(partido_doc.get("_id")).pasa_json()
        return self.repo_candi.guarda(encontrada)

    def borra(self, _id):
        encontrada = self.repo_candi.trae_elemento(_id)
        return self.repo_candi.borra(encontrada)

    def total(self):
        return self.repo_candi.total()

    def asigna_partido(self, candidato, partido):
        existe_candi = self.trae_elemento(candidato)
        existe_parti = self.trae_elemento(partido)
        existe_candi.partido = existe_parti
        return self.repo_candi.guarda(existe_candi)
