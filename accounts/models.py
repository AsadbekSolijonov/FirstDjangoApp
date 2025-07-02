from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='account_img/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s image"
