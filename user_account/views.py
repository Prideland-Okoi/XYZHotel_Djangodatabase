from re import U
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def registration(request):
    if request.method == 'POST':
        user_data = UserCreationForm(request.POST)
        if user_data.is_valid():
            user_data.save()
            return redirect('user_account:registrationsuccessful')

        else:
            return redirect('user_account:registrationsuccessful')
            
   

    context = {

        'form' : UserCreationForm()

    }
    return render(request, 'user_account/registration.html', context)




def registrationsuccessful(request):
    return render(request, 'user_account/registrationsuccessful.html')

def accountlogin(request):
    return render(request, 'user_account/accountlogin.html', )

def accountlogout(request):
    return render(request, 'user_account/accountlogout.html', )

