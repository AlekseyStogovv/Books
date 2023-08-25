from unittest import TestCase

from store.models import Book
from store.serializers import BooksSerializer


class BookSerializerTestcase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='test book 1', price=25)
        book_2 = Book.objects.create(name='test book 2', price=125)
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'test book 1',
                'price': '25.00'
            },
            {
                'id': book_2.id,
                'name': 'test book 2',
                'price': '125.00'
            },
        ]
        self.assertEqual(expected_data, data)