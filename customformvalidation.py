class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=18)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if 'admin' in username.lower():
            raise ValidationError("Username can't contain 'admin'")
        return username + '_processed'  # Modifying the value
