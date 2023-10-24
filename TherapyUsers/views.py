from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from TherapyUsers.forms import MyRegisterForm, MyPatientEditProfileForm, MyTherapistEditProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from TherapyUsers.models import InfoExtra
from django.contrib.auth.models import User

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            usuario = authenticate(username=username, password=password)
            
            django_login(request, usuario)
            
            InfoExtra.objects.get_or_create(user=usuario)
            
            return redirect('home')
    else:
        formulario = AuthenticationForm()
        
    return render(request, 'TherapyUsers/login.html', {'formulario': formulario})

def register_menu(request):
  
    return render(request, 'TherapyUsers/register_menu.html')

def register(request):
    if request.method == 'POST':
        formulario = MyRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = formulario = MyRegisterForm()

    return render(request, 'TherapyUsers/register.html', {'formulario': formulario})

@login_required
def edit_patient_profile(request):

    info_extra = request.user.infoextra

    request.user.infoextra.user_type = 'Patient'

    if request.method == 'POST':
        formulario = MyPatientEditProfileForm(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():

            info_extra.link = formulario.cleaned_data.get('link')
            if formulario.cleaned_data.get('avatar'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
            info_extra.dni = formulario.cleaned_data.get('dni')
            info_extra.age = formulario.cleaned_data.get('age')
            info_extra.budget = formulario.cleaned_data.get('budget')
            
            info_extra.save()

            formulario.save()
            return redirect('home')
    else:
        formulario = MyPatientEditProfileForm(initial={'link': info_extra.link, 'avatar': info_extra.avatar, 'dni': info_extra.dni,
                                                       'age': info_extra.age, 'budget': info_extra.budget}, instance=request.user)
    return render(request, 'TherapyUsers/edit_patient_profile.html', {'formulario': formulario})

@login_required
def edit_therapist_profile(request):

    info_extra = request.user.infoextra

    request.user.infoextra.user_type = 'Therapist'

    if request.method == 'POST':
        formulario = MyTherapistEditProfileForm(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():

            info_extra.link = formulario.cleaned_data.get('link')
            if formulario.cleaned_data.get('avatar'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
            info_extra.dni = formulario.cleaned_data.get('dni')
            info_extra.specialty = formulario.cleaned_data.get('specialty')
            info_extra.degree = formulario.cleaned_data.get('degree')
            info_extra.modality = formulario.cleaned_data.get('modality')
            info_extra.fee = formulario.cleaned_data.get('fee')
            
            info_extra.save()

            formulario.save()
            return redirect('home')
    else:
        formulario = MyTherapistEditProfileForm(initial={'link': info_extra.link, 'avatar': info_extra.avatar, 'dni': info_extra.dni, 
                                                         'specialty': info_extra.specialty, 'degree': info_extra.degree, 'modality': info_extra.modality, 'fee': info_extra.fee}, instance=request.user)
    return render(request, 'TherapyUsers/edit_therapist_profile.html', {'formulario': formulario})

@login_required
def view_patient_profile(request):
    user_data = {
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'dni': request.user.infoextra.dni,
        'age': request.user.infoextra.age,
        'budget': request.user.infoextra.budget,
        'link': request.user.infoextra.link if hasattr(request.user, 'infoextra') else None,
        'avatar': request.user.infoextra.avatar.url if hasattr(request.user, 'infoextra') and request.user.infoextra.avatar else None,
    }
    return render(request, 'TherapyUsers/view_patient_profile.html', {'user_data': user_data})

@login_required
def view_therapist_profile(request):
    user_data = {
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'dni': request.user.infoextra.dni,
        'specialty': request.user.infoextra.specialty,
        'degree': request.user.infoextra.degree,
        'modality': request.user.infoextra.modality,
        'fee': request.user.infoextra.fee,
        'link': request.user.infoextra.link if hasattr(request.user, 'infoextra') else None,
        'avatar': request.user.infoextra.avatar.url if hasattr(request.user, 'infoextra') and request.user.infoextra.avatar else None,
    }
    return render(request, 'TherapyUsers/view_therapist_profile.html', {'user_data': user_data})

class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'TherapyUsers/change_password.html'
    success_url = reverse_lazy('edit_profile')