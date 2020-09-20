from django.conf import settings
from django.db import models

# Create your models here.


class UserStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=120)

    def __unicode__(self):
        return str(self.stripe_id)

# cus_I3FjRWXlpElTm6
# cus_I3FrRjBWruGLl8
# cus_I3FrRjBWruGLl8


