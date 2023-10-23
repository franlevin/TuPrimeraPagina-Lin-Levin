from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

class MyRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {campo: '' for campo in fields}
    
class MyPatientEditProfileForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='Cambiar email')
    first_name = forms.CharField(label='Nombre', max_length=30)
    last_name = forms.CharField(label='Apellido', max_length=50)
    dni = forms.IntegerField() # DNI
    age = forms.CharField(label='Edad', max_length = 40)
    budget = forms.CharField(label='Presupuesto', max_length = 40)
    link = forms.URLField(required=False)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'dni', 'age', 'budget', 'link', 'avatar']

class MyTherapistEditProfileForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='Cambiar email')
    first_name = forms.CharField(label='Nombre', max_length=30)
    last_name = forms.CharField(label='Apellido', max_length=50)
    dni = forms.IntegerField() # DNI
    specialty = forms.CharField(max_length = 30)
    degree = forms.CharField(max_length = 40)
    modality = forms.CharField(max_length = 40)
    fee = forms.IntegerField()
    link = forms.URLField(required=False)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'dni', 'specialty', 'degree', 'modality', 'fee', 'link', 'avatar']