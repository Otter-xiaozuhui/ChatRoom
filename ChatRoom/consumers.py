from channels import Group
from channels.sessions import channel_session
from ChatRoom.models import *


@channel_session
def ws_connect(message):



    # prefix, label = message['path'].strip('/').split('/')
    # room = Room.objects.get(label=label)
    # Group('chat-' + label).add(message.reply_channel)
    # message.channel_session['room'] = room.label
    pass


@channel_session
def ws_receive(message):
    pass


@channel_session
def ws_disconnect(message):
    pass
