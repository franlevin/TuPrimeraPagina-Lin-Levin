from django.db import models

# Create your models here.

class Profesional(models.Model):
    name = models.CharField(max_length = 40)
    surname = models.CharField(max_length = 40)
    specialty = models.CharField(max_length = 30)
    degree = models.CharField(max_length = 40)
    # disponibilidad = models.CharField(max_length = 40)
    modality = models.CharField(max_length = 40)
    fee = models.IntegerField(max_length = 40)
    score = models.IntegerField(max_length = 40)
    id = models.IntegerField(max_length = 8, primary_key=True) # DNI
    cuil = models.IntegerField(max_length = 11)
    is_banned = models.BooleanField()

class Patient(models.Model):
    name = models.CharField(max_length = 40)
    surname = models.CharField(max_length = 40)
    # date (should replace age for correct calculation)
    age = models.CharField(max_length = 40)
    budget = models.CharField(max_length = 40)
    motive = models.CharField(max_length = 1500)
    score = models.CharField(max_length = 40)
    id = models.IntegerField(max_length = 8, primary_key=True) # DNI
    cuil = models.IntegerField(max_length = 11)
    is_banned = models.BooleanField()

# class Meeting(models.Model): Va a servir para guardar los datos de cada reunión que se genere entre paciente y profesional










