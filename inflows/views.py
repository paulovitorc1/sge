from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms


class InflowListView(LoginRequiredMixin, ListView):
    model = models.Inflows
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('id')
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset
    
class InflowCreateView(LoginRequiredMixin, CreateView):
    model = models.Inflows
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')

class InflowDetailView(LoginRequiredMixin, DetailView):
    model = models.Inflows
    template_name = 'inflow_detail.html'
