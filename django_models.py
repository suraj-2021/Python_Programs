from django import forms  
from django.contrib.auth.models import User

class LoginForm(forms.Form):
      username = forms.CharField()
      password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
      password = forms.CharField(max_length=100,label='password',widget=forms.PasswordInput)
      password2 = forms.CharField(label='Repeat Password',max_length=100,widget=forms.PasswordInput)

      class Meta:
            model = User
            fields = ['first_name','username','email']

      def clean_password(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                  raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']
