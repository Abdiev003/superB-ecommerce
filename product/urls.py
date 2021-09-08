from django.urls import path

from product.views import (
    ProductView,
    ProductDetailView,
)

app_name = 'product'

urlpatterns = [
    path('<slug:slug>', ProductView.as_view(), name='product-list'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product-detail'),
]
