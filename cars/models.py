from django.db import models

# Create your models here.

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)      #modelo do carro
    brand = models.CharField(max_length=200)      #marca do carro
    factory_year = models.IntegerField(blank=True,null=True)          # ano de fabricaçao
    model_year = models.IntegerField(blank=True,null=True)             #ano do modelo
    value= models.FloatField(blank=True,null=True)              #valor


