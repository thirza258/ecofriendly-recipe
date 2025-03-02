from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.GetAllRecipe.as_view(), name='recipes'),
    path('recommendation/', views.RecommendationSystem.as_view(), name='recommendation'),
]