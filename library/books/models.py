from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    country = models.CharField(max_length=75)
    city = models.CharField(max_length=75)
    street = models.CharField(max_length=75)
    house = models.IntegerField()

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateTimeField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    image = models.ImageField(blank=True, default='book_default.jpg')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)