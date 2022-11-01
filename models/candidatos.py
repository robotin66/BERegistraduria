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
        return {
            "resolucion": self.resolucion,
            "cedula": self.cedula,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "partido": DBRef(id=ObjectId(self.partido._id), coll=Candidatos.COLLECTION)
        }

    def factory(self, data):
        partido = None
        if data.get("partido"):
            partido = Partidos.factory(data.get("partido"))
        return Candidatos(
            nombre=data["nombre"],
            apellido=data["apellido"],
            resolucion=data["resolucion"],
            cedula=data["cedula"],
            partido=partido,
            _id=str(data["_id"]) if data.get("_id") else None,
        )

    def pasa_json(self):
        return {
            "_id": self._id,
            "nombre": self.nombre,
            "apellido": self.cedula,
            "resolucion": self.resolucion,
            "cedula": self.cedula,
            "partido": self.partido.pasa_json()
        }


class CandidatoInexistente(ElementoInexistente):
    pass
