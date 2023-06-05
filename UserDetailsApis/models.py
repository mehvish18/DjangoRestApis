from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phone_number']


class UserDetail(models.Model):
    age = models.IntegerField()
    dob = models.DateField()
    profession = models.CharField(max_length=150)
    address = models.CharField(max_length=500)
    hobby = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, blank=True)

    def __str__(self):
        return self.user.first_name
