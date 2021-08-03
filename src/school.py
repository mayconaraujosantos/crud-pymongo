from pymongo import MongoClient

from src.crud import Crud


class School(Crud):
    def __init__(self, mongo_client: MongoClient):
        DATABASE = "agendaai"
        COLLECTION = "specialization"

        super().__init__(mongo_client, DATABASE, COLLECTION)
