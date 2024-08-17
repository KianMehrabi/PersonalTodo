from django.shortcuts import render , redirect

# importing logic from forms
from .forms import *

# for login stuff
from django.contrib.auth import authenticate, login as login_auth

# importing all the models classes
from .models import *

def home(request):
    
    return render(request , "home.html")

def sign_up(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login_auth(request, new_user)
            return redirect("home")
    return render(request , "signup.html" , context = {'sign_up_form': UserCreationForm} )

def login(request):
    form = LoginForm() 
    if request.method == "POST":
        form = LoginForm(request , data = request.POST)
        
        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password') 
            user = authenticate(request , username = username , password = password)
            
            if user is not None:
                login_auth(request , user)
                
                return redirect("home")
    return render(request , "login.html" , context = {'login_form': LoginForm} )

def todo(request):
    return render(request , "todo.html" , context={'todo': TodoObject})