from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("login_view", views.login_view, name="login_view"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout")
]
