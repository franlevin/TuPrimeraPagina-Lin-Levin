from django.db import models
from django.contrib.auth.models import User

class InfoExtra(models.Model):
    user_type = models.CharField(max_length = 40)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.IntegerField(default=0) # DNI
    age = models.CharField(max_length = 40, default='Unknown')
    budget = models.CharField(max_length = 40, default='Unknown')
    specialty = models.CharField(max_length = 30, default='Unknown')
    degree = models.CharField(max_length = 40, default='Unknown')
    modality = models.CharField(max_length = 40, default='Unknown')
    fee = models.IntegerField(default=0)
    link = models.URLField(null=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)