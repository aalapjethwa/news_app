from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

from fetch_news.models import Category


class User(AbstractUser):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(
        Category, blank=True, related_name="user"
    )
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$", message="Not a valid phone number"
    )
    phone = models.CharField(validators=[phone_regex], max_length=250, default="")
    last_updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AppUser(User):
    class Meta:
        proxy = True
        verbose_name = "App User"
        verbose_name_plural = "App Users"

    def save(self, *args, **kwargs):
        self.is_staff = True
        return super().save(*args, **kwargs)
