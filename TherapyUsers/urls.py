from django.urls import path
from TherapyUsers.views import login, edit_patient_profile, edit_therapist_profile, view_patient_profile, view_therapist_profile, register_menu, register, ChangePassword
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('register-menu/', register_menu, name='register_menu'),
    path('profile/view/patient', view_patient_profile, name='view_patient_profile'),
    path('profile/view/therapist', view_therapist_profile, name='view_therapist_profile'),
    path('profile/edit/patient', edit_patient_profile, name='edit_patient_profile'),
    path('profile/edit/therapist', edit_therapist_profile, name='edit_therapist_profile'),
    path('profile/edit/psswrd/', ChangePassword.as_view(), name='change_password'),
    path('logout/', LogoutView.as_view(template_name='TherapyUsers/logout.html'), name='logout'),
] 
