from bson import DBRef, ObjectId

from models.partidos import *


class Candidatos(AbstractModel):
    COLLECTION = "candidatos"
    resolucion = None
    cedula = None
    nombre = None
    apellido = None
    partido: Partidos = None

    def __init__(self, resolucion, cedula, nombre, apellido, _id=None, partido=None):
        super().__init__(_id)
        self.resolucion = resolucion
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.partido = partido

    def prepara_guardar(self):
        partido_ref = None
        if self.partido:
            partido_ref = DBRef(id=ObjectId(self.partido._id), collection=Partidos.COLLECTION)
        return {
            "resolucion": self.resolucion,
            "cedula": self.cedula,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "partido": partido_ref
        }

    @staticmethod
    def factory(data):
        assert data.get("partido")
        partido = Partidos.factory(data.get("partido"))
        return Candidatos(
            resolucion=data["resolucion"],
            cedula=data["cedula"],
            nombre=data["nombre"],
            apellido=data["apellido"],
            partido=partido,
            _id=str(data["_id"]) if data.get("_id") else None,
        )

    def pasa_json(self):
        partido = None
        if self.partido:
            partido = self.partido.pasa_json()
        return {
            "_id": self._id,
            "resolucion": self.resolucion,
            "cedula": self.cedula,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "partido": partido
        }


class CandidatoInexistente(ElementoInexistente):
    pass
