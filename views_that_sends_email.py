from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from .forms import UserRegistrationForm

def register(request):
    # Handle user registration form
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            # Send a welcome email to the user
            subject = 'Welcome to our site'
            message = f'Hi {user.username}, thank you for joining us.'
            from_email = 'admin@oursite.com'
            to_email = [user.email]
            send_mail(subject, message, from_email, to_email)
            # Redirect to the home page
            return redirect('home')
    else:
        form = UserRegistrationForm()
    # Render the registration template
    return render(request, 'registration/register.html', {'form': form})
