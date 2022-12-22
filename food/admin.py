from django.contrib import admin

from .models import (BestProduct, Brand, Category, CommentsHome, Products,
                     Slider, Color, Availability)

admin.site.register(Slider)
admin.site.register(Products)
admin.site.register(BestProduct)
admin.site.register(CommentsHome)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Availability)
