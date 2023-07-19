from django.contrib import admin

from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    fields = ('name', ('price', 'quantity',), 'image', 'description', 'short_description', 'category')
    search_fields = ('name', 'category__name')