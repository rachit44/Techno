from django.shortcuts import render, redirect
from django.http import HttpResponse
from Techno.forms import *
from django.core.exceptions import ValidationError
from TechnoCoder.models import *
from django.contrib.auth import login, authenticate
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required
            
# Create your views here.
def login_page(request):
    if(request.method=='POST'):
        username_or_email  = request.POST.get('username_or_email')
        password = request.POST.get('password')
        
        if '@' in username_or_email:
            user_obj = User.objects.filter(email=username_or_emails)
        else:
            user_obj = User.objects.filter(username=username_or_emails)
        
        if not user_obj.exists():
            error_message = "Username or Password is incorrect or doesn't exists"
            return render(request, 'login.html', {'error_message': error_message})
        
        if '@' in username_or_email:
            # Attempt to authenticate using email
            user_obj = authenticate(email = username_or_emails, password=password)
        else:
            # Attempt to authenticate using username
            user_obj = authenticate(username = username_or_emails, password=password)

        if user_obj:
            login(request, user_obj)
            return redirect('home' + f'?{request.user.username}')
             
        error_message = "Wrong Password"
        return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def register(request):
    if(request.method=='POST'):
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you, You are registered now")
    else:
        form= Register()
    return render(request, 'register.html',{'form':form})

@login_required
def home(request, **kwargs):
    certificates = {'CompTIA A+', 'CompTIA Network+', 'Cisco Certified Network Associate (CCNA)', 'Cisco Certified Network Professional (CCNP)',
                'Certified Information Systems Security Professional (CISSP)', 'Certified ScrumMaster (CSM)',
                'Certified Data Professional (CDP)','Red Hat Certified Engineer (RHCE)','AWS Certified Developer – Associate',
                'Microsoft Certified: Azure Developer Associate','Google Associate Cloud Engineer','Microsoft Certified: Azure AI Engineer Associate',
                'IBM Data Science Professional Certificate'}
    if request.method =='GET':
        userProfile = UserProfile.objects.get(user=request.user)
        if userProfile.course == UserProfile._meta.get_field('course').get_default():
            pass
    return render(request,'index.html',{'certificates':certificates})

def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserForm(instance=profile)
    return render(request, 'profile.html', {'form': form})


def password_reset(request):
    return render(request,'forgot-password.html',{'template':'password_reset.html'})


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
