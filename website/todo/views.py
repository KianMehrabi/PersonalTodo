from django.shortcuts import render

# importing logic from forms
from .forms import UserCreationForm

def home(request):
    
    return render(request , "home.html")

def sign_up(request):
    context = {
        'sign_up_form': UserCreationForm
    }
    return render(request , "signup.html" , context = context)