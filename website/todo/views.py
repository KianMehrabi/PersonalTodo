from django.shortcuts import render , redirect

# importing logic from forms
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login

def home(request):
    
    return render(request , "home.html")

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect("hello_world/")
    else:
        form = UserCreationForm()
    return render(request , "signup.html" , context = {'sign_up_form': UserCreationForm} )