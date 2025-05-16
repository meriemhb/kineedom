from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Order, OrderItem, Review

def product_list(request):
    """Vue pour lister les produits"""
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    """Vue pour afficher les détails d'un produit"""
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    return render(request, 'shop/product_detail.html', {
        'product': product,
        'reviews': reviews
    })

@login_required
def cart_detail(request):
    """Vue pour afficher le panier"""
    return render(request, 'shop/cart_detail.html')

@login_required
def cart_add(request, product_id):
    """Vue pour ajouter un produit au panier"""
    product = get_object_or_404(Product, id=product_id)
    # Logique d'ajout au panier
    messages.success(request, f'{product.name} a été ajouté au panier.')
    return redirect('shop:cart_detail')

@login_required
def cart_remove(request, product_id):
    """Vue pour retirer un produit du panier"""
    product = get_object_or_404(Product, id=product_id)
    # Logique de suppression du panier
    messages.success(request, f'{product.name} a été retiré du panier.')
    return redirect('shop:cart_detail')

@login_required
def checkout(request):
    """Vue pour le processus de paiement"""
    if request.method == 'POST':
        # Logique de paiement
        pass
    return render(request, 'shop/checkout.html')

@login_required
def order_list(request):
    """Vue pour lister les commandes"""
    if request.user.user_type in ['patient', 'kine']:
        orders = Order.objects.filter(customer=request.user)
    else:
        orders = Order.objects.all()
    return render(request, 'shop/order_list.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    """Vue pour afficher les détails d'une commande"""
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'shop/order_detail.html', {'order': order}) 