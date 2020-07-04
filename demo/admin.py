from django.contrib import admin

from .models import Book,BookNumber


#admin.site.register(Book)
admin.site.register(BookNumber)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #fields = ['title']
    list_display = ['id','title', 'description', 'is_published', 'price',]
    list_filter = ['is_published', 'title']
    search_fields = ['title', 'description', 'price']

