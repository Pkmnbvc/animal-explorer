from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category>/', views.animal_category, name='animal_category'),
    path('search/', views.search_animals, name='search_animals'),
    path('<int:animal_id>/', views.animal_detail, name='animal_detail'),

]
