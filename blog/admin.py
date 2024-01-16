from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'author')  # Fields to be displayed in the model list page
    search_fields = ['title', 'description']  # Fields to be searched
    list_filter = ('publish_date', 'categories')  # Filters to be applied

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'text_color', 'background_color')
    search_fields = ['title']

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)