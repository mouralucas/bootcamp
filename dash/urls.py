from django.urls import path

from dash import views

urlpatterns = [
    path('', views.ExercicioUm.as_view(), name='exercicio_um'),
]
