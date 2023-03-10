from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from food.models import Basket

from .forms import UserLoginForm, UserProfileForm, UserRegistrationForm


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm


class UserRegistrationView(CreateView):
    model = User
    template_name = 'user/registrations.html'
    success_url = reverse_lazy('authorization')
    form_class = UserRegistrationForm


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'user/my-account.html'
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('home'))
