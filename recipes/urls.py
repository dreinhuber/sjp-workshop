from django.urls import path

from .views import RecipeListView, RecipeDetailView, RecipeCreateView, change_recipe

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipes_list'),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('create/', RecipeCreateView.as_view(), name='create_recipe'),
    path('<int:pk>/edit', change_recipe, name='edit_recipe')
]