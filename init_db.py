import os
import django
from django.core.management import call_command
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kindom.settings')
django.setup()

def create_visitor_account():
    User = get_user_model()
    
    # Créer le compte visiteur s'il n'existe pas
    visitor, created = User.objects.get_or_create(
        email='visitor@kindom.com',
        defaults={
            'username': 'visitor',
            'first_name': 'Visiteur',
            'last_name': 'Kindom',
            'is_active': True,
            'is_staff': False,
            'is_superuser': False
        }
    )
    
    if created:
        visitor.set_password('visitor123')
        visitor.save()
        print("Compte visiteur créé avec succès!")
        print("Email: visitor@kindom.com")
        print("Mot de passe: visitor123")
    else:
        print("Le compte visiteur existe déjà.")

def init_db():
    # Appliquer toutes les migrations
    call_command('migrate')
    
    # Créer le site par défaut
    from django.contrib.sites.models import Site
    Site.objects.get_or_create(
        id=1,
        defaults={
            'domain': '127.0.0.1:8000',
            'name': 'Kindom'
        }
    )
    
    # Créer le compte visiteur
    create_visitor_account()
    
    print("Base de données initialisée avec succès!")

if __name__ == '__main__':
    init_db() 