from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import custom_random_page

urlpatterns = [
    path('', views.index, name='index'),
    path('wiki/css', views.css_view, name='css_view'),
    path('wiki/django', views.django_view, name='django_view'),
    path('wiki/git', views.git_view, name='git_view'),
    path('wiki/html', views.html_view, name='html_view'),
    path('wiki/python', views.python_view, name='python_view'),
    path('random/', custom_random_page, name='random_page'), # Placed before the generic entry pattern
    path('wiki/<str:title>', views.entry, name='entry'),
    path('wiki/django', views.django_view, name='django_view'),
    path('search/', views.search_form, name='search'),  # Update to search_form
    path('entry/<str:title>/', views.entry, name='entry'),
    path('new/', views.new_page, name='new_page'),  # Creating a new URL pattern for a new page
    path('edit/<str:entry_title>/', views.edit_entry, name='edit_entry'),
    path('save_edit', views.save_edit, name="save_edit"),
]

