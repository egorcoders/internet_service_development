from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="API Приложения Постов и Комментариев",
        default_version='1.2.0',
        description='''Результат лабораторных работ по предмету: \"Разработка интернет-сервисов.\"
                    \n Преподаватель: Файзрахманова К.Э.
                    \n Выполнил: Боев Е.C.
                    \n 
                    \n CRUD для таблицы БД комментариев
                    \n Метод GET к ручке /comments/ получает данные всех комментариев;
                    \n Метод POST к ручке /comments/ создает комментарий;
                    \n Метод GET к ручке /comments/{id}/ получает комментарий по id;
                    \n Метод PUT к ручке /comments/{id}/ заменяет все поля комментария;
                    \n Метод PATCH к ручке /comments/{id}/ изменяет часть полей комментария;
                    \n Метод DELETE к ручке /comments/{id}/ удаляет комментарий.
                    \n
                    \n CRUD для таблицы БД постов
                    \n Метод GET к ручке /posts/ получает данные всех постов;
                    \n Метод POST к ручке /posts/ создает пост;
                    \n Метод GET к ручке /posts/{id}/ получает пост по id;
                    \n Метод PUT к ручке /posts/{id}/ заменяет все поля поста;
                    \n Метод PATCH к ручке /posts/{id}/ изменяет часть полей поста;
                    \n Метод DELETE к ручке /posts/{id}/ удаляет пост.
                    '''
    ),
    public=True,
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
    path('admin/', admin.site.urls),
    path('api/v1/',
         include([
             path('post/', include(('post.api.urls', 'post'), namespace='posts')),
         ])
    ),
]
