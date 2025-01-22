
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from urllib import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from . import models, forms
from app import metrics
from brands.models import Brand
from categories.models import Category


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Products
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    permission_required = 'products.view_products'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('id')
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)
        if category:
            queryset = queryset.filter(category__id=category)
        if brand:
            queryset = queryset.filter(brand__id=brand)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_metrics'] = metrics.get_product_metrics()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        return context
    
class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Products
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.add_products'

class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Products
    template_name = 'product_detail.html'
    permission_required = 'products.view_products'

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Products
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.change_products'

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Products
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_products'