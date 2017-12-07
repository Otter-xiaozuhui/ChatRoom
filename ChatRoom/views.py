from ChatRoom.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from ChatRoom import models
import datetime


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
            request.session["username"] = username
            user.active_status = 1
            user.login_time = datetime.datetime.now()
            user.save()
            # return redirect()
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

    if password == repassword:
        user = models.User()
        user.username = username
        user.password = make_password(password)


def logout(request):
    username = request.session.get("username")
    if not username:
        pass
