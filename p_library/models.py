from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.utils.deconstruct import deconstructible
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


# @deconstructible
class Reader(models.Model):
    full_name = models.TextField()
    phone_number = PhoneNumberField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    short_name = models.CharField(max_length=254)
    full_name = models.TextField()
    phone_number = PhoneNumberField(null=True, blank=True)
    country = models.CharField(max_length=2)
    site = models.URLField()

    def __str__(self):
        return self.short_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, null=True, blank=True)
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    readers = models.ManyToManyField(Reader, null=True, blank=True, related_name = 'book_readers')
    cover = models.ImageField(upload_to='book_covers/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title
