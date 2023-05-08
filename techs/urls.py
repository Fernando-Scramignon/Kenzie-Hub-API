from . import views
from django.urls import path

urlpatterns = [
    path('techs/', views.TechView.as_view()),
    path('techs/<str:pk>/', views.TechDetailView.as_view())
]