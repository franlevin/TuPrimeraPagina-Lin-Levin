from django.urls import path
from TherapyApp import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('create-user/', views.create_user),
    path('professional-search/', views.professional_search),
    path('about/', views.about, name = 'about'),
    path('therapy-request/', views.TherapyRequestListView.as_view(), name='list-therapy-request'),  
    path('therapy-request/create/', views.TherapyRequestCreateView.as_view(), name='create-therapy-request'),  
    path('therapy-request/<int:pk>/delete/', views.TherapyRequestDeleteView.as_view(), name='delete-therapy-request'),  
    path('therapy-request/<int:pk>/update/', views.TherapyRequestUpdateView.as_view(), name='update-therapy-request'),  
    path('therapy-request/<int:pk>/', views.TherapyRequestDetailView.as_view(), name='detail-therapy-request'), 
    path('therapy-request/search/', views.search_therapy_request, name = 'search-therapy-request') 
]
