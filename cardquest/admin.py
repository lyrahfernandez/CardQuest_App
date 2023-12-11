from django.contrib import admin
from .models import Collection, PokemonCard, Trainer

@admin.register(PokemonCard)
class PokemonCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity', 'hp', 'card_type', 'attack', 'description', 'weakness', 'card_number', 'release_date', 'evolution_stage', 'abilities', 'created_at', 'updated_at')

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'location', 'email', 'created_at', 'updated_at')
    
admin.site.register(Collection)