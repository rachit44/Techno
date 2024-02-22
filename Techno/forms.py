from django import forms
from TechnoCoder.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import as_serializer_error
    
class Register(forms.Form):
    email = forms.EmailField()
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2']

    def clean(self):
        cleaned_data = super().clean()
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use. Please use a different email.")
        elif "@persistent.com" in email:
            return email
        else:
            raise ValidationError("Only Persistent Systems user allowed")

class UserForm(forms.Form):
    class Meta:
        model = UserProfile
        fields = ['user','profile picture','course','progress']