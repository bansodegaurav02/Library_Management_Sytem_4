from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Book(models.Model):
    
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
    page=models.CharField(max_length=100)
    quantity = models.IntegerField(default=30)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_issued = models.DateField(auto_now_add=True)

    fee_charged = models.DecimalField(max_digits=10, decimal_places=2, default=0)



