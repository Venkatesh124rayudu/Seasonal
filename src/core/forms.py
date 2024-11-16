# core/forms.py

from django import forms
from .models import SeasonalFlavor
from django import forms
from .models import CustomerSuggestion

# class CustomerSuggestionForm(forms.ModelForm):
#     class Meta:
#         model = CustomerSuggestion
#         fields = ['customer_name', 'flavor_suggestion', 'allergy_concerns']
#         labels = {
#             'customer_name': 'Name',
#             'flavor_suggestion': 'Suggestion Description',
#             'allergy_concerns': 'Allergy Concerns',
#         }
from django import forms
from .models import CustomerSuggestion
from django import forms
from .models import SeasonalFlavor

class SeasonalFlavorForm(forms.ModelForm):
    class Meta:
        model = SeasonalFlavor
        fields = ['name', 'description', 'season', 'is_active'] 

class CustomerSuggestionForm(forms.ModelForm):
    class Meta:
        model = CustomerSuggestion
        fields = ['customer_name', 'flavor_suggestion', 'allergy_concerns']
        labels = {
            'customer_name': 'Name',
            'flavor_suggestion': 'Suggestion Description',
            'allergy_concerns': 'Allergy Concerns',
        }
