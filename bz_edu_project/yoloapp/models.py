from django.db import models


# Create your models here.
class YoloModels(models.Model):
    img = models.ImageField(upload_to='imgs/')

    class Meta:
        db_table = 't_yolo'
