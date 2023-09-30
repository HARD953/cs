from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin, AbstractBaseUser,BaseUserManager
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from distutils.command.upload import upload

from django.conf import settings

# Create your models here.

class CustumerAccountManager(BaseUserManager):
    def create_user(self, email, user_name,first_name,password, **other_fields):
        if not email:
            raise ValueError("you must provide a email address")
        email=self.normalize_email(email)
        user=self.model(email=email,user_name=user_name,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name,first_name, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email, user_name,first_name,**other_fields)

class NewUser(AbstractBaseUser,PermissionsMixin):
    def nameFile(instance, filename):
        return '/'.join(['images', str(instance.user_name), filename])
    user_name=models.CharField(max_length=30,unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30,default="issa")
    start_date=models.DateTimeField(default=timezone.now)
    email=models.EmailField(max_length=255,unique=True)
    adresse=models.CharField(max_length=300, blank=True, null=True)
    create=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image=models.ImageField(upload_to=nameFile,blank=True,default="issa")
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    is_user=models.BooleanField(default=True)
    last_login = models.DateTimeField(('last_login'), default=timezone.now())
    responsable=models.CharField(max_length=30,default="issa")
    district=models.CharField(max_length=100,blank=True)
    region=models.CharField(max_length=100,blank=True)
    departement=models.CharField(max_length=100,blank=True)
    sous_prefecture=models.CharField(max_length=100,blank=True)
    commune=models.CharField(max_length=100,blank=True)

    objects=CustumerAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['user_name','first_name']
    def __str__(self):
        return self.email









    
