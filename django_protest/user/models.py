from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=64)

    class Meta:
        db_table = 't_user'


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)

    servers_hot = models.BooleanField(default=False)
    servers_clod = models.BooleanField(default=False)

    def __str__(self):
        return f"餐厅: {self.place.name} - 地址: {self.place.address}"
    class Meta:
        db_table = 't_restaurant'


class Waiter(models.Model):
    """
   服务员
   """
    name = models.CharField(max_length=32, verbose_name='人名')
    induction = models.DateTimeField(verbose_name='入职时间', null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='所在餐厅', null=True)

    def __str__(self):
        return f'{self.name} == {self.induction}'

    class Meta:
        db_table = 't_waiter'


class Food(models.Model):
    """
   食物
   """
    name = models.CharField(max_length=32, verbose_name='菜名')
    is_main = models.BooleanField(default=True, verbose_name='是否是主食', null=True)
    restaurant = models.ManyToManyField(Restaurant, verbose_name='哪个餐厅有', null=True)

    class Meta:
        db_table = 't_food'


if __name__ == '__main__':
    place = Place.objects.first()
    print(place.restaurant)