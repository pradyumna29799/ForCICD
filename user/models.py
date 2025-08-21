from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class Role(models.Model):
    role_name = models.CharField(max_length=255)
    access = models.TextField()
    
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(null=True,blank=True)
    phone_no = models.CharField(unique=True,max_length=10)
    role  = models.ForeignKey('Role',on_delete=models.CASCADE) 
    
    USERNAME_FIELD = 'phone_no'

class Document(models.Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    title = models.CharField(max_length=255,blank=True,null=True)
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
