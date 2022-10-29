from models.abstract import AbstractModel


class Partidos(AbstractModel):
    nombre = None
    lema = None

    def __init__(self, _id, nombre, lema):
        super().__init__(_id)
        self.nombre = nombre
        self.lema = lema
