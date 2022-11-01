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
    def factory(data):
        return Mesas(
            num_mesa=data["num_mesa"],
            ced_inscritas=data["ced_inscritas"],
            _id=str(data["_id"]) if data.get("_id") else None,
        )

    def pasa_json(self, data):
        return self.__dict__


class MesaInexistente(ElementoInexistente):
    pass
