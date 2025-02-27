from django.urls import path
from . import views

urlpatterns = [
    path("", views.RecommenderView.as_view(), name="recommender"),
]