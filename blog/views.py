from django.views.generic import ListView
from hitcount.views import HitCountDetailView

from blog.models import Blog


class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    paginate_by = 6


class BlogDetailView(HitCountDetailView):
    model = Blog
    slug_url_kwarg = 'blog'
    template_name = 'blog/blog-details.html'
    context_object_name = 'blog'
