from django.db import models

# Create your models here.
class user_massage(models.Model):
    id = models.IntegerField(primary_key=True)
    photo = models.CharField(max_length=10)  # 手机
    name  = models.CharField(max_length=20)  # 姓名
    age = models.CharField(max_length=50)  # 年龄
    cz = models.CharField(max_length=3)  # 生肖
    region = models.CharField(max_length=30)  # 地区



