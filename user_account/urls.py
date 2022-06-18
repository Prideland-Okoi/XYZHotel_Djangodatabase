from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user_account'

urlpatterns = [
    path('registeration/', views.registration, name = 'registration' ),
    path('registration_successful/', views.registrationsuccessful, name = 'registrationsuccessful'),
    path('accountlogin/', auth_views.LoginView.as_view(template_name = 'user_account/accountlogin.html'), name = 'accountlogin'),
    path('accountlogout/', auth_views.LogoutView.as_view(template_name = 'user_account/accountlogout.html'), name = 'accountlogout' )

]