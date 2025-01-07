from django.shortcuts import render
from django.http import HttpResponse
# from Form_data import User
from Form_data.models import User

# Create your views here.


def homepage(request):
    return render(request , 'index.html')

def saveFormData(request):
    if request.method == 'POST':
     Name = request.POST.get('Name')
     Email = request.POST.get('Email')
     Message = request.POST.get('Message')
     user = User(Name=Name , Email=Email , Message=Message)
     user.save()

     return render(request , 'index.html')
