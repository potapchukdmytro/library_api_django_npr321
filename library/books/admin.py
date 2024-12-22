from django.contrib import admin
from .models import Address, Author, Book

# Register your models here.
admin.site.register(Address)
admin.site.register(Author)
admin.site.register(Book)