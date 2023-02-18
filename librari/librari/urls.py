from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet, BookModelViewSet, ArticleModelViewSet, BiographyModelViewSet
from authors.views import MyAPIView
from todo_app.views import ProjectModelViewSet, ToDoModelViewSet
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_shema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView

shema_view = get_shema_view(
    openapi.Info(
        title='Library',
        default_version='0.1',
        description="Doc for project",
        contact=openapi.Contact(email='babba@baba.com'),
        license=openapi.License(name="MIT License")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookModelViewSet)
router.register('article', ArticleModelViewSet)
router.register('authors', AuthorModelViewSet)
router.register('biography', BiographyModelViewSet)
# вместо path('myapi/', MyAPIView.as_view({'get': 'list'})),
# можно записать через роутер
# router.register('my', MyAPIView, basename='my')

router.register('project', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    # <Documantation>
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    # </Documantation>

    # 1. работает вместе с 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning'
    # в settings.py
    # re_path(r'^api/(?P<version>\d)/authors/$',
    #         MyAPIView.as_view({'get': 'list'})),
    # 2.работает с 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    # path('api/1/authors/', include('authors.urls', namespace='1')),
    # path('api/2/authors/', include('authors.urls', namespace='2')),
    # 3. работает с 'rest_framework.versioning.QueryParameterVersioning'
    # path('myapi/authors/', MyAPIView.as_view({'get': 'list'})),
    # 4. работает с 'rest_framework.versioning.AcceptHeaderVersioning'
    # path('myapi/authors/', MyAPIView.as_view({'get': 'list'})),

]
