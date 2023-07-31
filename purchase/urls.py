from django.urls import path
from .views import PurchaseListView, PurchaseDetailView, CreatePurchaseView

urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase_list'),
    path('<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('create/', CreatePurchaseView.as_view(), name='purchase_create'),
]