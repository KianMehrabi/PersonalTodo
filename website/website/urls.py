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
    path('edit_todo/<int:id>' , edit_todo , name = "edit_todo" ),
    path('delete_todo/<int:id>' , delete_todo , name = "delete_todo" ),
]
