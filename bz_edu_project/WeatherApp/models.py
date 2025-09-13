from django.db import models


class WeatherModels(models.Model):
    Qnum = models.CharField(max_length=20, null=False)
    City = models.CharField(max_length=20,null=False)
    class Meta:
        db_table = 't_weather_sub'
