from rest_framework.test import APITestCase
from django.urls import reverse


class BookViewTest(APITestCase):
    def test_response_is_correct(self):
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response.status_code == 200

    def test_response_is_json(self):
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response['Content-Type'] == 'application/json'

    def test_response_contains_hello_key(self):
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert 'hello' in response.data

    def test_response_contains_correct_value(self):
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response.data['hello'] == 'django'

    def test_post_method_not_allowed(self):
        url = reverse('api:books')
        response = self.client.post(url, {}, format='json')
        assert response.status_code == 405