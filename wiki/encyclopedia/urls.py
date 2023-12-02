from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wiki/css', views.css_view, name='css_view'),  # Place this before the entry pattern
    path('wiki/<str:title>', views.entry, name='entry'),
    path("wiki/git", views.git_view, name="git_view"),
]
