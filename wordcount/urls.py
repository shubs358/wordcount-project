
from django.urls import path
from . import hello

urlpatterns = [
    path('', hello.home),
    path('countsord/',hello.count, name="count")
]
