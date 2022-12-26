from django.contrib import admin

from .models import (Basket, BestProduct, Brand, Category, Length, Products,
                     ProductsImage, Slider)


class ProductsImageAdmin(admin.StackedInline):
    model = ProductsImage


class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = (['color'])
    inlines = [ProductsImageAdmin]


admin.site.register(Slider)
admin.site.register(Products, ProductsAdmin)
admin.site.register(BestProduct)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Length)
admin.site.register(Basket)
