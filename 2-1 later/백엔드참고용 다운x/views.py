from django.shortcuts import render
from .models import User, Minicar
from django.http import HttpResponseRedirect
from django.urls import reverse

# User Controller
def index(request):
    user = User.objects.all()
    minicar_list = Minicar.objects.all()
    context = {"minicars" : minicar_list, "users": user}
    return render(request, "index.html", context)

def create_user(request):
  if request.method == "POST" :
    user_name = request.POST.get("name")
    user_model = request.POST.get("model")
    new_user = User()

    new_user.name = user_name
    new_user.models = user_model
    new_user.save()
    return HttpResponseRedirect(reverse("omorobot:index"))

def delete_user(request, pk):
    del_user = User.objects.filter(pk=pk)
    del_user.delete()
    return HttpResponseRedirect(reverse("omorobot:index"))

def update_user(request, pk) :
  if request.method == "POST" :
    user_model = request.POST.get("model")
    old_user = User.objects.get(pk=pk)
    old_user.models = user_model
    old_user.save()
    return HttpResponseRedirect(reverse("omorobot:index"))

# Minicar Controller

def create_minicar(request):
  if request.method == "POST" :
    minicar_speed = request.POST.get("speed")
    minicar_battery = request.POST.get("battery")
    minicar_color = request.POST.get("color")
    new_minicar = Minicar()
    
    new_minicar.speed = minicar_speed
    new_minicar.battery = minicar_battery
    new_minicar.color = minicar_color
    new_minicar.save()
    return HttpResponseRedirect(reverse("omorobot:index"))

def delete_minicar(request, pk):
    del_minicar = Minicar.objects.filter(pk=pk)
    del_minicar.delete()
    return HttpResponseRedirect(reverse("omorobot:index"))

def update_minicar(request, pk) :
  if request.method == "POST" :
    minicar_speed = request.POST.get("speed")
    minicar_battery = request.POST.get("battery")
    minicar_color = request.POST.get("color")
    old_minicar = Minicar.objects.get(pk=pk)
    old_minicar.speed = minicar_speed
    old_minicar.battery = minicar_battery
    old_minicar.color = minicar_color
    old_minicar.save()
    return HttpResponseRedirect(reverse("omorobot:index"))
