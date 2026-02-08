from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email' # 👈 critical 
    REQUIRED_FIELDS = ['username'] # still collect username, but email is the login field 

  
    class Meta:
        db_table = 'auth_user'  # Use the default auth_user table


