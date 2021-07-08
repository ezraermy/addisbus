from django.db import models

# Create your models here.
class BusStation(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Line(models.Model):
    origin = models.ForeignKey(BusStation, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(BusStation, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passengers(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    routes = models.ManyToManyField(Line, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"

    class Meta:
        verbose_name_plural = "Passengers"