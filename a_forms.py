from django import forms
from django.contrib.auth.models import User
from modelapp.models import UserProfileInfo

class UserForm(forms.ModelForm):
      password = forms.CharField(widget = forms.PasswordInput())
      portfolio = forms.URLField(required = False)
      picture = forms.ImageField(required = False)
      class Meta():
            model = User
            
            
