from django.urls import path

from .views import FoodView

urlpatterns = [
    path('', FoodView.as_view(), name='food'),
    path('category/<int:category_id>/', FoodView.as_view(), name='category'),
]
