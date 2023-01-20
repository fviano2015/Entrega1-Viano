from django.db import models

class Transport(models.Model):
    type = models.CharField(max_length = 50)
    time = models.FloatField()
    place = models.CharField(max_length = 200)
    price = models.FloatField()

    def __str__(self):
        return self.type
    class Meta:
        verbose_name = 'Transporte'
        verbose_name_plural = 'Transportes'


class Activities(models.Model):
    name = models.CharField(max_length = 50)
    time = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'


