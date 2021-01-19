from django.urls import path
from . import views

urlpatterns = [
    path("", views.redirect, name="root"),
    path("wiki/", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("newpage", views.newpage, name="newpage"),
    path("editpage/<str:title>", views.editpage, name="editpage"),
    path("randomEntry", views.randomEntry, name="randomEntry")
]