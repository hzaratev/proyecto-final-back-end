from django.contrib import admin

from .models import Product, User, Category


admin.site.register(Product)
admin.site.register(User)
admin.site.register(Category)