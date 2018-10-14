'''
Created on Sep 5, 2018

@author: admin
'''


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'todos/$',views.mani,name = 'mani'),
    url(r'^$',views.index, name = 'index'),
]