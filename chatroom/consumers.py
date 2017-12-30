from channels.sessions import channel_session
from channels import Group
import json
from chatroom import models
import datetime


@channel_session
def ws_connect(message, room_name):
    # message.reply_channel.send({"text": "連接成功"})
    Group(room_name).add(message.reply_channel)


@channel_session
def ws_receive(message, room_name):
    message.reply_channel.send({"text": "數據發送成功"})
    print(message.content.get("text"))

    data = json.loads(message.content.get("text"))

    try:
        room = models.Room.objects.filter(room_name=room_name)[0]
    except Exception as err:
        message.reply_channel.send({"error": "服务器错误"})
        return

    try:
        username = data.get("username")
        user = models.User.objects.filter(username=username)[0]
    except Exception as err:
        message.reply_channel.send({"error": "服务器错误"})
        return

    try:
        content = data.get("content")
    except Exception as err:
        message.reply_channel.send({"error": "服务器错误"})
        return

    message = models.Message()
    message.room = room
    message.from_user = user
    message.content = content
    message.send_time = datetime.datetime.now()

    message.save()

    d = {
        "send_time": str(message.send_time),
        "from_user": username,
        "content": content,
    }

    print(d)

    Group(room_name).send({
        "text": json.dumps(d)
    })


@channel_session
def ws_disconnect(message, room_name):
    # message.reply_channel.send({"text": "連接斷開"})
    Group(room_name).discard(message.reply_channel)
