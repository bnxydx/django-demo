from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name='教师姓名')
    brief = models.CharField(null=True, blank=True, max_length=512, verbose_name='教师简介')
    avatar = models.CharField(null=True, blank=True, max_length=512, verbose_name='教师头像')
    position = models.CharField(null=True, blank=True, max_length=20, verbose_name='教师职位')
    characteristic = models.CharField(null=True, blank=True, max_length=256, verbose_name='教师特点')

    class Meta:
        db_table = 't_teacher'
