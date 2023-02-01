from django.shortcuts import render
from .models import User, Mycar , Model
from django.http import HttpResponseRedirect
from django.urls import reverse
import sqlite3
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


context = {
            "joinmessage" : "",
            "message" : "",
            }

# main index페이지 보여주기
def index(request):
    mycar = Mycar.objects.all()
    global context
    context = {
        "joinmessage" : "이니셜 페이지",
        "message" : "",
        "mycars": mycar
    }
    return render(request, "index.html", context)

# mycar Controller
# def index(request, pk):
#     mycar = Mycar.objects.all()
#     context = {"mycars": mycar}
#     return render(request, "index.html", context)


# 회원별 index페이지 보여주기
def user(request, pk) :
    mycar = Mycar.objects.all()
    print(mycar)
    mymodel = Model.objects.all()
    old_user = User.objects.get(user_name=f"{pk}")
    username = old_user.user_name
    usermodel = old_user.model_name
    context = {
        "context" : "login한 유저가 있따." ,
        "user_name" : username,
        "user_model" : usermodel,
        "mycars" : mycar,
        "mymodel": mymodel
    }
    return render(request, "index.html", context)

#회원가입
def join(request) :
    return render(request, "join.html", context)

# 회원가입로직
def create_user(request) :
    global context
    if request.method == "POST":
        join_username = request.POST.get("username")
        join_password = request.POST.get("password")
        join_confirm = request.POST.get("password_confirm")

        # 빈칸 확인
        if join_username == "" :
            context = {
                "message" : "ID를 입력하세요"
            }
            return HttpResponseRedirect(reverse("omorobot:join"))
        # 중복아이디 확인
        elif User.objects.filter(user_name = f"{join_username}").exists() :
            context = {
                "message" : "중복id가있다."
            }
            return HttpResponseRedirect(reverse("omorobot:join"))  
        else :
            # 암호 빈칸확인
            if join_password == "" :
                context = {
                    "message" : "PW가 비어있습니다"
                }
                return HttpResponseRedirect(reverse("omorobot:join"))
            # 암호가 같은지 확인
            # 같으면 로그인 된 회원페이지로 이동
            else :
                if join_password == join_confirm :
                    new_user = User()
                    new_user.user_name = join_username
                    new_user.user_password = join_password
                    new_user.save()
                    return HttpResponseRedirect(f"/{join_username}")
                else : 
                    context ={
                        "message" : "비밀번호 확인하세요"
                    }
                    return HttpResponseRedirect(reverse("omorobot:join"))
    else :
        return render(request, "join.html", context)


# 모델생성페이지
def model(request):
    return render(request, "model.html")

# create 모델
def create_model(request) : 
    new_model = Model()
    new_model.model_name = request.GET.get("model_name")
    new_model.model_size = request.GET.get("model_size")
    new_model.model_battery = request.GET.get("model_battery")
    new_model.model_weight = request.GET.get("model_weight")
    new_model.model_firmware = request.GET.get("model_firmware")
    new_model.save()
    context ={
        "message" : "모델생성이 완료되었습니다."
    }
    return render(request, "model.html", context)

# 로그인페이지
def login(request) :
    return render(request, "login.html", context)

# 로그인 로직
def enterlogin(request) :
    global context
    if request.method == "POST":
        login_username = request.POST.get("username")
        login_password = request.POST.get("password")

        # 빈칸 확인
        if login_username == "" :
            context = {
                "message" : "ID를 입력하세요"
            }
            return HttpResponseRedirect(reverse("omorobot:login"))
                
        else :
            # 암호 빈칸확인
            if login_password == "" :
                context = {
                    "message" : "PW가 비어있습니다"
                }
                return HttpResponseRedirect(reverse("omorobot:login"))
            # 같으면 로그인 된 회원페이지로 이동
            else :
                if User.objects.filter(user_name = f"{login_username}").exists() :
                    old_user = User.objects.get(user_name = f"{login_username}")
                    user_password = old_user.user_password
                    if user_password != login_password :
                        context ={
                            "message" : "비밀번호 확인하세요"
                        }
                        return HttpResponseRedirect(reverse("omorobot:login"))
                    else : 
                        return HttpResponseRedirect(f"/{login_username}/")
                else : 
                    context ={
                        "message" : "아이디가 없습니다"
                        }
                    return HttpResponseRedirect(reverse("omorobot:login"))                    
    else :
        return render(request, "login.html", context)


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


