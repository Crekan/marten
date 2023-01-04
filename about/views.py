from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Cards, Statistics, Team
from food.models import CommentsHome


def about(request):
    return render(request, 'about/about-us.html')


class AboutView(TemplateView):
    template_name = 'about/about-us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data()
        context['comments_home'] = CommentsHome.objects.all()
        context['cards'] = Cards.objects.all().order_by('-id')[:1]
        context['statistics'] = Statistics.objects.all()
        context['team'] = Team.objects.all().order_by('-id')[:4]
        return context
