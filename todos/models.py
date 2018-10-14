# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from unittest.util import _MAX_LENGTH
from django.views.decorators.http import last_modified
fields = ('Inprogress','completed','pending')
# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=200)
    Description = models.TextField()
    status = models.Value(fields)
    created_at = models.DateTimeField(default=datetime.time,blank = True)
    last_modified
    def __str__(self):
        return self.title