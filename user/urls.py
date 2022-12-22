from django.urls import path

from .views import (UserLoginView, UserLogoutView, UserProfileView,
                    UserRegistrationView)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='authorization'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
