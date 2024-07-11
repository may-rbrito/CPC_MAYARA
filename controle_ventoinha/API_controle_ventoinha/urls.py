from django.urls import path
from . import views

urlpatterns = [
    path('api/temperature/', views.temperature_api_view, name='temperature_api'),
]
