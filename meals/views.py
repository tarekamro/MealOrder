from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Meal
from .forms import AddMeal
from orders.models import OrderForm

# Create your views here.


def all_meals(request):
    cats = Category.objects.all()
    meals = Meal.objects.all()
    context = {
                'cats': cats,
                'meals': meals,
              }
    return render(request, 'meals/index.html', context)


def meal_details(request, id, slug):
    meal = get_object_or_404(Meal, id=id, slug=slug)
    form = OrderForm()
    context = {
                'meal': meal,
                'form': form,
              }
    return render(request, 'meals/details.html', context)


def add_meal(request):
    # form = AddMeal()

    if request.method == "POST":
        form = AddMeal(request.POST)
        if form.is_valid():
            form.save()
            # form.save(commit=False)
            return redirect('add_meal')

    else:
        form = AddMeal()

    return render(request, 'meals/add_meal.html', {'form': form})

