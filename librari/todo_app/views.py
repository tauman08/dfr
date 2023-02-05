from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .serializers import ProjectModelSerializer, ToDoModelSerializer
from .models import Project, ToDo
from rest_framework.permissions import AllowAny, IsAuthenticated


class ProjectPaginator(LimitOffsetPagination):
    default_limit = 10


class ToDoPaginator(LimitOffsetPagination):
    default_limit = 5


class ProjectModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPaginator

    def get_queryset(self):

        name = self.request.query_params.get('name', '')
        if name:
            return Project.objects.filter(name__contains=name)
        return super().get_queryset()


class ToDoModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_fields = ['project', 'date_creation', 'date_update', 'is_active']
    pagination_class = ToDoPaginator
