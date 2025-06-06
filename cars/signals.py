from django.db.models.signals import pre_save, pre_delete,post_delete,post_save
from django.db.models import Sum
from django.dispatch import receiver
from llm_api.client import get_car_bio
from cars.models import Car, CarInventory

def car_inventory_update():
    cars_count= Car.objects.all().count()
    car_value =Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=car_value
    )

@receiver(post_save,sender=Car)
def car_post_save(sender,instance,**kwargs):
    car_inventory_update()

@receiver(post_delete,sender=Car)
def car_post_delete(sender,instance,**kwargs):
    car_inventory_update()


@receiver(pre_save,sender=Car)
def car_pre_save(sender,instance,**kwargs):
    if not instance.bio:
        ai_bio = get_car_bio(
            model=instance.model,
            brand=instance.brand,
            year=instance.model_year
        )
        instance.bio = ai_bio


