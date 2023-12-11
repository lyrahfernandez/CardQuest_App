# urls.py
from django.urls import path
from .views import (
    PokemonCardListView,
    PokemonCardDetailView,
    PokemonCardCreateView,
    PokemonCardUpdateView,
    PokemonCardDeleteView,
)

urlpatterns = [
    path('pokemon_cards/', PokemonCardListView.as_view(), name='pokemon_card_list'),
    path('pokemon_cards/<int:pk>/', PokemonCardDetailView.as_view(), name='pokemon_card_detail'),
    path('pokemon_cards/new/', PokemonCardCreateView.as_view(), name='pokemon_card_create'),
    path('pokemon_cards/<int:pk>/edit/', PokemonCardUpdateView.as_view(), name='pokemon_card_edit'),
    path('pokemon_cards/<int:pk>/delete/', PokemonCardDeleteView.as_view(), name='pokemon_card_delete'),
]
