from pymongo import MongoClient

from controllers.abstract import AbstractController
from models.mesas import Mesas

MONGO_URI = "mongodb+srv://robotin66:regis123@clusterg40e4.p6aztfp.mongodb.net/?retryWrites=true&w=majority"


class ControladorMesa(AbstractController):

    def __init__(self):
        self._cliente = MongoClient(MONGO_URI)
        self.BD = self._cliente.get_database("BERegistraduria")
        self.COLL = self.BD.get_collection(Mesas.COLLECTION)

    def trae_todo(self):
        _lista = []
        for elemento in self.COLL.find():
            elemento["_id"] = str(elemento["_id"])
            _lista.append(
                Mesas(
                    num_mesa=elemento["num_mesa"],
                    ced_inscritas=elemento["ced_inscritas"],
                    _id=elemento["_id"],
                )
            )
        return _lista

    def trae_elemento(self, num_mesa):
        elemento = self.COLL.find_one({"num_mesa": int(num_mesa)})
        if elemento is None:
            raise MesaInexistente
        return Mesas(
                    num_mesa=elemento["num_mesa"],
                    ced_inscritas=elemento["ced_inscritas"],
                    _id=str(elemento["_id"]),
                )

    def crea(self, body):
        creada = Mesas(
            num_mesa=body["num_mesa"],
            ced_inscritas=body["ced_inscritas"],
        )
        insertada = self.COLL.insert_one({
            "num_mesa": creada.numero_mesa,
            "ced_inscritas": creada.cedulas_inscritas,
        })
        creada._id = str(insertada.inserted_id)
        return creada

    def actualiza(self, num_mesa, body):
        encontrada = self.trae_elemento(num_mesa)
        encontrada.cedulas_inscritas = body["ced_inscritas"]
        self.COLL.update_one({
                "num_mesa": int(num_mesa)
            },
            {
                "$set": {
                    "ced_inscritas": encontrada.cedulas_inscritas,
                }
            }

        )
        return encontrada

    def borra(self, num_mesa):
        resultado = self.COLL.delete_one({"num_mesa": num_mesa})
        return resultado.deleted_count

    def total(self):
        return self.COLL.count_documents({})


class MesaInexistente(Exception):
    pass
