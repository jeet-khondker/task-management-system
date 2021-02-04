from django.db import models

from django.contrib.auth.models import AbstractBaseUser

from .managers import UserAccountManager

# Custom User Account Model
class UserAccount(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email Address", max_length=60, unique=True)
    full_name = models.CharField(verbose_name="Full Name", max_length=30)
    date_joined = models.DateTimeField(verbose_name="Member Since", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Logged In", auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name",] #Required fields other than 'email'

    objects = UserAccountManager()

    # String Representation of User Account Model
    def __str__(self):
        return self.full_name

    # For checking Permissions
    # All Admin Users have ALL Permissions
    def has_perm(self, perm, object=None):
        return self.is_admin

    # Does this user has permission to use this application?
    # Always YES for Simplicity
    def has_module_perms(self, app_label):
        return True