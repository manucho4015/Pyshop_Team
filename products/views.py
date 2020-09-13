from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProductForm, ProductSearchForm
from .models import Product, Snack, Pastrie, ReadyMeal, \
    FruitsAndVegetable, DairyProduct, SoftDrink, Frozen, Other


def search(request):
    try:
        k = request.GET.get('search')
    except:
        k = None
    if k:
        products = Product.objects.filter(name__icontains=k)
        context = {'search': k, 'products': products}
        template = "results.html"
    else:
        template = "index.html"
        context = {}
    return render(request, template, context)


def index(request):
    all_products = Product.objects.all()
    return redirect(reverse('index.html',
                            kwargs={'all_products': all_products}))


def fruits_and_vegetable(request):
    fruits_and_vegetables = FruitsAndVegetable.objects.all()
    return render(request, 'fruits_and_vegetables.html',
                  {'fruits_and_vegetables': fruits_and_vegetables})


def snack(request):
    snacks = Snack.objects.all()
    return render(request, 'snacks.html',
                  {'snacks': snacks})


def pastrie(request):
    pastries = Pastrie.objects.all()
    return render(request, 'pastries.html', {'pastries': pastries})


def ready_meal(request):
    ready_meals = ReadyMeal.objects.all()
    return render(request, 'ready_meal.html', {'ready_meals': ready_meals})


def dairy_product(request):
    dairy_products = DairyProduct.objects.all()
    return render(request, 'dairy_product.html', {'dairy_products': dairy_products})


def soft_drink(request):
    soft_drinks = SoftDrink.objects.all()
    return render(request, 'soft_drinks.html', {'soft_drinks': soft_drinks})


def frozen(request):
    frozen_goods = Frozen.objects.all()
    return render(request, 'frozen_goods.html', {'frozen_goods': frozen_goods})


def other(request):
    other_goods = Other.objects.all()
    return render(request, 'other_goods.html', {'other_goods': other_goods})
