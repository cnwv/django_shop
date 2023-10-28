from django.contrib import admin

from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'is_active')
    fields = ('name', ('price', 'quantity',), 'image', 'description', 'short_description', 'category', 'is_active')
    search_fields = ('name', 'category__name')