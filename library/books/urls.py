from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path('', views.books_list, name="list"),
    path('<int:id>', views.book_page, name="page")
]