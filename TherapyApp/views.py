from django.shortcuts import render
from TherapyApp.forms import TherapyRequestForm
from TherapyApp.models import TherapyRequest

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):  
    return render(request, r'TherapyApp\home.html')

def about(request):
    return render(request, r'TherapyApp\about.html')

class TherapyRequestCreateView(CreateView):
    model = TherapyRequest
    template_name = "TherapyApp/create_therapy_request.html"
    fields = ['title', 'modality_required', 'username', 'request_description', 'budget', 'age']
    success_url = reverse_lazy('list-therapy-request')
    labels = {
            'title': 'Titulo',
            'modality_required': "Modalidad requerida",
            'username': "Nombre de usuario",
            'request_description': 'Descripción de la Solicitud',
            'budget': 'Presupuesto',
            'age': 'Edad'          
    }
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field, label in self.labels.items():
            form.fields[field].label = label
        return form

class TherapyRequestDeleteView(DeleteView):
    model = TherapyRequest
    template_name = "TherapyApp/delete_therapy_request.html"
    success_url = reverse_lazy('list-therapy-request')
    
class TherapyRequestDetailView(DetailView):
    model = TherapyRequest
    template_name = "TherapyApp/detail_therapy_request.html"
    
class TherapyRequestListView(ListView):
    model = TherapyRequest
    context_object_name = 'therapy_request_list'
    template_name = "TherapyApp/list_therapy_request.html"
    
class TherapyRequestUpdateView(UpdateView):
    model = TherapyRequest
    template_name = "TherapyApp/update_therapy_request.html"
    fields = ['title', 'modality_required', 'username', 'request_description', 'budget', 'age']
    success_url = reverse_lazy('list-therapy-request')

def search_therapy_request(request):
    search_form = TherapyRequestForm(request.GET)
    
    if search_form.is_valid():
        modality_to_search = search_form.cleaned_data.get("modality")
        therapy_request_found = TherapyRequest.objects.filter(modality_required__icontains = modality_to_search)
    else:       
        therapy_request_found = TherapyRequest.objects.all()
    
    search_form = TherapyRequestForm(request.GET)
    return render(request, r'TherapyApp\search_therapy_request.html', 
                  {"search_form": search_form, "therapy_request_found" : therapy_request_found})

def modalities(request):
    return render(request, r'TherapyApp\modalities.html')