from tkinter import E
from django.shortcuts import get_object_or_404, render

from .models import Product
from category.models import Category

# Create your views here.
def store(request, category_slug=None):
    # iniciazamos las variables
    categories = None
    products= None
    # verificamos
    if category_slug != None:
        # obtenemos las categorias donde su slug sea category_slug
        categories = get_object_or_404(Category, slug=category_slug)
        # ahora obtenemos las productos que tengan esas categorias
        products = Product.objects.filter(category=categories, is_available=True)
        # por ultimo obtenemos la cuenta de productos
        products_count = products.count()
    else:
        # obtenemos todos los productos
        products = Product.objects.all().filter(is_available= True)
        # y la cuenta de productos
        products_count = products.count()
    
    context = {
        'products': products,
        'products_count': products_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug= category_slug, slug= product_slug)
    except Exception as e:
        raise E
    
    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html',context)