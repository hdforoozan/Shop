from django.db import models
from django.urls import reverse
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
    	return self.name

    def get_absolute_url(self):
        return reverse('bookstore:author-detail', args=[str(self.id)])

class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
    	return self.name

    def get_absolute_url(self):
        return reverse('bookstore:publisher-detail', args=[str(self.id)])

class Book(models.Model):
    name = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2 ,blank=True , null=True)
    translator = models.CharField(max_length = 100 , blank = True)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField(blank=True , null=True)

    def __str__(self):
    	return self.name

    def get_absolute_url(self):
        return reverse('bookstore:book-detail', args=[str(self.id)])
