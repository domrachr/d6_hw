from django.contrib import admin
from p_library.models import Book, Author, Publisher, Reader
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('author', 'year_release')

    list_display = ('title', 'author',)
    # fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass    