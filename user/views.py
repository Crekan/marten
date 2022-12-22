from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserLoginForm, UserRegistrationForm


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm


class UserRegistrationView(CreateView):
    model = User
    template_name = 'user/registrations.html'
    success_url = reverse_lazy('authorization')
    form_class = UserRegistrationForm


def profile(request):
    return render(request, 'user/my-account.html')
