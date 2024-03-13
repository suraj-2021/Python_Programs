from django.shortcuts import render
from django.contrib.auth.decorators import loging_required 
from django.shortcuts import redirect
from django.contrib.auth import login
from .forms import RegistrationForm, LoginForm

def register(request):
    if request.method == "POST":
       form = RegistrationForm(request.POST)
       if form.is_valid():
           user = form.save()
           login(request,user)
           return redirect('home')

    else:
        form = RegistrationForm()
        return render (request,'music_player/register.html',{'form': form}) 

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
