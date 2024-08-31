from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.contrib import messages

def user_list(request):
    users = User.objects.exclude(id = request.user.id)
    return render(request,'chatapp/user_list.html',{"users":users})


def user_registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect(reverse('chatapp:user_list'))
        else:
            messages.error(request, "Input is Incorrect, Please Try Again")
            return render(request, 'chatapp/user_registration.html', {"form": form})
    else:
        form = UserRegistrationForm()
        return render(request, 'chatapp/user_registration.html', {"form": form})
            
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect(reverse('chatapp:user_list'))
        else:
            messages.error(request,"Incorrect details, Try Again")
            return redirect(reverse("chatapp:user_login"))
    else:
        return render(request,'chatapp/user_login.html')
