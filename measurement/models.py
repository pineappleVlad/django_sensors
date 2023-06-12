from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor')
    temperature = models.IntegerField()
    date = models.DateField(auto_now_add=True)

