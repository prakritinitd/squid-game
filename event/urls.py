from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("squid-game", views.game),
]
