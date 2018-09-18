from django.db import models


# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(null=True,blank=True)
    discount = models.FloatField(null=True,blank=True)# 请先检查discount_prices是否设置，discount_price存在的时候禁止设置discount
    weight = models.IntegerField(default=1)
    introduction = models.TextField(blank=True)


class Img(models.Model):
    img_url = models.ImageField()
    img_info = models.CharField(max_length=420,blank=True,null=True)
    img_by = models.ForeignKey(to=Dish, on_delete=models.CASCADE)
