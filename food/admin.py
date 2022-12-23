from django.contrib import admin

from .models import (Availability, BestProduct, Brand, Category, Color,
                     CommentsHome, Length, Products, Size, Slider)


class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = (['color'])


admin.site.register(Slider)
admin.site.register(Products, ProductsAdmin)
admin.site.register(BestProduct)
admin.site.register(CommentsHome)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Availability)
admin.site.register(Size)
admin.site.register(Length)
