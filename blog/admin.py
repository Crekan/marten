from django.contrib import admin

from .models import Blog, BlogImage


class BlogImageAdmin(admin.StackedInline):
    model = BlogImage


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [BlogImageAdmin]


admin.site.register(Blog, BlogAdmin)
