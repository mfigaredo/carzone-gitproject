from django.db import models
from datetime import datetime
from cars.models import Car

# Create your models here.
class Contact(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  car_id = models.IntegerField()
  customer_need = models.CharField(max_length=100)
  car_title = models.CharField(max_length=100)
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=5)
  email = models.EmailField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True, null=True)
  user_id = models.IntegerField(blank=True, null=True)
  create_date = models.DateTimeField(blank=True, default=datetime.now)

  def __str__(self):
    return self.email

  # @property
  def car(self):
    return Car.objects.get(id=self.car_id)