from abc import ABCMeta, abstractmethod


class AbstractModel(metaclass=ABCMeta):
    _id = None
    COLLECTION = ""

    def __init__(self, _id=None):
        self._id = _id

    def es_nuevo(self) -> bool:
        return not self._id

    @abstractmethod
    def prepara_guardar(self):
        raise NotImplemented

    @staticmethod
    def factory(doc):
        raise NotImplemented

    @abstractmethod
    def pasa_json(self):
        raise NotImplemented


class ElementoInexistente(Exception):
    pass
