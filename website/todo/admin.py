from django.contrib import admin

# importing my models
from .models import TodoObject

admin.site.register(TodoObject)