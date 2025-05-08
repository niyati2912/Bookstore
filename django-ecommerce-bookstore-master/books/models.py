from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200) 
    description = models.TextField(max_length=500, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=2083, blank=True)
    follow_author = models.URLField(max_length=2083, blank=True)
    book_available = models.BooleanField(default=False)
    genres = models.ManyToManyField(Genre, related_name='books')

    def __str__(self):
        return self.title

class Order(models.Model):
    product = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.title) if self.product else 'No product'
