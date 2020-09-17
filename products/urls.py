from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('fruits_and_vegetables', views.fruits_and_vegetable),
    path('snacks', views.snack),
    path('pastries', views.pastrie),
    path('ready_meals', views.ready_meal),
    path('dairy_products', views.dairy_product),
    path('soft_drinks', views.soft_drink),
    path('frozen_goods', views.frozen),
    path('other_goods', views.other),
]
