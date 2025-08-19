from django.db import models

# Create your models here.
class UploadImg(models.Model):
    file = models.FileField(upload_to='files/')
    img = models.ImageField(upload_to='imgs/')
    desc = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.file.name},{self.img.name},{self.desc}'
    class Meta:
        db_table = 't_upload_file'
        verbose_name = "上传文件"