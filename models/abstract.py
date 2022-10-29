from abc import ABCMeta


class AbstractModel(metaclass=ABCMeta):
    _id = None

    def __init__(self, _id):
        self._id = _id
