from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from hitcount.views import HitCountDetailView

from blog.models import Blog, BlogImage


class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    paginate_by = 6
    ordering = '-id'


class BlogDetailView(HitCountDetailView):
    model = Blog
    slug_url_kwarg = 'blog'
    template_name = 'blog/blog-details.html'
    context_object_name = 'blog'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data()
        blog_slug = self.kwargs['blog']
        blog = get_object_or_404(Blog, slug=blog_slug)
        context['photos'] = BlogImage.objects.filter(blog=blog).order_by('-id')[:2]
        return context
