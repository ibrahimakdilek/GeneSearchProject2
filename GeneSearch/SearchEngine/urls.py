from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search-autocomplete/', views.search_autocomplete_view, name='search_autocomplete')
    
]
