from django.shortcuts import render
from .models import Book

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', { 'books': books } )

def book_page(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'books/book_page.html', { 'book': book })