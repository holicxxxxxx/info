# -*-coding:utf-8-*-
from django.urls import path
from people.views import create_book

urlpatterns=[
    path('create/',create_book),
]