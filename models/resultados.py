from models.candidatos import *
from models.mesas import *


class Resultados(AbstractModel):
    COLLECTION = "resultados"
    votos = None
    candidato: Candidatos = None
    mesa: Mesas = None

    def __init__(self, votos, candidato, mesa, _id=None):
        super().__init__(_id)
        self.votos = votos
        self.mesa = mesa
        self.candidato = candidato

    def prepara_guardar(self):
        return {
            "votos": self.votos,
            "mesa": DBRef(id=ObjectId(self.mesa._id), coll=Mesas.COLLECTION),
            "candidato": DBRef(id=ObjectId(self.candidato._id), coll=Candidatos.COLLECTION)
        }

    def factory(self, data):
        assert data.get("mesa")
        assert data.get("candidato")
        mesa = Mesas.factory(data.get("mesa"))
        candidato = Candidatos.factory(data.get("candidato"))
        return Resultados(
            votos=data["votos"],
            candidato=candidato,
            mesa=mesa,
            _id=str(data["_id"]) if data.get("_id") else None,
        )

    def pasa_json(self, data):
        return {
            "_id": self._id,
            "votos": self.votos,
            "mesa": self.mesa.pasa_json(),
            "candidato": self.candidato.pasa_json()
        }


class ResultadoInexistente(ElementoInexistente):
    pass
