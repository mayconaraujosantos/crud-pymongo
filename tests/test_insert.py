from bson.objectid import ObjectId

from tests.test_school_case import CRUDTestCase


class CRUDInsertTestCase(CRUDTestCase):
    def test_insert_one_document(self) -> None:
        for client in self.clients:
            _id = self.clientest_crud.insert(client)
            type_id = type(_id)

            self.assertEqual(type_id, ObjectId)

    def test_insert_many_documents(self) -> None: 
        ids = self.clientest_crud.insert_many(self.clients)
        type_ids = [type(id) for id in ids]

        for type_id in type_ids:
            self.assertEqual(type_id, ObjectId)
