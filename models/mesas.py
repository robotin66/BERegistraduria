from models.abstract import AbstractModel


class Mesas(AbstractModel):
    COLLECTION = "mesas"
    numero_mesa = None
    cedulas_inscritas = None

    def __init__(self, num_mesa, ced_inscritas, _id=None):
        super().__init__(_id)
        self.numero_mesa = num_mesa
        self.cedulas_inscritas = ced_inscritas
