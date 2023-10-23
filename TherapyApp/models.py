from django.db import models
from .choices import modality_choices

# class Meeting(models.Model): Va a servir para guardar los datos de cada reunión que se genere entre paciente y profesional

class TherapyRequest(models.Model):
  
    title = models.CharField(max_length = 100)
    modality_required = models.CharField(max_length = 40, choices = modality_choices)
    username = models.CharField(max_length=40)
    request_description = models.TextField()
    budget = models.IntegerField()
    age = models.IntegerField()
    
    def __str__(self):
        return f"Solicitud de {self.username}: {self.title}"
    









