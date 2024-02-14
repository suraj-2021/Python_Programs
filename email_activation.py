from django.contrib.auth import login, activate
from django.shortcuts import render, redirect

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.is_valid(user, token):
        user.is_active = True
        user.save()
        login(request, user)
