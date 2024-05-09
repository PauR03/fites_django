from django.db import models
from django.contrib.auth.models import User


class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)
    def __str__(self):
        return self.matricula + ' - ' + self.marca + " " + self.model

class Reserva(models.Model):
    auto = models.ForeignKey(Automobil, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.auto.marca + ' - ' + self.client.username

