from ChatRoom.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password


def Page_Login(request):
    return render(request, 'login.html')


def Page_Register(request):
    return render(request, 'regist.html')


def login(request):
    username = request.POST.get("username")
    if not username:
        return redirect('PageLogin/')
    password = request.POST.get("password")
    if not password:
        return redirect('PageLogin/')
    user = User.objects.get(username=username)
    if user:
        if check_password(password, user.password):
            pass
        else:
            return redirect('PageRegister/')
    else:
        return redirect('PageRegister/')


def register(request):
    username = request.POST.get("username")
    if not username:
        return redirect('PageLogin/')
    password = request.POST.get("password")
    if not password:
        return redirect('PageLogin/')
    repassword = request.POST.get("repassword")
    if not repassword:
        return redirect('PageLogin/')


def logout(request):
    pass