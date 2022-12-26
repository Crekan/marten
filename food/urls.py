from django.urls import path

from .views import CartView, FoodView, ProductsView, basket_add, basket_remove

app_name = 'food'

urlpatterns = [
    path('', FoodView.as_view(), name='food'),
    path('category/<int:category_id>/', FoodView.as_view(), name='category'),
    path('product/<slug:product>/', ProductsView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
