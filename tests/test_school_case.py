import os
from json import load as json_load
from unittest import TestCase

from src.database import Database as CRUDMongoClient
from src.school import School


class CRUDTestCase(TestCase):
    def setUp(self) -> None:
        self.mongo_client = CRUDMongoClient()
        self.mongo_client = self.mongo_client.client

        self.clientest_crud = School(self.mongo_client)
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "fixture/specialization.json")
        with open(file_path, "r") as data:
            self.clients = json_load(data)

    def tearDown(self) -> None:
        self.clientest_crud.clean_collection()
