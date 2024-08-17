from django.shortcuts import render , redirect

# importing logic from forms
from .forms import *

# for login stuff
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
            return redirect("home")
    else:
        form = UserCreationForm()
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
                login(request , user)
                
                return redirect("home")
    context = {'login_form': LoginForm}
    return render(request , "login.html" , context = context )