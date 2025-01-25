from django.urls import path
from orders import views


urlpatterns = [
    path('menu/', views.menu_view, name='menu'),
    path('cart/', views.view_cart, name='cart'),
    path('cart/add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/checkout/', views.place_order, name='place_order'),
    path('orders/', views.order_history, name='orders'),
]
