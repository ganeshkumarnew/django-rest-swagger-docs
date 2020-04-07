# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=22)
    phone = models.CharField(max_length=22)
    address = models.CharField(max_length=44)
    designation = models.CharField(max_length=66)