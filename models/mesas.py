from models.abstract import *


class Mesas(AbstractModel):
    COLLECTION = "mesas"
    numero_mesa = None
    cedulas_inscritas = None

    def __init__(self, num_mesa, ced_inscritas, _id=None):
        super().__init__(_id)
        self.numero_mesa = num_mesa
        self.cedulas_inscritas = ced_inscritas

    def prepara_guardar(self):
        return {
            "num_mesa": self.numero_mesa,
            "ced_inscritas": self.cedulas_inscritas,
        }

    @staticmethod
    def factory(doc):
        return Mesas(
            num_mesa=doc["num_mesa"],
            ced_inscritas=doc["ced_inscritas"],
            _id=str(doc["_id"]) if doc.get("_id") else None,
        )

    def pasa_json(self):
        return self.__dict__


class MesaInexistente(ElementoInexistente):
    pass
