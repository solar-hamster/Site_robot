from django.db import models
from robot.models import Robot

# Create your models here.
class Order(models.Model):
    robot = models.ForeignKey(Robot, verbose_name='робот-пылесос')
    name = models.CharField('имя', max_length=50)
    phone = models.CharField('телефон', max_length=50)
    date = models.DateTimeField('дата', auto_now_add=True)
