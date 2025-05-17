from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from allauth.account.views import LoginView
from .models import CustomUser
from .forms import CustomUserChangeForm

def home(request):
    """Vue pour la page d'accueil"""
    return render(request, 'accounts/home.html')

@login_required
def profile(request):
    """Vue pour afficher le profil de l'utilisateur"""
    return render(request, 'accounts/profile.html')

@login_required
def edit_profile(request):
    """Vue pour modifier le profil de l'utilisateur"""
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre profil a été mis à jour avec succès.')
            return redirect('accounts:profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    """Vue pour supprimer le profil de l'utilisateur"""
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Votre compte a été supprimé avec succès.')
        return redirect('home')
    return render(request, 'accounts/delete_profile.html')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        user_type = self.request.POST.get('user_type', 'visitor')
        user = form.user
        
        if user.user_type != user_type:
            messages.error(self.request, f"Ce compte n'est pas un compte {user_type}.")
            return self.form_invalid(form)
            
        return super().form_valid(form) 