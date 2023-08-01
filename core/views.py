from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CarStore
from .models import FeaturedCars
from core.forms import UserForm
from core.models import UserInfo
from core.forms import ContactForm
from core.models import ContactInfo
from django.contrib.auth.mixins import LoginRequiredMixin
import requests

def home(request):
    logout(request)
    messages.success(request, 'You have just Signed out, come back soon...')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def cars(request):
    carStore = CarStore.objects.all()
    return render(request, 'cars.html', {"carStore": carStore})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('success')
            except:
                pass
    else:
        form = UserForm()
    return render(request, 'contact.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return redirect("login")
        
    return render(request, 'login.html')

    

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Form submitted successfully')
                return redirect('login')
            except:
                pass
    else:
        form = UserForm()
    return render(request, 'register.html')

def success(request):
    return render(request, 'success.html')

def single(request):
    featuredcars = FeaturedCars.objects.all()
    return render(request, 'single.html')

def dashboard(request):
    url = "https://newsapi.org/v2/everything?q=technology&from=2023-07-28&sortBy=popularity&apiKey=a7418d607fd04777848fe513b3052054"
    
    cars_news = requests.get(url).json()

    a = cars_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    mylist = zip(title, desc, img)
    context = {'mylist':mylist}


    return render(request, 'dashboard.html', context)
