from ChatRoom.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password


def Page_Login(request):
    return render(request, 'login.html')


def login(request):
    username = request.POST.get("username")
    if not username:
        return redirect('PageLogin/')
    password = request.POST.get("password")
    if not password:
        return redirect('PageLogin/')
    user = User.objects.get(username=username)
    if user:
        password = make_password(password)
        if password == user.password:
            return redirect('PageLogin/')
        else:
            return redirect('PageLogin/')
    else:
        return redirect('PageLogin/')
