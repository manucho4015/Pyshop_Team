from django.contrib import admin
from .models import Product, Offer, FruitsAndVegetable, Pastrie, Snack, \
    ReadyMeal, DairyProduct, SoftDrink, Frozen, Other


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class FruitsAndVegetablesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class PastriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class SnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class ReadyMealAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class DairyProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class SoftDrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class FrozenAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OtherAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(FruitsAndVegetable, FruitsAndVegetablesAdmin)
admin.site.register(Pastrie, PastriesAdmin)
admin.site.register(Snack, SnackAdmin)
admin.site.register(ReadyMeal, ReadyMealAdmin)
admin.site.register(DairyProduct, DairyProductAdmin)
admin.site.register(SoftDrink, SoftDrinkAdmin)
admin.site.register(Frozen, FrozenAdmin)
admin.site.register(Other, OtherAdmin)
