from django.views.generic import TemplateView

from .models import Slider, Products, BestProduct


class HomeView(TemplateView):
    template_name = 'food/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['sliders'] = Slider.objects.all()
        context['products'] = Products.objects.all().order_by('-id')[:8]
        context['best_products'] = BestProduct.objects.order_by('-id')[:1]
        return context
