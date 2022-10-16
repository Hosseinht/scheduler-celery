from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'User Profiles'
        ordering = ["id"]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
