from django.urls import path

from apps.users.views import SingUpView, LoginView, LogoutView

urlpatterns = [
    path('create/', SingUpView.as_view(), name='create-user'),
    path('login/', LoginView.as_view(), name='create-user'),
    path('logout/', LogoutView.as_view(), name='create-user'),
]