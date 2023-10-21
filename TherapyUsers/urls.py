from django.urls import path
from TherapyUsers.views import login, register, edit_profile, ChangePassword
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/edit/psswrd/', ChangePassword.as_view(), name='change_password'),
    path('logout/', LogoutView.as_view(template_name='TherapyUsers/logout.html'), name='logout'),
] 