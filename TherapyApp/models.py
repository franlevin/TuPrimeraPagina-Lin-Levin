from django.db import models
from .choices import modality_choices
from ckeditor.fields import RichTextField

class TherapyRequest(models.Model):
  
    title = models.CharField(max_length = 100)
    modality_required = models.CharField(max_length = 40, choices = modality_choices)
    username = models.CharField(max_length=40)
    request_description = RichTextField()
    budget = models.IntegerField()
    age = models.IntegerField()
    
    def __str__(self):
        return f"Solicitud de {self.username}: {self.title}"
    









