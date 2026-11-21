from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def home(request):
    products = Product.objects.filter(is_active=True).select_related('category')
    categories = Category.objects.all()

    q = request.GET.get('q', '').strip()
    category_slug = request.GET.get('category', '')

    if q:
        products = products.filter(name__icontains=q)
    if category_slug:
        products = products.filter(category__slug=category_slug)

    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories,
        'q': q,
        'active_category': category_slug,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'store/product_detail.html', {'product': product})
