from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class CreateBookView(CreateView):
    model = Book
    template_name = 'create_book.html'
    fields = ['title', 'author', 'genre', 'published_date', 'description']