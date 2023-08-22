from django.urls import path
from .views import BookListView, BookDetailView, CreateBookView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', CreateBookView.as_view(), name='book_create'),
]