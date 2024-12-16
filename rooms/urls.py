from django.urls import path, include

from . import views

urlpatterns = [
    path('Lobby/', views.LobbyView, name='Lobby'),
]
