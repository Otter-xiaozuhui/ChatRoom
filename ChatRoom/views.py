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
        return redirect('PageRegister/?message="用户名不能为空"')
    password = request.POST.get("password")
    if not password:
        return redirect('PageRegister/?message="密码不能为空"')
    repassword = request.POST.get("repassword")
    if not repassword:
        return redirect('PageRegister/?message="重复密码不能为空"')

    t_user = models.User.objects.get(username=username)
    if t_user:
        return redirect('PageRegister/?message="该用户名已被注册s"')

    if password == repassword:
        user = models.User()
        user.username = username
        user.password = make_password(password)
        user.save()

        return redirect('PageLogin/?message="注册成功，请重新登陆"')
    else:
        return redirect('PageRegister/?message="重复密码错误"')


def logout(request):
    username = request.session.get("username")
    if not username:
        redirect('PageLogin/')

    user = models.User.objects.get(username=username)
    if user:
        user.active_status = 0
        user.save()
        del request.session["username"]

        return redirect('PageLogin/')


def Page_Cschat(request):
    username = request.session.get("username")
    if not username:
        redirect('PageLogin/')


