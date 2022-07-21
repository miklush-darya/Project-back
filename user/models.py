from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

from core.models import BaseModel


class User(AbstractUser, BaseModel):
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        null=True,
        blank=True,
    )

    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Shop(BaseModel):

    name_shop = models.CharField(max_length=255)
    unp = models.IntegerField()

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="shops")

    def __str__(self):
        return self.name_shop