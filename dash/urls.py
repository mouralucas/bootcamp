from django.urls import path

from dash import views

urlpatterns = [
    path('', views.Dash.as_view(), name='dash'),
]
