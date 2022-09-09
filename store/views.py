from django.shortcuts import get_object_or_404, render
from elasticsearch_dsl import Q

from .documents import ProductDocument
from .models import Category, Product

# Create your views here.


def products_all(request):
    # products = Product.objects.all()
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "store/index.html", {"products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "store/detail_product.html", {"product": product})


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    # products = Product.objects.filter(category__in=Category.objects.get(name=slug).get_descendants(include_self=True))
    products = Product.objects.filter(category=category)

    context = {"category": category, "products": products}
    return render(request, "store/category.html", context)


def search_view(request):
    q = request.GET.get("q")
    # q = Q("multi_match", query=q, fields=["title"])
    q = Q("match", title=q) | Q("match", category__name=q)
    if q:
        # products = ProductDocument.search().query("match", category__name=q)
        products = ProductDocument.search().query(q)
    else:
        products = None

    return render(request, "store/search_result.html", {"products": products})
