from ast import pattern
from django import views
from django.urls import  re_path
from app_ecoponto import views

urlpatterns = [
     re_path(r'^$',views.listview),  
    ]
