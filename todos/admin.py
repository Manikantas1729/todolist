# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from import_export.admin import ImportExportActionModelAdmin
from django.contrib import admin

from .models import ToDo
#from .models import export_as_csv

#admin.site.register(ToDo)
@admin.register(ToDo)
# Register your models here.
class ToDo(ImportExportActionModelAdmin):
    pass