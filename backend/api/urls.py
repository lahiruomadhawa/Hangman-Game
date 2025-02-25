from django.urls import path
from .views import new_game, get_state, guess_char

urlpatterns = [
    path("game/new/", new_game, name="new_game"),  # POST
    path("game/<int:id>/", get_state, name="get_state"),  # GET
    path("game/<int:id>/guess/", guess_char, name="guess_char"),  # POST
]
