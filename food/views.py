from django.views.generic import TemplateView

from .models import Slider


class HomeView(TemplateView):
    template_name = 'food/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['sliders'] = Slider.objects.all()
        return context
