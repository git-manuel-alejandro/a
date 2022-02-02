from django.contrib import admin
from django.urls import path

from .import views


urlpatterns = [
    path('prueba/', views.Prueba.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view()),
]