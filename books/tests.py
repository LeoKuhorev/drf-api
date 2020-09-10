from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import BookRecord, Genre


class BookTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='test_user', password='password')
        test_user.save()

        test_genre = Genre.objects.create(name='Test genre')

        test_book_record = BookRecord.objects.create(
            name='Test name',
            author='Test author',
            genre=test_genre,
            record_created_by=test_user
        )
        test_book_record.save()

    def test_book_record_content(self):
        book = BookRecord.objects.last()
        actual_name = str(book.name)
        actual_author = str(book.author)
        actual_genre = str(book.genre)
        actual_record_created_by = str(book.record_created_by)
        self.assertEqual(actual_name, 'Test name')
        self.assertEqual(actual_author, 'Test author')
        self.assertEqual(actual_genre, 'Test genre')
        self.assertEqual(actual_record_created_by, 'test_user')
