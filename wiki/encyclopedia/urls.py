from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.wiki, name="wiki"),
    path("add/", views.add, name="add"),
    path("random/", views.random, name="random")
]
