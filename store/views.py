from django.shortcuts import get_object_or_404, render
from . models import Category, Product

# Create your views here.


def products_all(request):
    products = Product.products.all()
    return render(request, 'store/index.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True, is_active=True)
    return render(request, "store/detail_product.html", {'product': product})


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.products.filter(category=category)

    context = {'category': category, 'products': products}
    return render(request, 'store/category.html', context)
