from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms 




# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})
    
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged In. "))
            return redirect('home')
        else:
            messages.success(request, ("Error. Please Try again. "))
            return redirect('login')
    
    else:
        return render(request, 'login.html', {})

def logout_user(request):
   logout(request)
   messages.success(request, ("You have been logged out...."))
   return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user
            user = authenticate(username=username, password=password )
            login(request, user)
            messages.success(request, ("You have registered successfully...."))
            return redirect('home')
        else:
            messages.success(request, ("whoops!there is a problem...."))
            return redirect('register')
        
    else:       
        return render(request, 'register.html', {'form':form})