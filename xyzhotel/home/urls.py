from django.urls import path
from .import views

app_name='home'
urlpatterns=[
    path('', views.books),
    path('', views.index, name='xyzhotel')
]