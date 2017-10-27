# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import Owner
from django.db import models

# Create your models here.
class Trip(models.Model):
    trip_name = models.CharField(max_length = 255)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.CharField(max_length = 255)
    owner = models.ManyToManyField(Owner, related_name = "trips")
