# notes about animals

___
Данное приложение является сервисом для создания заметок о животных. В нем реализованны:

- [x] Регистрация
- [x] Авторизация
- [x] Создание, редактирование, удаление, получение определенной заметки и всех.
- [x] Интеграция со сторонним API для поиска и скачивания картинок.

___

## стек

+ python3.11 <img height="24" width="24" src="https://cdn.simpleicons.org/python/5066b3" />
+ Django 4.1 <img height="24" width="24" src="https://cdn.simpleicons.org/django/5066b3" />
+ Postgres 15.0 <img height="24" width="24" src="https://cdn.simpleicons.org/postgresql/5066b3" />
+ Docker <img height="24" width="24" src="https://cdn.simpleicons.org/docker/5066b3" />
+ poetry<img height="24" width="24" src="https://cdn.simpleicons.org/poetry/" />
+ DRF 3.14
+ Redis<img height="24" width="24" src="https://cdn.simpleicons.org/redis/" />
+ Docker-compose
+ Celery

___

## swagger

/api/schema/swagger/
___

## Установка:

1. Клонируйте репозиторий с github на локальный компьютер
2. Создайте виртуальное окружение и активируйте его
3. Создайте в корне проекта файл в .env и заполните переменными окружения на примере .env.example
4. Соберите и поднимите docker-контейнер командой `make docker-compose` для запуска postgres и redis
5. Установите зависимости командой `make install-tools`
6. Запустите миграции `make migrate`
7. Запустите проект `make start-project`
8. Запустите celery `make run-celery`
9. Для запуска тестов используйте команду `make run-test`

___

## Как пользоваться

Сперва необходимо создать учетную запись, затем авторизоваться. После чего можно будет приступить к поиску картинок,
для этого не обходимо отправить POST запрос на endpoint `/images/search-images/` в теле запроса передать название
животного и количество картинок которые нужно скачать, на пример:

```
{
    "count": "4",
    "search": "duck"
}
   ```
После этого асинхронно будут скачаны картинки и сохранены в БД. Потом можно создать заметку и прикрепить к ней 
картинку. Для 
кэширования GET запросов используется Redis. При удалении заметки пользователем она не удаляется из БД, а 
приобретает статус `is_active = False`. Ежедневно в полночь запускается фоновая задача `Celery`, которая удаляет из 
БД заметки со статусом  `is_active = False` и датой последнего изменения старше 30 дней.
___

## Endpoint:

+ /users/create/ (Регистрация нового пользователя)
+ /users/login (Вход по логину и паролю)
+ /users/logout (Выход из учетной записи)
+ /images/search-images/ (Найти и скачать нужное кол-во картинок)
+ /blogs/get-blog/<int:pk>/ (Получить заметку по id)
+ /blogs/list-blog/ (Получить все заметки)
+ /blogs/create-blog/ (Создать заметку (только аутентифицированный пользователь))
+ /blogs/update-blog/<int:pk>/ (Изменить заметку (только хозяин заметки))
+ /blogs/destroy-blog/<int:pk>/ (Удалить заметку (только хозяин заметки))
