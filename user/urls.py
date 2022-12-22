from django.urls import path

from .views import UserLoginView, UserRegistrationView, profile

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='authorization'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/', profile, name='profile'),
]
