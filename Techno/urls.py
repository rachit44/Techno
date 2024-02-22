"""
URL configuration for Techno project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from TechnoCoder import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/',views.profile,name='profile'),
    path('login/', views.login_page,name = 'login'),
    path('register/', views.register, name='register'),
    path('home/<str:username>',views.home, name='home'),
    path('streaks/',views.calculate_login_streak, name='streak'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('importCSV',views.importCSV),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
