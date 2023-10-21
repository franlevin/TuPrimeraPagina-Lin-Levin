from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from TherapyUsers.forms import MyRegisterForm, MyEditProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from TherapyUsers.models import InfoExtra

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

def register(request):
    
    if request.method == 'POST':
        formulario = MyRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = MyRegisterForm()
        
    return render(request, 'TherapyUsers/register.html', {'formulario': formulario})

@login_required
def edit_profile(request):
    
    info_extra = request.user.infoextra
    
    if request.method == 'POST':
        formulario = MyEditProfileForm(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            info_extra.link = formulario.cleaned_data.get('link')
            if formulario.cleaned_data.get('avatar'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
            info_extra.save()
            
            formulario.save()
            return redirect('home')
    else:
        formulario = MyEditProfileForm(initial={'link': info_extra.link, 'avatar': info_extra.avatar}, instance=request.user)
    return render(request, 'TherapyUsers/edit_profile.html', {'formulario': formulario})


class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'TherapyUsers/edit_profile.html'
    success_url = reverse_lazy('edit_profile')