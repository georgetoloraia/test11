from django.contrib import admin
from .models import Blog, Category



# Register your models with the customized admin classes
admin.site.register(Blog)
admin.site.register(Category)
