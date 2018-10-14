# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from unittest.util import _MAX_LENGTH
from django.views.decorators.http import last_modified
# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=200)
    Description = models.TextField()
    created_at = models.DateTimeField(default=datetime.time,blank = True)
    stat = (
            ('a','In progress'),
            ('b','completed'),
            ('c','pending'),
           )
    status = models.CharField(max_length=100,default = 'pending',choices=stat)
    last_modified
    def __str__(self):
        return self.title
