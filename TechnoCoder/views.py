from django.shortcuts import render
from django.http import HttpResponse
from Techno.forms import *
from django.core.exceptions import ValidationError
from TechnoCoder.models import *
            
# Create your views here.
def login(request):
    if(request.method=='POST'):
        form = Login(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
    else:
        form= Login()
    return render(request, 'login.html',{'form':form})

def register(request):
    if(request.method=='POST'):
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you, You are registered now")
    else:
        form= Register()
    return render(request, 'Register.html',{'form':form})