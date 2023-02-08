from .models import Author, Book
from .views import AuthorModelViewSet, BookModelViewSet
import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from django.contrib.auth.models import User
from mixer.backend.django import mixer


class TestAuthorViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors')
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(
            '/api/authors', {
                'first_name': 'Александр',
                'last_name': 'Пушкин',
                'birthday_year': 1880
            })
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(
            '/api/authors', {
                'first_name': 'Александр',
                'last_name': 'Пушкин',
                'birthday_year': 1880
            })
        admin = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin')
        force_authenticate(request, admin)
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        author = Author.objects.create(first_name='Александр',
                                       last_name='Пушкин', birthday_year=1799)
        client = APIClient()
        response = client.get(f'/api/authors/{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        author = Author.objects.create(first_name='Александр',
                                       last_name='Пушкин', birthday_year=1799)
        client = APIClient()
        response = client.put(f'/api/authors/{author.id}/',
                              {'first_name': 'Грин',
                               'last_name': 'Лавкрафт',
                               'birthday_year': 1880})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        author = Author.objects.create(first_name='Александр',
                                       last_name='Пушкин', birthday_year=1799)
        client = APIClient()
        admin = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin')
        client.login(username='admin', password='admin')
        response = client.put(f'/api/authors/{author.id}/',
                              {'first_name': 'Грин',
                               'last_name': 'Лавкрафт',
                               'birthday_year': 1880})
        author = Author.objects.get(pk=author.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(author.first_name, 'Грин')
        self.assertEqual(author.last_name, 'Лавкрафт')
        client.logout()


class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)


class TestBookViewSet(APITestCase):
    def test_get_lists(self):
        responce = self.client.get('/api/books/')
        self.assertEqual(responce.status_code, status.HTTP_200_OK)

    def test_edit_book_admin(self):
        # тут все делаем руками для таблице many-to-many
        # author = Author.objects.create(first_name='Александр',
        #                                last_name='Пушкин', birthday_year=1799)
        # book = Book.objects.create(name='Руслан и Людмила')
        # book.authors.add(author)
        # теперь по модному с миксером, который создаст связные данные

        book = mixer.blend(Book,
                           authors__first_name='Александр', authors__last_name='Пушкин', authors__birthday_year=1799)

        admin = User.objects.create_superuser(
            'admin', 'admin@admin.com', 'admin')
        self.client.login(username='admin', password='admin')
        # было так
        # response = self.client.put(
        #     f'/api/books/{book.id}/', {'name': 'Пиковая дама', 'author': author.id})
        response = self.client.put(
            f'/api/books/{book.id}/', {'name': 'Пиковая дама', 'author': book.authors.first().id})

        book = Book.objects.get(pk=book.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(book.name, 'Пиковая дама')
        self.client.logout()
