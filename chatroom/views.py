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
    username = request.POST.get("username")
    if not username:
        return redirect('/PageLogin/')
    password = request.POST.get("password")
    if not password:
        return redirect('/PageLogin/')
    user = models.User.objects.get(username=username)
    if user:
        if check_password(password, user.password):
            request.session["username"] = username
            user.active_status = 1
            user.login_time = datetime.datetime.now()
            user.save()
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
    username = request.session.get("username")
    if not username:
        redirect('/PageLogin/')

    roomname = request.POST.get("room_name")
    password = request.POST.get("room_password")

    try:
        chat_room = models.Room()
        if not roomname:
            print("no room name")
            return redirect('/PageCschat/')

        if models.Room.objects.filter(room_name=roomname).count() > 0:
            print("name is too much")
            return redirect('/PageCschat/')

        chat_room.room_name = roomname
        chat_room.master = models.User.objects.get(username=username)
        # import binascii
        # import uuid
        # chat_room.room_uid = str(binascii.b2a_hex(roomname.encode('utf-8'))) + str(uuid.uuid1())

        if password:
            chat_room.room_password = password

        chat_room.create_time = datetime.datetime.now()

        chat_room.save()

        return redirect('/PageChatRoom/')

    except Exception as err:
        print(err)
        return redirect('/PageCschat/')


def add_user_into_room(request):
    pass


def Page_ChatRoom(request, cn):
    username = request.session.get("username")
    if not username:
        redirect('/PageLogin/')

    room = models.Room.objects.filter(id=cn)

    if not room:
        return redirect('/PageCschat/')

    room = room[0]

    messages = models.Message.objects.get(room=room)

    return render(request, 'chatroom.html', locals())


def into_room(request):
    # 这边要判断，是否房主进入、是否有密码、是否有权限（是否是房间用户）
    username = request.session.get("username")
    if not username:
        print(1)
        redirect('/PageLogin/')
    # 密码以后再认证

    room_id = request.POST.get("chatroom")
    print(room_id)

    room = models.Room.objects.filter(id=room_id)

    print(room)
    if not room:
        return redirect('/PageCschat/')

    room = room[0]

    if not room.active:
        return redirect('/PageCschat/')

    if room.master.username == username:
        return redirect('/PageChatRoom/' + room_id)

    if username in [u.username for u in room.users]:
        return redirect('/PageChatRoom/' + room_id)

    return redirect('/PageCschat/')
