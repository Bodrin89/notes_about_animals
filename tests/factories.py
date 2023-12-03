import factory.django

from apps.blogs.models import Blog
from apps.images.models import Images
from apps.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')


class ImagesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Images

    user = factory.SubFactory(UserFactory)
    title = 'текст блога'
    url = factory.Faker('url')


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    user = factory.SubFactory(UserFactory)
    title = "Блог про собак"
    text = "ТексT про собак"
    image = factory.SubFactory(ImagesFactory)
    is_active = True


class UserNotOwnerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')
#
#
# class MessageFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Message
#
#     created = factory.Faker('date')
#     text = factory.Faker('text')
#     user = factory.SubFactory(UserFactory)
#
#
# #
# class MessageNotOwnerFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Message
#
#     created = factory.Faker('date')
#     text = factory.Faker('text')
#     user = factory.SubFactory(UserNotOwnerFactory)
#
#
# class BotFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Bot
#
#     chat_id = 0
#     user = factory.SubFactory(UserFactory)
