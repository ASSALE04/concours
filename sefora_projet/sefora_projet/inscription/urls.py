# inscription/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil, qui appelle la vue 'home'
    path('inscrire/', views.inscrire, name='inscrire'),  # Page d'inscription, qui appelle la vue 'inscrire'
]
