from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('category/<str:category>/', views.animal_category, name='animal_category'),
    path('search/', views.search_animals, name='search_animals'),
    path('team/<slug:mascot>/', views.mascot_profile, name='mascot_profile'),
    path('<int:animal_id>/', views.animal_detail, name='animal_detail'),

]
