from django.db import models

# Create your models here.

class Brand(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)      #modelo do carro
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,related_name='car_brand')     #marca do carro
    factory_year = models.IntegerField(blank=True,null=True)          # ano de fabricaçao
    model_year = models.IntegerField(blank=True,null=True)             #ano do modelo
    value= models.FloatField(blank=True,null=True)              #valor


    def __str__(self):
        return self.model       