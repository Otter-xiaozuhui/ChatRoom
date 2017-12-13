from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, verbose_name="用户姓名", unique=True)
    password = models.CharField(max_length=120, verbose_name="用户密码")
    login_time = models.DateTimeField(verbose_name="最后登陆时间", null=True)
    active_status = models.IntegerField(verbose_name="活动状态", default=0, choices=((1, "在线"), (-1, "繁忙"), (0, "离线")))

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Room(models.Model):
    room_name = models.CharField(max_length=20, verbose_name="房间名称", default="未命名")
    master = models.ForeignKey(User, verbose_name="房主", related_name='master')
    users = models.ManyToManyField(User, verbose_name="用户", related_name='chaters')
    create_time = models.DateTimeField(verbose_name="创建时间")
    room_password = models.CharField(verbose_name="房间密码", max_length=120, null=True)
    active = models.BooleanField(verbose_name="活跃状态", default=True)

    class Meta:
        verbose_name = '房间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.room_name


class Message(models.Model):
    from_user = models.ForeignKey(User, verbose_name="发送信息的用户")
    # 因为是房间群发，所以没必要在意是谁什么时候接受到了信息，但依旧再次保留
    # to_user = models.ForeignKey(User, verbose_name="接受信息的用户")
    send_time = models.DateTimeField(verbose_name="发送时间")
    room = models.ForeignKey(Room)
    # get_time = models.DateTimeField(verbose_name="接受时间")
    content = models.TextField(verbose_name="信息内容")

    class Meta:
        verbose_name = "信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
