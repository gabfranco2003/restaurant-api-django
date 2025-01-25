from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('delivery_crew', 'Delivery Crew'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='customer')

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Custom related_name to avoid conflicts
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Custom related_name to avoid conflicts
        blank=True,
    )
