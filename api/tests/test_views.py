from rest_framework.test import APITestCase


class BookViewTest(APITestCase):
    def test_response_is_correct(self):
        response = self.client.get()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"hello": "django"})