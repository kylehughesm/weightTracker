from django.db import models
from django.conf import settings


class Entry(models.Model):
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
