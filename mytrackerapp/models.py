from django.db import models
#import uuid
#from django_mysql.models import DynamicField

class RecordModel(models.Model):
    #uid = models.UUIDField(default=uuid.uuid4,editable=False)
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    buckwheat = models.FloatField(default=0)
    pasta = models.FloatField(default=0)
    rice = models.FloatField(default=0)
    chips = models.FloatField(default=0)
    mandarins = models.FloatField(default=0)
    bread = models.FloatField(default=0)
    chicken = models.FloatField(default=0)
    pork = models.FloatField(default=0)
    beef = models.FloatField(default=0)
    other_meat = models.FloatField(default=0)