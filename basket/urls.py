from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
    path('addBasket/', views.basket_add, name='basket_add'),
    path('deleteBasket/', views.basket_delete, name='basket_delete'),
    path('updateBasket/', views.basket_update, name='basket_update')



]
