from django.db import models


class RecordModel(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()

    buckwheat = models.FloatField(default=0)
    pasta = models.FloatField(default=0)
    rice = models.FloatField(default=0)
    
    chicken = models.FloatField(default=0)
    pork = models.FloatField(default=0)
    beef = models.FloatField(default=0)
    
    potatoe = models.FloatField(default=0)
    carrot = models.FloatField(default=0)
    ququmber = models.FloatField(default=0)
    tomato = models.FloatField(default=0)

    eggs = models.FloatField(default=0)
    milk = models.FloatField(default=0)
    cheese = models.FloatField(default=0)
    cottage_cheese = models.FloatField(default=0)

    bananas = models.FloatField(default=0)
    mandarins = models.FloatField(default=0)
    
    bread = models.FloatField(default=0)
    
    chips = models.FloatField(default=0)
    
    
    