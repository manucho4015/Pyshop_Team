from django.conf import settings
import uuid
from django.db import models
from django.urls import reverse

CATEGORY_CHOICES = (
    ('FV', 'Fruits and Vegetables'),
    ('P', 'Pastry'),
    ('S', 'Snack'),
    ('RM', 'Ready Meal'),
    ('DP', 'Dairy Product'),
    ('SD', 'Soft Drink'),
    ('FG', 'Frozen Good'),
    ('OG', 'Other Good')
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


class FruitsAndVegetableManager(models.Manager):
    def get_queryset(self):
        return super(FruitsAndVegetableManager, self).get_queryset().filter(category='FV')


class FruitsAndVegetable(Product):
    objects = FruitsAndVegetableManager()

    class Meta:
        proxy = True


class PastrieManager(models.Manager):
    def get_queryset(self):
        return super(PastrieManager, self).get_queryset().filter(category='P')


class Pastrie(Product):
    objects = PastrieManager()

    class Meta:
        proxy = True


class SnackManager(models.Manager):
    def get_queryset(self):
        return super(SnackManager, self).get_queryset().filter(category='S')


class Snack(Product):
    objects = SnackManager()

    class Meta:
        proxy = True


class ReadyMealManager(models.Manager):
    def get_queryset(self):
        return super(ReadyMealManager, self).get_queryset().filter(category='RM')


class ReadyMeal(Product):
    objects = ReadyMealManager()

    class Meta:
        proxy = True


class DairyProductManager(models.Manager):
    def get_queryset(self):
        return super(DairyProductManager, self).get_queryset().filter(category='DP')


class DairyProduct(Product):
    objects = DairyProductManager()

    class Meta:
        proxy = True


class SoftDrinkManager(models.Manager):
    def get_queryset(self):
        return super(SoftDrinkManager, self).get_queryset().filter(category='SD')


class SoftDrink(Product):
    objects = SoftDrinkManager()

    class Meta:
        proxy = True


class FrozenManager(models.Manager):
    def get_queryset(self):
        return super(FrozenManager, self).get_queryset().filter(category='FG')


class Frozen(Product):
    objects = FrozenManager()

    class Meta:
        proxy = True


class OtherManager(models.Manager):
    def get_queryset(self):
        return super(OtherManager, self).get_queryset().filter(category='OG')


class Other(Product):
    objects = OtherManager()

    class Meta:
        proxy = True
