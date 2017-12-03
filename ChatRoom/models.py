from django.db import models


class User(models.Model):
    '''
    用户的模型
        :username 用户姓名
        :password 用户密码
        :login_time 用户登陆时间
    '''
    username = models.CharField(max_length=20, verbose_name="用户姓名")
    password = models.CharField(max_length=120, verbose_name="用户密码")
    login_time = models.DateTimeField(verbose_name="最后登陆时间")

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
