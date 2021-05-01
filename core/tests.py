from django.test import TestCase

from core.models import Book


class BookTests(TestCase):
    def test_book_is_created_successfully(self):
        book = Book(
            name='starter',
            slug='starter'
        )
        book.save()

