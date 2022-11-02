from models.abstract import *


class Partidos(AbstractModel):
    COLLECTION = "partidos"
    nombre = None
    lema = None

    def __init__(self, nombre, lema, _id=None):
        super().__init__(_id)
        self.nombre = nombre
        self.lema = lema

    def prepara_guardar(self):
        return {
            "nombre": self.nombre,
            "lema": self.lema,
        }

    @staticmethod
    def factory(data):
        return Partidos(
            nombre=data["nombre"],
            lema=data["lema"],
            _id=str(data["_id"]) if data.get("_id") else None,
        )

    def pasa_json(self):
        return self.__dict__


class PartidoInexistente(ElementoInexistente):
    pass
