from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('visitor', 'Visiteur'),
        ('patient', 'Patient'),
        ('kine', 'Kinésithérapeute'),
        ('vendor', 'Vendeur'),
        ('admin', 'Administrateur'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='visitor')
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.email} ({self.get_user_type_display()})" 