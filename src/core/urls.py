# offerings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('seasonal-flavors/', views.seasonal_flavors, name='seasonal_flavors'),
    path('ingredient-inventory/', views.ingredient_inventory, name='ingredient_inventory'),
    path('customer-suggestions/', views.customer_suggestions, name='customer_suggestions'),
    path('add-seasonal-flavor/', views.add_seasonal_flavor, name='add_seasonal_flavor'),
    path('update-ingredient-quantity/', views.update_ingredient_quantity, name='update_ingredient_quantity'),
    path('add-customer-suggestion/', views.add_customer_suggestion, name='add_customer_suggestion'),
    path('suggestion-success/', views.suggestion_success, name='suggestion_success'),
    path('customer-order-details/', views.customer_order_details, name='customer_order_details'),

]
