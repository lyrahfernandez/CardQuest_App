# models.py
from django.db import models

class PokemonCard(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Collection(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    pokemon_card = models.ForeignKey(PokemonCard, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
