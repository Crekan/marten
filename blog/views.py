from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView
from hitcount.views import HitCountDetailView

from blog.models import Blog, BlogImage, Comment
from food.models import Basket
from .forms import CommentForm


class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    paginate_by = 6
    ordering = '-id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogView, self).get_context_data()
        if self.request.user.is_authenticated:
            context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context


class BlogDetailView(HitCountDetailView):
    model = Blog
    slug_url_kwarg = 'blog'
    template_name = 'blog/blog-details.html'
    context_object_name = 'blog'
    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            blog_name = self.get_object()
            form.instance.user = request.user
            form.instance.blog = blog_name
            form.save()
            return redirect(reverse('blog:detail_blog', kwargs={'blog': blog_name.slug}))

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data()
        blog_slug = self.kwargs['blog']
        blog = get_object_or_404(Blog, slug=blog_slug)
        context['photos'] = BlogImage.objects.filter(blog=blog).order_by('-id')[:2]
        context['form'] = self.form
        context['comments'] = Comment.objects.filter(blog__slug=self.kwargs['blog'])
        if self.request.user.is_authenticated:
            context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context
