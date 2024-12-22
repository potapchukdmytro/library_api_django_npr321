from django.db import models

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

class Book(models.Model):
    title = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')