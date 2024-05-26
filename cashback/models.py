from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.
class User(models.Model):
    category = models.CharField(max_length=5, default='user')
    username = models.CharField(max_length=30, default='username')
    password = models.CharField(max_length=30, default='password')
    budget   = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(1000000)])
    user_hash = models.CharField(max_length=5, default='*****')

    def __str__(self):
        return "{}, {}, {}".format(self.username, self.user_hash, self.budget)

class Logs(models.Model):
    user_hash = models.CharField(max_length=5, default='*****')
    amount   = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(1000000)])
    date_time = models.CharField(max_length=10, default=datetime.datetime.today())
