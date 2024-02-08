from django.contrib import admin

from apps.products.models import Product, ProductImages


class ProductImageInline(admin.TabularInline):
    model = ProductImages
    extra = 1


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['category']
    search_fields = ['title']
    inlines = [ProductImageInline]
