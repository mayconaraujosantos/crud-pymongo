from typing import List

import pymongo
from bson.objectid import ObjectId


class Crud:
    def __init__(
        self,
        mongo_client: pymongo.MongoClient,
        database_name: str,
        collection_name: str,
    ) -> None:
        self.mongo = mongo_client
        self.database_name = database_name
        self.db = self.mongo[database_name]

        self.collection_name = collection_name
        self.collection = self.db[collection_name]

    def insert(self, document: dict) -> ObjectId:
        inserted_document = self.collection.insert_one(document)
        inserted_id = inserted_document.inserted_id
        return inserted_id

    def insert_many(self, documents: List[dict]) -> List[ObjectId]:
        inserted_documents = self.collection.insert_many(documents)
        inserted_ids = inserted_documents.inserted_ids
        return inserted_ids

    def list_all(self, query_params: dict) -> list:
        query = self.collection.find(query_params)
        query_list = list(query)
        return query_list

    def update(self, query_parameters: dict, update_values: dict) -> int:
        update_dict = {"$set": update_values}

        updated_document = self.collection.update_one(query_parameters, update_dict, upsert=False)
        updated_count = updated_document.modified_count

        return updated_count

    def update_many(self, query_parameters: dict, update_values: dict) -> List[int]:
        update_dict = {"$set": update_values}
        updated_document = self.collection.update_one(query_parameters, update_dict, upsert=False)
        updated_count = updated_document.modified_count
        return updated_count

    def delete(self, query_parameters: dict) -> int:
        deleted_documents = self.collection.delete_many(query_parameters)
        deleted_count = deleted_documents.deleted_count
        return deleted_count

    def clean_collection(self) -> int:
        deleted_count = self.delete({})
        return deleted_count
