# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse

from .models import ToDo
# Create your views here.
def index(request):
    todos = ToDo.objects.all()[:10]
    context = {
        'todos' : todos
    }
    return render(request,'index.html',context)
def mani(request):
    return render(request,'exp.html')