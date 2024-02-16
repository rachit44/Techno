from django import forms
from TechnoCoder.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Login(forms.Form):
    user_name = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput(),max_length=14,min_length=10)
    
class Register(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please use a different email.")
        elif "@persistent.com" in email:
            return email
        else:
            raise ValidationError("Only Persistent Systems user allowed")