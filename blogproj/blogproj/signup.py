from django import forms
from django.contrib.auth.models import User

class SignUp(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password']