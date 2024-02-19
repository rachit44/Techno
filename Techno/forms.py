from django import forms
from TechnoCoder.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import as_serializer_error

class Login(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput(),max_length=14,min_length=10)
    
class Register(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(as_serializer_error("This email is already in use. Please use a different email."))
        elif "@persistent.com" in email:
            return email
        else:
            raise ValidationError("Only Persistent Systems user allowed")

class UserForm(forms.Form):
    class Meta:
        model = UserProfile
        fields = ['user','course','progress','status']