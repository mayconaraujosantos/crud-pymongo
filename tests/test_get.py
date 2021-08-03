from .test_school_case import CRUDTestCase


class CRUDGetTestCase(CRUDTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.clientest_crud.insert_many(self.clients)

    def test_get_one_document(self) -> None:
        query_params = {"course_code": "DBI"}
        result = self.clientest_crud.list_all(query_params)

        quant_result = len(result)
        self.assertEqual(quant_result, 0)

    def test_get_many_documents(self) -> None:
        query_params = {"code": "2347894"}
        result = self.clientest_crud.list_all(query_params)

        quant_result = len(result)
        self.assertEqual(quant_result, 1)

        query_params = {"course_code": "DBI", "code": "2347894"}
        result = self.clientest_crud.list_all(query_params)

        quant_result = len(result)
        self.assertEqual(quant_result, 0)
