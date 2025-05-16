from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):
    password = None  # On ne veut pas afficher le champ mot de passe
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', 
                 'address', 'profile_picture', 'bio')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 3}),
        } 