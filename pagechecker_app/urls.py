from django.urls import path

from .views import page_checker

urlpatterns = [
    path("", page_checker, name="home"),
]
