from models.abstract import AbstractModel


class Mesas(AbstractModel):
    numero_mesa = None
    cedulas_inscritas = None

    def __init__(self, _id, num_mesa, ced_inscritas):
        super().__init__(_id)
        self.numero_mesa = num_mesa
        self.cedulas_inscritas = ced_inscritas
