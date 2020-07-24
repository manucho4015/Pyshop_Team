from django.conf import settings
import uuid
from django.db import models
from django.urls import reverse

CATEGORY_CHOICES = (
    ('FW', 'Fruits and Vegetables'),
    ('P', 'Pastry'),
    ('S', 'Snack'),
    ('RM', 'Ready Meal'),
    ('DP', 'Dairy Product'),
    ('SD', 'Soft Drink'),
    ('FG', 'Frozen Good')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)

    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'slug')

    def get_price(self):
        return self.price

    def get_absolute_url(self):
        return reverse("single_product", kwargs={'slug': self.slug})


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class FruitsAndVegetable(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    image_url = models.CharField(max_length=2083)


class Pastrie(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    image_url = models.CharField(max_length=2083)


class Snack(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    image_url = models.CharField(max_length=2083)


class ReadyMeal(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    image_url = models.CharField(max_length=2083)


class DairyProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    image_url = models.CharField(max_length=2083)


class SoftDrink(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    image_url = models.CharField(max_length=2083)


class Frozen(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    image_url = models.CharField(max_length=2083)


class Other(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    image_url = models.CharField(max_length=2083)
