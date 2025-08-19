from django.db import models

# Create your models here.
class Tools(models.Model):
    name = models.CharField(max_length=100,verbose_name='工具描述')
    uurl = models.CharField(max_length=1000,verbose_name='跳转链接')

    class Meta:
        db_table = 't_tools'
