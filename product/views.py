from django.shortcuts import render
from django.views.generic import TemplateView


class ProductView(TemplateView):
    template_name = 'grid.html'


class ProductDetailView(TemplateView):
    template_name = 'product_detail.html'