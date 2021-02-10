from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.contrib.auth.models import User

# Create your models here.
class Workout(models.Model):
    activity = models.CharField(max_length=100)
    howLong = models.IntegerField()
    description = models.TextField(max_length=300)
    time = models.DateTimeField('Workout Time', default= datetime.now(), blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)

    def __str__(self):
        return self.activity

    def get_absolute_url(self):
        return reverse('detail', kwargs={'workout_id': self.id})

class Food(models.Model):
    item = models.CharField(max_length=100)
    calories = models.IntegerField()
    meal = models.CharField(max_length=100)
    time = models.DateTimeField('Meal Time', default= datetime.now(), blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('detail', kwargs={'food_id': self.id})
