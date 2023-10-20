from django.db import models

# Create your models here.

class Profesional(models.Model):
    name = models.CharField(max_length = 40)
    surname = models.CharField(max_length = 40)
    specialty = models.CharField(max_length = 30)
    degree = models.CharField(max_length = 40)
    # disponibilidad = models.CharField(max_length = 40)
    modality = models.CharField(max_length = 40)
    fee = models.IntegerField()
    #score = models.IntegerField()
    #id = models.IntegerField(primary_key=True) # DNI: deberia tener un limite de 8 caracteres
    #cuil = models.IntegerField() #el limite es 11 caracteres
    #is_banned = models.BooleanField()
    
    def __str__(self):
        return f"{self.name} {self.surname} ({self.modality})"

class Patient(models.Model):
    name = models.CharField(max_length = 40)
    surname = models.CharField(max_length = 40)
    # date (should replace age for correct calculation)
    age = models.CharField(max_length = 40)
    budget = models.CharField(max_length = 40)
    motive = models.CharField(max_length = 1500)
    score = models.CharField(max_length = 40)
    id = models.IntegerField(primary_key=True) # DNI
    cuil = models.IntegerField()
    is_banned = models.BooleanField()

# class Meeting(models.Model): Va a servir para guardar los datos de cada reunión que se genere entre paciente y profesional

class TherapyRequest(models.Model):
    title = models.CharField(max_length = 100)
    modality_required = models.CharField(max_length = 40)
    username = models.CharField(max_length = 40)
    request_description = models.TextField()
    budget = models.IntegerField()
    age = models.IntegerField()
    
    
    def __str__(self):
        return f"Solicitud de {self.username}: {self.title}"
    









