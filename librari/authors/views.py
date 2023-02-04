from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Author, Book, Article, Biography
from .serializers import AuthorModelSerializer, BookModelSerializer, ArticleModelSerializer, BiographyModelSerializer
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated


class AuthorPaginator(LimitOffsetPagination):
    default_limit = 10


class AuthorModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    # ручками через переопределение родительского метода:
    # def get_queryset(self):
    #     # через заголовки
    #     # param = self.request.headers.get('Filter')
    #     # через параметры
    #     param = self.request.query_params.get('name','')
    #     if params:
    #         # через заголовки
    #         # return Author.objects.filter(first_name__contains=param)
    #         # через параметры
    #         return Author.objects.filter(first_name__contains=param[0])
    #     return super().get_queryset()
    # /////////////////////////////////////////////////////////////////
    # через django_filters:
    filterset_fields = ['first_name', 'last_name', 'birthday_year']
    pagination_class = AuthorPaginator


class BookModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


# class MyAPIView(APIView):

#     def get(self, request):
#         return Response({'data': 'GET SUCCESS'})

#     def post(self, request):
#         return Response({'data': 'POST SUCCESS'})

# class MyAPIView(CreateAPIView):
#     # создание объекта post
#     renderer_classes = [JSONRenderer]
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializer

# class MyAPIView(ListCreateAPIView):
#     # чтение данных объекта get
#     renderer_classes = [JSONRenderer]
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializer

# class MyAPIView(CreateAPIView, ListCreateAPIView):
#     # методы get и post

#     # указываем конкретный рендер который хотим использовать, иначе будет использован
#     # рендер по умолчанию
#     # renderer_classes = [JSONRenderer]

#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializer

class MyAPIView(ViewSet):

    # create - post,
    # retrieve - получение одного объекта
    # update - update,
    # destroy - delete,
    # list- get(получение всех объектов)
    # абревиатура - CRUD (create,retrieve,update, destroy)
    # принятые в django обозначения методов mixins.py
    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorModelSerializer(queryset, many=True)
        return Response(serializer.data)

    # реализуем свой произвольный метод. url создается автоматом - /my/babayka
    @action(detail=False, methods=['get'])
    def babayka(self, request):
        return Response({'data': 'RATATA'})
