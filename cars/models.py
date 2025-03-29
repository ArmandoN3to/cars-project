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
    plate = models.CharField(max_length=10,blank=True,null=True)
    value= models.FloatField(blank=True,null=True)              #valor
    photo = models.ImageField(upload_to='cars/',blank=True,null=True)

    def __str__(self):
        return self.model     


class CarInventory(models.Model):
    cars_count= models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateField(auto_now_add=True)  

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'