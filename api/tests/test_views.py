from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import Book


class BookViewTest(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Dune",
            author="Frank Herbert",
            isbn="9780441013593",
            published_date="1965-08-01",
            description="Let the spice flow"
        )
        self.url = reverse('api:books')

    def test_get_response_is_200(self):
        response = self.client.get(self.url, format='json')
        assert response.status_code == 200

    def test_response_is_json(self):
        response = self.client.get(self.url, format='json')
        assert response['Content-Type'] == 'application/json'

    def test_get_returns_list(self):
        response = self.client.get(self.url, format='json')
        assert isinstance(response.data, list)

    def test_get_returns_correct_fields(self):
        response = self.client.get(self.url, format='json')
        book = response.data[0]
        assert 'id' in book
        assert 'title' in book
        assert 'author' in book
        assert 'isbn' in book
        assert 'published_date' in book
        assert 'description' in book
        assert 'created_at' in book

    def test_get_returns_correct_values(self):
        response = self.client.get(self.url, format='json')
        book = response.data[0]
        assert book['title'] == 'Dune'
        assert book['author'] == 'Frank Herbert'
        assert book['isbn'] == '9780441013593'

    def test_post_creates_book(self):
        data = {
            'title': '1984',
            'author': 'George Orwell',
            'isbn': '9780451524935',
            'published_date': '1949-06-08',
            'description': 'Big Brother is watching.'
        }
        response = self.client.post(self.url, data, format='json')
        assert response.status_code == 201

    def test_post_invalid_data_returns_400(self):
        response = self.client.post(self.url, {}, format='json')
        assert response.status_code == 400