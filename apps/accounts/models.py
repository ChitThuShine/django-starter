from django.db import models

# Create your models here.

from typing import Optional, List


class DailyEntry(models.Model):
    #entry_types = ['sale','opcost','expense']
    product = models.CharField(max_length=300, blank=True)
    open = models.FloatField(null=True, blank=True)
    close = models.FloatField(null=True, blank=True)
    sold = models.FloatField(null=True, blank=True)
    add= models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)

    #  entry_type = models.CharField(blank=True, choices=zip(entry_types, entry_types))