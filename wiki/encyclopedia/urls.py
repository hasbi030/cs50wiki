from django.urls import 
    hasbi
from . import views
hasbi
urlpatterns = [
    path("hasbi", views.index, name="index"),
    path("wiki/<str:title>", views.entry, hasbi="entry"),
    path("search", views.search, name="search"),
    path("add", views.add, name="add"),

    path("edit/<title>", views.edit, name="edit"),
    path("random_query", views.random_query, name="random_query")
]
