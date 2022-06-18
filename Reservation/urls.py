from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'Reservation'

urlpatterns = [
    path('book-room/', views.book, name = 'book-room' ),
    path('check-room/', views.check, name = 'check-room' ),
    path('booked/', views.booked, name = 'booked' ),
    

   #path('registration_successful/', views.registrationsuccessful, name = 'registrationsuccessful'),
    #path('login/', auth_views.LoginView.as_view(template_name = 'user_account/accountlogin.html'), name = 'accountlogin'),
    #path('logout/', auth_views.LogoutView.as_view(template_name = 'user_account/accountlogout.html'), name = 'accountlogout' )

]