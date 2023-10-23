from django import forms
from .choices import modality_choices
    
class TherapyRequestForm(forms.Form):
    modality = forms.ChoiceField(
        label = "Modalidad", 
        choices = modality_choices,
        required=False,
        widget = forms.Select(attrs={'class':'form-control'})
    )