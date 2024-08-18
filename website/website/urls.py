from django.contrib import admin
from django.urls import path

from todo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home , name = "home"),
    path('signup/' , sign_up , name = "sign_up"),
    path('login/' , login , name = "login" ),
    path('todo/' , todo , name = "todo" ),
    
    # crud
    
    path('create_todo/' , create_todo , name = "create_todo" ),
    path('create_todo/' , edit_todo , name = "edit_todo" ),
    path('delete_todo/' , delete_todo , name = "delete_todo" ),
    path('delete_all_todo/' , delete_all_todo , name = "delete_all_todo" ),
]
