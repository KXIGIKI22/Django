#from django.http import HttpResponse

#def my_users_view(request):
#    return HttpResponse("Hello, users!")

#def users_view(request):
#    return HttpResponse("Hello, admin users!")
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import User, Purchase, Book
from .serializers import UserSerializer, PurchaseSerializer, BookSerializer

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