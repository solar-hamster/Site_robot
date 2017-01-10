from django.db import models

class Robot(models.Model):
    name = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена")
    description = models.TextField("Описание")
    photo = models.ImageField("фотография", upload_to="robot/photes", default="", blank=True)

    class Meta:
        verbose_name = "робот-пылесос"
        verbose_name_plural = "роботы-пылесосы"
        ordering = ["name"]


    def __str__(self):
        return self.name
