from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        SUPERADMIN = 'SUPERADMIN', "Owner of this platform"
        ADMIN = 'ADMIN', "Administrator"
        STUDENT = 'STUDENT', "Student"
        USER = 'USER', "User"

    role = models.CharField(
        max_length=20,
        choices=Role,
        default=Role.USER,
        verbose_name="Role"
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]