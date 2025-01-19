from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', { 'books': books } )

def book_page(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'books/book_page.html', { 'book': book })

@login_required(login_url="/users/login")
def book_new(request):
    if request.method == "POST":
        form = forms.CreateBook(request.POST, request.FILES)
        if form.is_valid():
            newbook = form.save(commit=False)
            newbook.user = request.user
            newbook.save()
            return redirect("books:list")
    else:
        form = forms.CreateBook()
    return render(request, 'books/book_new.html', { 'form': form })