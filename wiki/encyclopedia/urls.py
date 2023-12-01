from django.urls import path
from . import views

urlpatterns = [
    path("wiki/css", views.css_view, name="css_view"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("", views.index, name="index"),
]
