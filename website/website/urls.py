from django.contrib import admin
from django.urls import path

from todo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home , name = "home"),
    path('signup/' , sign_up , name = "sign_up"),
    path('login/' , login , name = "login" ),
]
