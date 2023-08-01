from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('cars', views.cars, name='cars'),
    path('contact', views.contact, name='contact'),
    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),
    path('success', views.success, name='success'),
    path('single', views.single, name='single'),
    path('dashboard', views.dashboard, name='dashboard')
]