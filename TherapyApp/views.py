from django.shortcuts import render
from django.template import Template
from TherapyApp.forms import UserCreateForm, ProfessionalSearchForm
from TherapyApp.models import Profesional, Patient

# Create your views here.
def home(request):
       
    return render(request, r'TherapyApp\home.html')

def create_user(request):
    if request.method == "POST": 
        user_form = UserCreateForm(request.POST)
           
        if user_form.is_valid():
            data = user_form.cleaned_data
            professional = Profesional(name=data.get("name"), surname = data.get("surname"), 
                                        specialty = data.get("specialty"), degree = data.get("degree"),
                                        modality = data.get("modality"), fee = data.get("fee"))
            professional.save()
        else:
            return render(request, r"TherapyApp\create_user.html", {"user_form": user_form})
		
    user_form = UserCreateForm()
    return render(request, r"TherapyApp\create_user.html", {"user_form": user_form})
  
def professional_search(request):
    search_form = ProfessionalSearchForm(request.GET)
    
    if search_form.is_valid():
        modality_to_search = search_form.cleaned_data.get("modality")
        professionals_found = Profesional.objects.filter(modality__icontains = modality_to_search)
    else:       
        professionals_found = Profesional.objects.all()
    
    search_form = ProfessionalSearchForm()
    return render(request, r'TherapyApp\professional_search.html', {"search_form": search_form, "professionals_found" : professionals_found})

def marulina(request):
    
    return render(request, r'SharedTemplates\index.html')
