from django.contrib import admin
from django.urls import path
from .views import index, create_user, delete_user, update_user, create_mycar,  delete_mycar, update_mycar, login, enterlogin, join, model, create_model, user, selectcar, chart, create_allmycar, create_textmycar

app_name = "omorobot"

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
    path("createuser/", create_user, name="createuser"),
    path("deleteuser/<str:pk>/", delete_user, name="delete_user"),
    path("updateuser/<str:pk>/", update_user, name="update_user"),
    path("<str:fk>/deletemycar/<int:pk>/", delete_mycar, name="delete_mycar"),
    path("updatemycar/", update_mycar, name="update_mycar"),
    path("login/", login, name="login"),
    path("login/enterlogin/", enterlogin, name="enterlogin"),
    path("join/", join, name="join"),
    path("join/createuser/", create_user, name="createuser"),
    path("model/", model, name="model"),
    path("model/createmodel/", create_model, name ="create_model"),
    path("<str:pk>/", user, name="user"),
    path("<str:pk>/createmycar/", create_mycar, name="create_mycar"),
    path("<str:pk>/createallmycar/", create_allmycar, name="create_allmycar"),
    path("<str:pk>/createtextmycar/", create_textmycar, name="create_textmycar"),
    path("select/", selectcar, name="selectcar"),
    path("select/chart/", chart, name="chart")
]
