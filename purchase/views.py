from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Purchase

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'purchase_list.html'
    context_object_name = 'purchases'

class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'purchase_detail.html'
    context_object_name = 'purchase'

class CreatePurchaseView(CreateView):
    model = Purchase
    template_name = 'create_purchase.html'
    fields = ['user', 'book', 'purchase_date', 'price']