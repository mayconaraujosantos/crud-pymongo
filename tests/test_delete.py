from .test_school_case import CRUDTestCase


class CRUDDeleteTestCase(CRUDTestCase):
    def setUp(self):
        super().setUp()
        self.clientest_crud.insert_many(self.clients)

    def test_delete_one_document(self) -> None:
        for client in self.clients:
            delete_count = self.clientest_crud.delete(client)
            self.assertEqual(delete_count, 1)

    def test_delete_many_documents(self) -> None:
        deleted_count = self.clientest_crud.delete({})
        self.assertEqual(deleted_count, 1)
