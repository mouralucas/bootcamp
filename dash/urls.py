from django.urls import re_path

from dash import views

urlpatterns = [
    re_path('', views.Dash.as_view(), name='dash'),
]
