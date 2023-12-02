from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wiki/css", views.css_view, name="css_view"),
    path("wiki/git", views.git_view, name="git_view"),  
]
