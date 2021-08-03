from os import getenv

import pymongo


class Database:
    def __init__(self) -> None:
        self.HOST = "localhost"
        self.PORT = 27017
        self.client = pymongo.MongoClient(self.HOST, self.PORT)

    @property
    def connection(self) -> pymongo.MongoClient:
        return self.client

    # @property
    # def __get_db_vars(self) -> None:
    #     self.HOST = getenv("MONGO_HOST")
    #     self.PORT = getenv("MONGODB_PORT")

    #     if not self.HOST:
    #         self.HOST = "localhost"
    #     if self.PORT:
    #         self.PORT = int(self.PORT)
    #     else:
    #         self.PORT = 27017
