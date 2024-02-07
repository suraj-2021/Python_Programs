from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
      first_name= forms.CharField(max_length = 30, required = True, help_text = "Required. Enter your First Name")
      last_name= forms.CharField(max_length = 30, required = True, help_text = "Required. Enter your last Name")

      class Meta:
            model = User
            fields = [
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
            ]
