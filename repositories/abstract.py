from abc import ABC
from typing import Type

from bson import ObjectId, DBRef
from pymongo import MongoClient

from models.abstract import *

MONGO_URI = "mongodb+srv://robotin66:regis123@clusterg40e4.p6aztfp.mongodb.net/?retryWrites=true&w=majority"
DB = "BERegistraduria"


class RepositorioAbstracto(ABC):
    def __init__(self, model: Type[AbstractModel], inexistente: Type[ElementoInexistente]):
        self._cliente = MongoClient(MONGO_URI)
        self.BD = self._cliente.get_database(DB)
        self.COLL = self.BD.get_collection(model.COLLECTION)
        self.model = model
        self.inexistente = inexistente

    def guarda(self, modelo: AbstractModel):
        if modelo.es_nuevo():
            insertada = self.COLL.insert_one(modelo.prepara_guardar())
            modelo._id = str(insertada.inserted_id)
        else:
            self.COLL.update_one({
                "_id": ObjectId(modelo._id)
            },
                {
                    "$set": modelo.prepara_guardar()
                }
            )
        return modelo

    def borra(self, modelo: AbstractModel):
        doc = self.COLL.delete_one({"_id": ObjectId(modelo._id)})
        return doc.deleted_count

    def trae_todo(self):
        lista = []
        for doc in self.COLL.find():
            self.llenar_db_ref(doc)
            lista.append(AbstractModel.factory(doc))
        return lista

    def trae_elemento(self, elemento):
        doc = self.COLL.find_one({"_id": ObjectId(elemento)})
        if not doc:
            raise self.inexistente
        self.llenar_db_ref(doc)
        return self.model.factory(doc)

    def total(self):
        return self.COLL.count_documents({})

    def llenar_db_ref(self, data):
        for llave, valor in data.items():
            if valor and isinstance(valor, DBRef):
                collection = self.BD.get_collection(valor.collection)
                relacionada = collection.find_one({
                    "_id": valor.id
                })
                data[llave] = relacionada
