# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=200)
    test = models.TextField()
    created_at = models.DateTimeField(default=datetime.time,blank = True)
    def __str__(self):
        return self.title
        