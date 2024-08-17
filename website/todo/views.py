from django.shortcuts import render

# importing logic from forms
from .forms import UserCreationForm

def home(request):
    context = {
        'sign_up_form': UserCreationForm
    }
    return render(request , "home.html" , context = context)
