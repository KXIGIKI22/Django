from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
#from .models import User, Purchase, Book
from .serializers import UserSerializer, PurchaseSerializer, BookSerializer
from myapp.tasks import print_text, print_purchase_count
from myapp.serializers import UserSerializer, PurchaseSerializer, BookSerializer

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PurchaseListView(ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseDetailView(RetrieveAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):

        print_text.delay("Hello, Celery!")

        user_id = 1
        print_purchase_count.delay(user_id)

        return super().get(request, *args, **kwargs)