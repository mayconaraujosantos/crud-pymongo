from .test_school_case import CRUDTestCase


class CRUDUpdateTestCase(CRUDTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.clientest_crud.insert_many(self.clients)

    def test_update_one_document(self) -> None:
        update_where = {"course_code": "DBI"}
        update_to = {"code": "2347894"}

        updated_count = self.clientest_crud.update(update_where, update_to)

        self.assertEqual(updated_count, 0)

    def test_update_many_documents(self) -> None:
        update_where = {"course_code": "DBI"}
        update_to = {"code": "2347894"}

        update_count = self.clientest_crud.update_many(update_where, update_to)
        self.assertEqual(update_count, 0)
