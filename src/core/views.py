from django.shortcuts import render, redirect  # Ensure 'redirect' is imported
from .models import SeasonalFlavor, Ingredient, CustomerSuggestion
from .forms import SeasonalFlavorForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .forms import CustomerSuggestionForm


from .forms import SeasonalFlavorForm



def add_customer_suggestion(request):
    if request.method == 'POST':
        form = CustomerSuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save()
            return render(request, 'core/success.html', {'suggestion': suggestion})
    else:
        form = CustomerSuggestionForm()
    return render(request, 'core/add_customer_suggestion.html', {'form': form})


def suggestion_success(request):
    return render(request, 'core/success.html')

def update_ingredient_quantity(request):
    if request.method == 'POST':
        ingredient_id = request.POST.get('ingredient_id')
        quantity = request.POST.get('quantity')

        try:
        
            quantity = int(quantity)
            if quantity < 1 or quantity > 100:
                return HttpResponse("Quantity must be between 1 and 100", status=400)

            ingredient = get_object_or_404(Ingredient, id=ingredient_id)
            ingredient.quantity = quantity
            ingredient.save()
            return redirect('ingredient_inventory')  # Redirect to the inventory page
        except ValueError:
            return HttpResponse("Invalid quantity", status=400)

    return HttpResponse("Invalid request", status=400)


def seasonal_flavors(request):
    flavors = SeasonalFlavor.objects.all()
    return render(request, 'core/seasonal_flavors.html', {'flavors': flavors})

def add_seasonal_flavor(request):
    if request.method == 'POST':
        form = SeasonalFlavorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seasonal_flavors')  
    else:
        form = SeasonalFlavorForm()
    return render(request, 'core/add_seasonal_flavor.html', {'form': form})

def ingredient_inventory(request):
    flavor_id = request.GET.get('flavor_id')  # Get flavor_id from the query parameters
    if flavor_id:
        # Add logic if needed, e.g., filter ingredients related to this flavor
        selected_flavor = SeasonalFlavor.objects.get(id=flavor_id)
        ingredients = Ingredient.objects.all()  # You can filter by flavor if there’s a relationship
        context = {
            'ingredients': ingredients,
            'selected_flavor': selected_flavor,
        }
    else:
        ingredients = Ingredient.objects.all()
        context = {'ingredients': ingredients}

    return render(request, 'core/ingredient_inventory.html', context)


def customer_suggestions(request):
    suggestions = CustomerSuggestion.objects.all()
    return render(request, 'core/customer_suggestions.html', {'suggestions': suggestions})

def customer_order_details(request):
    orders = CustomerSuggestion.objects.all()  # Or any logic to fetch the customer orders
    return render(request, 'core/customer_order_details.html', {'orders': orders})