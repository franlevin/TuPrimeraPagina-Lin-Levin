from django.urls import path
from TherapyApp.views import home, create_user, professional_search

urlpatterns = [
    path('home/', home),
    path('create-user/', create_user),
    path('professional-search/', professional_search),
]