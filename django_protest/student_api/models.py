from django.db import models


class Classes(models.Model):
    name = models.CharField(max_length=20, verbose_name='班级')

    class Meta:
        db_table = 't_class'


# Create your models here.
class Student(models.Model):
    SEX_CHOICES = ((1, '男'), (2, '女'))
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(null=True, blank=True, verbose_name='年龄')
    sex = models.IntegerField(choices=SEX_CHOICES, default=1, verbose_name='性别')
    classes = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True, verbose_name='班级',related_name='students')

    class Meta:
        db_table = 't_student'
