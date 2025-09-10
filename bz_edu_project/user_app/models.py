from django.db import models
import hashlib

# Create your models here.
class User(models.Model):
    objects = models.Manager()
    GENDER_CHOICES = (
        (0,'女'),
        (1,'男'),
    )
    phone = models.CharField(null=True, max_length=11, verbose_name='手机号')
    _password = models.CharField(null=True, blank=True, max_length=100, verbose_name='真实密码')
    password = models.CharField(null=True, blank=True, max_length=100, verbose_name='密码', db_column=None)
    nickname = models.CharField(null=True, max_length=50, blank=True, verbose_name='昵称')
    gender = models.IntegerField(null=True, blank=True, verbose_name='性别', choices=GENDER_CHOICES, default=1)
    job_title = models.CharField(null=True, max_length=50, blank=True, verbose_name='职称')
    introduction = models.TextField(null=True, blank=True, verbose_name='简介')
    avatar = models.CharField(null=True, blank=True, max_length=50, verbose_name='头像')

    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 't_user'
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,pwd):
        self._password = hashlib.md5(pwd.encode('utf-8')).hexdigest()

    def check_password(self, raw_password):
        encrypted = hashlib.md5(raw_password.encode()).hexdigest()
        return encrypted == self._password
    

