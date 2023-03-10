from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from hitcount.views import HitCountDetailView

from blog.models import Blog

from .forms import CommentForm
from .models import (Basket, BestProduct, Category, Comment, CommentsHome,
                     Products, ProductsImage, Slider)


class HomeView(TemplateView):
    template_name = 'food/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['sliders'] = Slider.objects.all()
        context['products'] = Products.objects.all().order_by('-id')[:8]
        context['best_products'] = BestProduct.objects.order_by('-id')[:1]
        context['comments_home'] = CommentsHome.objects.all()
        context['blogs'] = Blog.objects.all().order_by('-id')[:3]
        if self.request.user.is_authenticated:
            context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context


class FoodView(ListView):
    model = Products
    template_name = 'food/shop-page.html'
    context_object_name = 'products'
    paginate_by = 9
    ordering = '-id'

    def get_queryset(self):
        queryset = super(FoodView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(FoodView, self).get_context_data()
        context['categories'] = Category.objects.all()
        if self.request.user.is_authenticated:
            context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context


class ProductsView(HitCountDetailView):
    model = Products
    slug_url_kwarg = 'product'
    template_name = 'food/product-details.html'
    context_object_name = 'product'
    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            product_name = self.get_object()
            form.instance.user = request.user
            form.instance.post = product_name
            form.save()
            return redirect(reverse('food:product_detail', kwargs={'product': product_name.slug}))

    def get_context_data(self, *args, **kwargs):
        context = super(ProductsView, self).get_context_data()
        product_slug = self.kwargs['product']
        product = get_object_or_404(Products, slug=product_slug)
        context['photos'] = ProductsImage.objects.filter(products=product)
        context['comments'] = Comment.objects.filter(post__slug=self.kwargs['product'])
        context['form'] = self.form
        context['recent_products'] = Products.objects.all().order_by('title')[:4]
        if self.request.user.is_authenticated:
            context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context


class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'food/cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context


@login_required
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        baskets = baskets.first()
        baskets.quantity += 1
        baskets.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
