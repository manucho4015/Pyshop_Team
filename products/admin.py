from django.contrib import admin

from .models import Product, Offer, FruitsAndVegetable, Pastrie, Snack, \
    ReadyMeal, DairyProduct, SoftDrink, Frozen, Other


class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    search_fields = ('name',)
    list_display = ('name', 'price', 'stock', 'category', 'updated')
    list_editable = ('price', 'stock')
    list_filter = ('price', 'category')
    readonly_fields = ('updated', 'timestamp')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Product


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class FruitsAndVegetablesAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    search_fields = ('name',)
    list_display = ('name', 'price', 'stock', 'updated')
    list_editable = ('price', 'stock')
    readonly_fields = ('updated', 'timestamp')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = FruitsAndVegetable


class PastriesAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    search_fields = ('name',)
    list_display = ('name', 'price', 'stock', 'updated')
    list_editable = ('price', 'stock')
    readonly_fields = ('updated', 'timestamp')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Pastrie


class SnackAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    search_fields = ('name',)
    list_display = ('name', 'price', 'stock', 'updated')
    list_editable = ('price', 'stock')
    readonly_fields = ('updated', 'timestamp')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Snack


class ReadyMealAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    search_fields = ('name',)
    list_display = ('name', 'price', 'stock', 'updated')
    list_editable = ('price', 'stock')
    readonly_fields = ('updated', 'timestamp')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = ReadyMeal


class DairyProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    search_fields = ('name',)
    list_display = ('name', 'price', 'stock', 'updated')
    list_editable = ('price', 'stock')
    readonly_fields = ('updated', 'timestamp')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = DairyProduct


class SoftDrinkAdmin(admin.ModelAdmin):
    ldate_hierarchy = 'updated'
    search_fields = ('name',)
    list_display = ('name', 'price', 'stock', 'updated')
    list_editable = ('price', 'stock')
    readonly_fields = ('updated', 'timestamp')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = SoftDrink


class FrozenAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    search_fields = ('name',)
    list_display = ('name', 'price', 'stock', 'updated')
    list_editable = ('price', 'stock')
    readonly_fields = ('updated', 'timestamp')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Frozen


class OtherAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated'
    search_fields = ('name', 'category')
    list_display = ('name', 'price', 'stock', 'updated')
    list_editable = ('price', 'stock')
    readonly_fields = ('updated', 'timestamp')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Other


admin.site.site_header = 'SOKO APP'
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
