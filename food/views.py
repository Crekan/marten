from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView

from blog.models import Blog

from .models import (BestProduct, Category, CommentsHome, Products,
                     Slider, ProductsImage)


class HomeView(TemplateView):
    template_name = 'food/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['sliders'] = Slider.objects.all()
        context['products'] = Products.objects.all().order_by('-id')[:8]
        context['best_products'] = BestProduct.objects.order_by('-id')[:1]
        context['comments_home'] = CommentsHome.objects.all()
        context['blogs'] = Blog.objects.all().order_by('-id')[:3]
        return context


class FoodView(ListView):
    model = Products
    template_name = 'food/shop-page.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        queryset = super(FoodView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(FoodView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductsView(DetailView):
    model = Products
    slug_url_kwarg = 'product'
    template_name = 'food/product-details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data()
        product = get_object_or_404(Products, slug=self.kwargs['product'])
        context['photos'] = ProductsImage.objects.filter(products=product)
        return context
