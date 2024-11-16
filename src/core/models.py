# # offerings/models.py

from django.db import models


    
class CustomerSuggestion(models.Model):
    customer_name = models.CharField(max_length=100)
    flavor_suggestion = models.TextField()
    allergy_concerns = models.TextField()

    def __str__(self):
        return f"Suggestion by {self.customer_name}"


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()  # Store quantity as an integer (grams, units, etc.)

    def __str__(self):
        return self.name


class SeasonalFlavor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    season = models.CharField(max_length=50, default="Winter")
    is_active = models.BooleanField(default=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='flavors')  # ManyToMany relation with Ingredient

    def __str__(self):
        return self.name
