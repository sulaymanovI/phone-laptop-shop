from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomUserManager

class User(AbstractBaseUser,PermissionsMixin):

    class Type(models.IntegerChoices):
        CUSTOMER=1
        SELLER=2
    
    fullname=models.CharField(max_length=255, verbose_name="Ism Familiyasi")
    email = models.EmailField(max_length=155, unique=True , verbose_name="Email")
    user_type=models.IntegerField(choices=Type.choices, default=1,verbose_name="User turi")
    created_at = models.DateTimeField(auto_now_add=True , verbose_name="Yaratilgan vaqti")
    updated_at=models.DateTimeField(auto_now=True , verbose_name="Yangilangan vaqti")
    is_staff = models.BooleanField(default=False , verbose_name="Staff")
    is_superuser=models.BooleanField(default=False , verbose_name="Superuser")
    is_active = models.BooleanField(default=True , verbose_name="Aktivligi")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
