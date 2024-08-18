from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput , TextInput

# importing all the models
from .models import TodoObject

class CreateUserForm(UserCreationForm):
    
    class Meta:
        models = User
        fields = ['username' , 'email' ,  'password1' , 'password2'] 
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
class TodoObjectForm(forms.ModelForm):
    class Meta:
        model = TodoObject
        fields = ["user" , "text" , "is_checked"]