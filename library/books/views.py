from django.shortcuts import render

# Create your views here.
def books_list(request):
    return render(request, 'books/books_list.html')