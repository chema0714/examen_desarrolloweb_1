# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time

from django.db import models

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=99999,decimal_places=2)
    created = models.CharField(max_length=100,default=time.strftime("%H:%M"))


