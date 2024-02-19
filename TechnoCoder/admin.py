from django.contrib import admin
from TechnoCoder.models import *
# Register your models here.
#class App(admin.ModelAdmin):

admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Questions)
admin.site.register(Choice)