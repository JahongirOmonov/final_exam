from django.db import models
from datetime import datetime


# Create your models here.

class FieldModel(models.Model):
    
    name=models.CharField(max_length=100, default='')
    address=models.CharField(max_length=120, default='')
    contact=models.CharField(max_length=15, default='')
    image = models.ImageField(upload_to='field/')
    price_per_hour=models.IntegerField(default=50)
    stadium_length=models.IntegerField(default=10)
    stadium_width=models.IntegerField(default=10)



    class Meta:
        db_table = 'area'

    def __str__(self) -> str:
        return self.name
    
class ReserveModel(models.Model):
    day=models.DateField(default=datetime.now)
    start_time = models.CharField(default='', max_length=50)
    end_time = models.CharField(default='', max_length=50)
    field=models.ForeignKey(FieldModel, on_delete=models.CASCADE)











