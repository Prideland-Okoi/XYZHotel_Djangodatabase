from django.shortcuts import render

# Create your views here.

def xyzlandingpage(request):
    return render(request, 'home/index.html')
