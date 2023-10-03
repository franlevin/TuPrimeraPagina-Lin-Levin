from django.shortcuts import render
from django.template import Template

# Create your views here.
def home(request):
       
    return render(request, r'TherapyApp\home.html')

def create_user(request):
    
    return render(request, r'TherapyApp\create_user.html')

def professional_search(request):
    
    return render(request, r'TherapyApp\professional_search.html')

def marulina(request):
    
    return render(request, r'TherapyApp\index.html')
