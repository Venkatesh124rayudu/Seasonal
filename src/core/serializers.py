from rest_framework import serializers
from .models import SeasonalFlavor, Ingredient, CustomerFeedback

class SeasonalFlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonalFlavor
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class CustomerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFeedback
        fields = '__all__'
