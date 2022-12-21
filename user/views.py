from django.contrib.auth.views import LoginView

from .forms import UserLoginForm


class UserLoginView(LoginView):
    template_name = 'user/login-register.html'
    form_class = UserLoginForm
