from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class User(models.Model):
    category = models.CharField(max_length=5, default='user')
    username = models.CharField(max_length=30, default='username')
    password = models.CharField(max_length=30, default='password')
    budget   = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(1000000)])
    user_hash = models.CharField(max_length=5, default='*****')
