from models.abstract import AbstractModel


class Candidatos(AbstractModel):
    numero_resolucio = None
    cedula = None
    nombre = None
    apellido = None

    def __init__(self, _id, num_resolucion, cedula, nombre, apellido):
        super().__init__(_id)
        self.numero_resolucio = num_resolucion
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido