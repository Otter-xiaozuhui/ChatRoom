"""ChatRoom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from chatroom import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^PageLogin/', views.Page_Login, name='Pagelogin'),
    url(r'^Login/', views.login, name='Login'),
    url(r'^PageRegister/', views.Page_Register, name='PageRegister'),
    url(r'^Register/', views.register, name='Register'),
    url(r'^Logout/', views.logout, name='Logout'),
    url(r'^PageCschat/', views.Page_Cschat, name='PageCschat'),
    url(r'^CreateChatroom/', views.create_chatroom, name='CreateChatroom'),
    url(r'^AddUserIntoRoom/', views.add_user_into_room, name='AddUserIntoRoom'),
    url(r'^PageChatRoom/(?P<cn>\w+)', views.Page_ChatRoom, name='PageChatRoom'),
    url(r'^IntoRoom/', views.into_room, name='IntoRoom'),
    url(r'^', views.Page_Login),

]
