from django.shortcuts import render , redirect , get_object_or_404

# importing logic from forms
from .forms import *

# for login stuff
from django.contrib.auth import authenticate, login as login_auth
from django.contrib.auth.decorators import login_required


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


@login_required(login_url="login")
def todo(request):
    todo_item = TodoObject.objects.filter(user = request.user)
    return render(request , "todo.html" , context={'todos': todo_item})

@login_required(login_url="login")
def create_todo(request):
    if request.method == "POST":
        form = TodoObjectForm(request.POST)
        
        # saves the form but not commit and then after commit it would save it
        if form.is_valid:
            saved_form = form.save(commit=False)
            saved_form.user = request.user
            saved_form.save()
            return redirect("todo")
    else:
        form = TodoObjectForm()
    
    return render(request , "create_todo.html" , context = {'create_todo': form})

@login_required
def edit_todo(request , id):
    instance = get_object_or_404(TodoObject , id = id)
    form = TodoObjectForm(instance = instance)
    
    if request.method == "POST":
        
        form = TodoObjectForm(request.POST)
        if form.is_valid:
            form_object = TodoObject.objects.get(id = id)
            form_object.user = request.user
            form_object.text = request.POST.get("text")
            if request.POST.get("is_checked") == "on":
                form_object.is_checked = True
            else:
                form_object.is_checked = False
            form_object.save()
            return redirect("todo")
        
        
    
    return render(request , "edit_todo.html" , context= {'edit_todo':form})

@login_required
def delete_todo(request , id):
    todo_item = TodoObject.objects.get(id = id)
    
    if request.method == "POST":
        todo_item.delete()
        return redirect("todo")
            
    return render(request , "delete_todo.html" , context= {"todo": todo_item})