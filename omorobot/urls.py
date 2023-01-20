from django.contrib import admin
from django.urls import path
from .views import index, read, delete

app_name = "omorobot"

urlpatterns = [
    path('', index, name="index"),
    path("read/", read),
    path("delete/", delete),
]