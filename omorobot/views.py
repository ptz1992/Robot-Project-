from django.shortcuts import render
from .models import User, Minicar
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt



# 전송해서 저장 (Create)
@csrf_exempt
def index(request):
  if request.method == "POST" :
    minicar_speed = request.POST.get("speed")
    minicar_battery = request.POST.get("battery")
    minicar_color = request.POST.get("color")
    month_text = request.POST.get('month')

    new_minicar = Minicar()
    new_minicar.speed = minicar_speed
    new_minicar.battery = minicar_battery
    new_minicar.color = minicar_color
    new_minicar.month = month_text

    new_minicar.save()

    return HttpResponseRedirect(reverse("omorobot:index"))
  else :
    minicar_list = Minicar.objects.all()
    context = {"minicars" : minicar_list}
    return render(request, "index.html", context)

 # 조회하기 (read)
@csrf_exempt
def read(request):
  Minicars = Minicar.objects.all()
  context = {
    "Minicars" : Minicars
  }
  return render(request, "index.html", context)

# 업데이트 (update)

def update(request):
  return render(request, "update.html")

# 삭제하기 (delete)
@csrf_exempt
def delete(request):
    if request.method == "POST" :
      dele = Minicar.objects.all()
      dele.delete()
      return HttpResponseRedirect(reverse("omorobot:index"))
    else :
      Minicar_list = Minicar.objects.all()
      context = {"Minicar_list" : Minicar_list}
      return render(request, "index.html", context)