def create_mycar(request, pk):
    if request.method == "POST" :
        mycarseletor = request.POST.get("mycarselector")
        number = request.POST.get("number")
        new_minicar = Mycar()
        old_user = User.objects.get(user_name=f"{pk}")
        new_minicar.user_name = old_user

        if mycarseletor == "speed" :
            new_minicar.mycar_speed = int(number)
        elif mycarseletor == "battery":
            new_minicar.mycar_battery = int(number)
        else:
            new_minicar.mycar_color = number
        new_minicar.save()
        return HttpResponseRedirect(f"/{pk}")

def create_allmycar(request, pk):
    if request.method == "POST" : 
        mycar_speed = request.POST.get("speed")
        mycar_battery = request.POST.get("battery")
        mycar_color = request.POST.get("color")
        new_minicar = Mycar()
        old_user = User.objects.get(user_name=f"{pk}")
        new_minicar.user_name = old_user
        new_minicar.mycar_speed = int(mycar_speed)
        new_minicar.mycar_battery = int(mycar_battery)
        new_minicar.mycar_color = mycar_color
        new_minicar.save()
        return HttpResponseRedirect(f"/{pk}")

def create_textmycar(request, pk):
    if request.method == "POST" :
        carset = request.POST.get("carset")
        carnum = request.POST.get("carnum")
        new_minicar = Mycar()
        old_user = User.objects.get(user_name=f"{pk}")
        new_minicar.user_name = old_user
        if carset == "speed" :
            new_minicar.mycar_speed = int(carnum)
        elif carset == "battery":
            new_minicar.mycar_battery = int(carnum)
        elif carset == "color":
            new_minicar.mycar_color = carnum
        else:
            context ={
                            "message" : "망했어요."
                        }
            # return render(request, "index.html", context)

        new_minicar.save()
        return HttpResponseRedirect(f"/{pk}", context)

def delete_mycar(request, pk, fk):
    mycar = Mycar.objects.filter(user_name=fk)
    del_mycar = mycar.filter(pk = pk)
    del_mycar.delete()
    return HttpResponseRedirect(f"/{fk}")

def update_mycar(request, pk) :
  if request.method == "POST" :
    mycar_speed = request.POST.get("speed")
    mycar_battery = request.POST.get("battery")
    mycar_color = request.POST.get("color")
    old_minicar = Mycar.objects.get(pk=pk)
    old_minicar.speed = mycar_speed
    old_minicar.battery = mycar_battery
    old_minicar.color = mycar_color
    old_minicar.save()
    return HttpResponseRedirect(reverse("omorobot:index"))

def selectcar(request):
    old_mycar = Mycar.objects.all()
    sel_speed = request.GET.get("speed")
    sel_encoder = request.GET.get("encoder")
    con_speed = Mycar.objects.filter(mycar_speed = sel_speed)
    final_mycar= con_speed.filter(mycar_encoder_or = sel_encoder)

    print(final_mycar)
    context = {
        "mycars" : final_mycar,
    }
    return render(request, "index.html", context)

@csrf_exempt
def chart(request):
    if request.method=="POST":
        data =json.loads(request.body)
        print("들어온 데이터 : ", data)
       
        print(data["speed"], data["encoder"])

        qs = Mycar.objects.filter(mycar_speed=data["speed"], mycar_encoder_or=data["encoder"])

        ac_dict = {}
        i = 0
        for s in qs: 
            ac_dict[i] = s.mycar_encoder_ac
            i += 1

        i =5 
        for b in qs:
            ac_dict[i] = b.mycar_battery
            i += 1
        
        i =10
        for e in qs:
            ac_dict[i] = e.mycar_encoder_or
            i += 1
        
        i =15
        for c in qs:
            ac_dict[i] = c.mycar_color
            i += 1
        
        ac_dict['length'] = i

        return JsonResponse(ac_dict)
        