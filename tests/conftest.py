from pytest_factoryboy import register

from tests.factories import UserFactory, BlogFactory, ImagesFactory, UserNotOwnerFactory

pytest_plugins = 'tests.fixtures'

register(UserFactory)
register(BlogFactory)
register(ImagesFactory)
register(UserNotOwnerFactory)
