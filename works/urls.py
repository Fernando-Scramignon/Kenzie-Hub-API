from django.urls import path
from . import views


urlpatterns = [
    path('works/', views.WorkView.as_view())
]