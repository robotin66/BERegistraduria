from abc import ABCMeta


class AbstractModel(metaclass=ABCMeta):
    _id = None
    COLLECTION = ""


    def __init__(self, _id=None):
        self._id = _id
