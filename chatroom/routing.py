from chatroom import consumers
from channels.routing import route

channel_routing = {
    route('websocket.connect', consumers.ws_connect, path=r"^/ChatRoom/(?P<room_name>[a-zA-Z0-9_]+)/$"),
    route('websocket.receive', consumers.ws_receive, path=r"^/ChatRoom/(?P<room_name>[a-zA-Z0-9_]+)/$"),
    route('websocket.disconnect', consumers.ws_disconnect, path=r"^/ChatRoom/(?P<room_name>[a-zA-Z0-9_]+)/$"),
}
