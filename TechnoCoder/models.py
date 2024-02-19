from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import uuid
from django.utils import timezone
from django.utils.crypto import get_random_string

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
     
    class Meta:
        abstract = True

class LoginActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_date = models.DateField(auto_now_add=True)

class Course(BaseModel):
    CHOICES = (('level1','Beginner'),
                ('level2','Intermediate'),
                ('level3','Practitioner'),
                ('level4','Expert'))
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_images/')
    proficiency = models.CharField(max_length=20, choices=CHOICES,default='level1')
    category= models.CharField(max_length=50,default='Cloud')

class UserProfile(BaseModel):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    enrolled_on = models.DateField(default=timezone.now)
    progress = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')

class Questions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=200,default='')

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=100,default='')
    is_correct = models.BooleanField(default=False)