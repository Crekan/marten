from django.urls import path

from .views import BlogDetailView, BlogView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('<slug:blog>/', BlogDetailView.as_view(), name='detail_blog'),
]
