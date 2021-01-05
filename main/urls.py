from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>/', category_detail, name='category'),
    path('recipe-detail/<int:pk>/', recipe_detail, name='detail'),
    path('add_recipe/', add_recipe, name='add-recipe'),
    path('update_recipe/<int:pk>/', update_recipe, name='update-recipe')
]
