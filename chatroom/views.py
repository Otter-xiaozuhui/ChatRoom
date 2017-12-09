import datetime

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect

from chatroom import models
from django.db.models import Q


def Page_Login(request):
    return render(request, 'login.html')


def Page_Register(request):
    return render(request, 'regist.html')


def login(request):
    print(1)
    username = request.POST.get("username")
    if not username:
        print("lost username")
        return redirect('/PageLogin/')
    password = request.POST.get("password")
    if not password:
        print("lost password")
        return redirect('/PageLogin/')
    user = models.User.objects.get(username=username)
    if user:
        if check_password(password, user.password):
            request.session["username"] = username
            user.active_status = 1
            user.login_time = datetime.datetime.now()
            user.save()
            print("SUCCESS")
            print(user)
            return redirect('/PageCschat/')
        else:
            return redirect('/PageRegister/')
    else:
        return redirect('/PageRegister/')


def register(request):
    username = request.POST.get("username")
    if not username:
        return redirect('/PageRegister/?message="用户名不能为空"')
    password = request.POST.get("password")
    if not password:
        return redirect('/PageRegister/?message="密码不能为空"')
    repassword = request.POST.get("repassword")
    if not repassword:
        return redirect('/PageRegister/?message="重复密码不能为空"')

    t_user = models.User.objects.filter(username=username)
    if t_user.count() > 0:
        print("该用户名已被注册")
        return redirect('/PageRegister/?message="该用户名已被注册"')

    if password == repassword:
        user = models.User()
        user.username = username
        user.password = make_password(password)
        user.save()
        print("注册成功，请重新登陆")
        return redirect('/PageLogin/?message="注册成功，请重新登陆"')
    else:
        return redirect('/PageRegister/?message="重复密码错误"')


def logout(request):
    username = request.session.get("username")
    if not username:
        redirect('/PageLogin/')

    user = models.User.objects.get(username=username)
    if user:
        user.active_status = 0
        user.save()
        del request.session["username"]

    return redirect('/PageLogin/')


def Page_Cschat(request):
    username = request.session.get("username")
    if not username:
        redirect('/PageLogin/')

    chatrooms = models.Room.objects.filter(active=True)
    users = models.User.objects.filter(active_status=1).filter(~Q(username=username))

    return render(request, 'cschat.html', locals())



def create_chatroom(request):
    pass