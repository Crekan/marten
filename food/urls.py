from django.urls import path

from .views import FoodView, ProductsView

app_name = 'food'

urlpatterns = [
    path('', FoodView.as_view(), name='food'),
    path('category/<int:category_id>/', FoodView.as_view(), name='category'),
    path('product/<slug:product>/', ProductsView.as_view(), name='product_detail'),
]
