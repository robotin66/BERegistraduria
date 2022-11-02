from controllers.abstract import AbstractController
from models.candidatos import Candidatos, CandidatoInexistente
from models.mesas import Mesas, MesaInexistente
from models.resultados import Resultados, ResultadoInexistente
from repositories.candidatos import RepositorioCandidatos
from repositories.mesas import RepositorioMesas
from repositories.resultados import RepositorioResultados


class ControladorResultados(AbstractController):

    def __init__(self):
        self.repo_resul = RepositorioResultados(Resultados, ResultadoInexistente)
        self.repo_candi = RepositorioCandidatos(Candidatos, CandidatoInexistente)
        self.repo_mesa = RepositorioMesas(Mesas, MesaInexistente)

    def trae_todo(self):
        return self.repo_resul.trae_todo()

    def trae_elemento(self, _id):
        return self.repo_resul.trae_elemento(_id)

    def crea(self, body):
        doc_mesa = body.get("mesa", {})
        doc_partido = body.get("partido", {})
        body["mesa"] = self.repo_mesa.trae_elemento(doc_mesa.get("_id")).pasa_json()
        body["candidato"] = self.repo_candi.trae_elemento(doc_partido.get("_id")).pasa_json()
        return self.repo_resul.guarda(Resultados.factory(body))

    def actualiza(self, _id, body):
        encontrada = self.trae_elemento(_id)
        encontrada.votos = body["votos"]
        encontrada.cedula = body["cedula"]
        encontrada.nombre = body["nombre"]
        encontrada.apellido = body["apellido"]
        return self.repo_candi.guarda(encontrada)

    def borra(self, _id):
        encontrada = self.repo_resul.trae_elemento(_id)
        return self.repo_candi.borra(encontrada)

    def total(self):
        return self.repo_resul.total()

    def asigna_partido(self, candidato, partido):
        existe_candi = self.trae_elemento(candidato)
        existe_parti = self.trae_elemento(partido)
        existe_candi.partido = existe_parti
        return self.repo_candi.guarda(existe_candi)