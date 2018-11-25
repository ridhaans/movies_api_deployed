from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class MovieManager():
    """django can create movie from the movie model"""
    
    def create_movie(self,title,duration,year,director,writer):
        
        if not title:
             raise ValueError('Movie must have a title')
                
        movie=self.model(title=title,duration=duration,year=year,director=director,writer=writer)        
        movie.save(using=self.db)

        return movie

class Movie(models.Model):
    """Represents a movie"""""
    
    #use user id as a foreignkey and when the user is deleted, the movie goes with it.
    user_profile=models.ForeignKey('UserProfile', on_delete=models.CASCADE)

    #attribute/columns and rules definition, title is required and must be unique,etc
    title=models.CharField(max_length=255, unique=True)
    duration=models.DurationField("Duration (minutes)")    
    year=models.IntegerField()
    director=models.CharField(max_length=255)
    writer=models.CharField(max_length=255)
    REQUIRED_FIELDS=['title']

    objects=MovieManager()
    
    def __str__(self):
        return self.title


class UserProfileManager(BaseUserManager):
    """django can create user and superuser from userprofile model """

    def create_user(self,email,name,password=None):
        
        if not email:
             raise ValueError('Users must have an email address')
        
        email=self.normalize_email(email) #to normalize upper or lower case
        user=self.model(email=email,name=name)

        user.set_password(password) #turns the password into hash
        user.save(using=self._db)

        return user
    def create_superuser(self,email,name,password):
        
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return self


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Represents user, 
    AbstractBaseUser is django's pre-defined user model (can be customized by overriding),
    PermissionsMixin allows to add permission to user model"""

    #attribute/columns and rules definition, email and name are required, email must be unique,etc
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    objects = UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_name(self):
        
        return self.name
    
    def __str__(self):
        return self.email
    