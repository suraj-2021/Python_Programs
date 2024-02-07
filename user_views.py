from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import CustomUserCreationForm


def home(request):
    return render (request,'home.html',{})


def signup(request):
    if request.method == 'POST':
       form = CustomUserCreationForm(request.POST)
       if form.is_valid():
           form.save
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username = username, password = password)
           login(request,user)
           return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render (request,'signup.html',{'form':form})

