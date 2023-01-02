from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from blog.models import Blog


def blog(request):
    return render(request, 'blog/blog.html')


class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    paginate_by = 6


