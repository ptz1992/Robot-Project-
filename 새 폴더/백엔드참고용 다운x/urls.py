from django.contrib import admin
from django.urls import path
from .views import index, create_user, delete_user, update_user, create_minicar,  delete_minicar, update_minicar

app_name = "omorobot"

urlpatterns = [
    path('', index, name="index"),
    path("createuser/", create_user, name="create_user"),
    path("deleteuser/<str:pk>/", delete_user, name="delete_user"),
    path("updateuser/<str:pk>/", update_user, name="update_user"),
    path("createminicar/", create_minicar, name="create_minicar"),
    path("deleteminicar/<int:pk>/", delete_minicar, name="delete_minicar"),
    path("updateminicar/", update_minicar, name="update_minicar"),

]
