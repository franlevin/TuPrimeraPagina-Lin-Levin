from django import forms
from .choices import modality_choices
	
class UserCreateForm(forms.Form):
    name = forms.CharField(max_length = 40)
    surname = forms.CharField(max_length = 40)
    specialty = forms.CharField(max_length = 30)
    degree = forms.CharField(max_length = 40)
    modality = forms.CharField(max_length = 40)
    fee = forms.IntegerField()
    
class ProfessionalSearchForm(forms.Form):
    modality = forms.CharField(max_length=50, required=False)
    
class TherapyRequestForm(forms.Form):
    modality = forms.ChoiceField(
        label = "Modalidad", 
        choices = modality_choices,
        required=False,
        widget = forms.Select(attrs={'class':'form-control'})
    )    