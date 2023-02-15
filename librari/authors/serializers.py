from rest_framework.serializers import HyperlinkedModelSerializer, StringRelatedField, ModelSerializer
from .models import Author, Book, Article, Biography


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # fields = ['first_name', 'last_name']
        # exclude = ['id']


class AuthorModelSerializer_2(ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name']


class BiographyModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class ArticleModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class BookModelSerializer(HyperlinkedModelSerializer):
    authors = StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ['name', 'authors']
