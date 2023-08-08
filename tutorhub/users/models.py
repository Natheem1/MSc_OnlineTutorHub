from typing import Optional
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# CustomUserManager handles the creation and management of custom user accounts.
class CustomUserManager(BaseUserManager):

    # Create a superuser with necessary attributes and permissions.
    def create_superuser(self, email, username, first_name, password, **other_fields):

        # Set default values for is_staff, is_superuser, and is_active.
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        # Ensure the superuser is assigned to is_staff = True.
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'SuperUser Must Be Assigned to is_staff = True'
            )
        # Ensure the superuser is assigned to is_superuser = True.
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'SuperUser Must Be Assigned to is_superuser = True'
            )
        # Create and return the superuser.
        return self.create_user(email, username, first_name, password, **other_fields)
    
    # Create a regular user with required attributes.
    def create_user(self, email, username, first_name, password, **other_fields):
        
        # Check if an email address is provided.
        if not email:
            raise ValueError (("You MUST Provide An Email Address"))
        
        # Normalize the email address and create the user.
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    # Retrieve a user by their natural key (email).
    def get_by_natural_key(self, email):
        return self.get(email=email)


# NewUser represents a custom user model extending AbstractBaseUser and PermissionsMixin.
class NewUser(AbstractBaseUser,PermissionsMixin):

    #User attributes/fields
    email = models.EmailField(("email address"), unique=True)
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=True)

    # User type choices: admin, student, tutor.
    USER_TYPE_CHOICES = (
    ('admin', 'Admin'),
    ('student', 'Student'),
    ('tutor', 'Tutor'),
    )
    user_type = models.CharField(max_length=15, choices=USER_TYPE_CHOICES)

    # More user attributes/fields
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    # Define the email field as the username field for authentication.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    # String representation of the user (their username).
    def __str__(self):
        return self.username