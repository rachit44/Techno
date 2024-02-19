from django.shortcuts import render, redirect
from django.http import HttpResponse
from Techno.forms import *
from django.core.exceptions import ValidationError
from TechnoCoder.models import *
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login, authenticate
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
            
# Create your views here.
def login_page(request):
    if(request.method=='POST'):
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('/login/')
            user_obj = authenticate(username = username, password=password)

            if user_obj:
                login(request, user_obj)
                return redirect(reverse("home") + f'?{request.user.id}')
             
            messages.error(request, "Wrong Password")
            return redirect('/login/')
    else:
        form= Login()
    return render(request, 'login.html',{'form':form,'request':request})

def register(request):
    if(request.method=='POST'):
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you, You are registered now")
    else:
        form= Register()
    return render(request, 'Register.html',{'form':form})

def home(request):
    certificates = {'CompTIA A+', 'CompTIA Network+', 'Cisco Certified Network Associate (CCNA)', 'Cisco Certified Network Professional (CCNP)',
                'Certified Information Systems Security Professional (CISSP)', 'Certified ScrumMaster (CSM)',
                'Certified Data Professional (CDP)','Red Hat Certified Engineer (RHCE)','AWS Certified Developer – Associate',
                'Microsoft Certified: Azure Developer Associate','Google Associate Cloud Engineer','Microsoft Certified: Azure AI Engineer Associate',
                'IBM Data Science Professional Certificate'}
    return render(request,'index.html',{'certificates':certificates})

def home_logged_in(request, username):
    return HttpResponse("heijj")

@receiver(user_logged_in)
def log_user_login(sender, user, request, **kwargs):
    LoginActivity.objects.create(user=user)

def calculate_login_streak(user):
    today = timezone.now().date()
    streak = 0
    current_date = today
    max_streak = 0

    while LoginActivity.objects.filter(user=user, login_date=current_date).exists():
        streak += 1
        current_date -= timedelta(days=1)

    return streak
