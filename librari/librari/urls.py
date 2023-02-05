"""librari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet, BookModelViewSet, ArticleModelViewSet, BiographyModelViewSet
from authors.views import MyAPIView
from todo_app.views import ProjectModelViewSet, ToDoModelViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookModelViewSet)
router.register('article', ArticleModelViewSet)
router.register('authors', AuthorModelViewSet)
router.register('biography', BiographyModelViewSet)
# вместо path('myapi/', MyAPIView.as_view({'get': 'list'})),
# можно записать через роутер
router.register('my', MyAPIView, basename='my')

router.register('project', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token)
    # path('myapi/', MyAPIView.as_view({'get': 'list'})),
]
