from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wiki/css', views.css_view, name='css_view'),
    path('wiki/django', views.django_view, name='django_view'),
    path('wiki/git', views.git_view, name='git_view'),
    path('wiki/html', views.html_view, name='html_view'),
    path('wiki/python', views.python_view, name='python_view'),
    path('wiki/<str:title>', views.entry, name='entry'),
]
