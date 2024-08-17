from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class TodoObject(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    text = models.CharField(max_length = 100)
    is_checked = models.BooleanField()
    
    def __str__(self):
        return self.text