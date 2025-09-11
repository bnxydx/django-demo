from django.db import models

# Create your models here.

class ClientModel(models.Model):
    co2 = models.CharField(max_length=10,null=True,blank=True,verbose_name="二氧化碳浓度")
    damp = models.CharField(max_length=10,null=True,blank=True,verbose_name="湿度")
    temperature = models.CharField(max_length=10,null=True,blank=True,verbose_name="温度")
    time = models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table = 't_client'
