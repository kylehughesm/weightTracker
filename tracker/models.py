from django.db import models


class Entry(models.Model):
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    datetime = models.DateTimeField(auto_now=True)
