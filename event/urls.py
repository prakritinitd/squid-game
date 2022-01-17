from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("squid-game", views.game, name="game"),

    # API's for ROUND 1

    path("round1-attempts-left", views.attemptsLeftRound1),
    path("round1-help", views.replayRoundOne),
    path("round1_-_-_-_", views.SuccessRound1),
    path("profile", views.UserProfile),

    # API's for cheaters of round1

    path('blackbox',views.cheaterRound1),

    # API for gameover

    path('pandorabox',views.gameOver)
]
