from django import forms
from .models import tweet 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class tweetform(forms.ModelForm):
    class Meta:
        model = tweet
        fields = ['id','text', 'photo' ]

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta :
        model = User
        fields = ('username','email','password1','password2')

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
