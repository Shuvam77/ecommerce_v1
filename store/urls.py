from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.products_all, name='products_all'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:slug>/', views.category_list, name='category_list'),
]
