from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "stock", "image_url"]


class ProductSearchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name"]