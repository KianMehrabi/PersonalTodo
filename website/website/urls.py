from django.contrib import admin
from django.urls import path

from todo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home),
    path('signup/' , sign_up),
    path('login/' , login),
]
