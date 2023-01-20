from django.db import models


class Rooms(models.Model):
    name = models.CharField(max_length = 100)
    price_day = models.FloatField() 
    available = models.BooleanField(default=True)
    time = models.FloatField()
    space = models.FloatField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Cuarto'
        verbose_name_plural = 'Cuartos'