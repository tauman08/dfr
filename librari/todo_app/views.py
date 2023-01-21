from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .serializers import ProjectModelSerializer, ToDoModelSerializer
from .models import Project, ToDo


class ProjectPaginator(LimitOffsetPagination):
    default_limit = 10


class ToDoPaginator(LimitOffsetPagination):
    default_limit = 5


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPaginator

    def get_queryset(self):

        name = self.request.query_params.get('name', '')
        if name:
            return Project.objects.filter(name__contains=name)
        return super().get_queryset()


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_fields = ['project', 'date_creation', 'date_update', 'is_active']
    pagination_class = ToDoPaginator
