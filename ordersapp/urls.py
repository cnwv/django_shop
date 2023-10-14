from django.urls import path, re_path
from ordersapp import views

app_name='ordersapp'

urlpatterns = [
    path('', views.OrderList.as_view(), name='order_list'),
    path('create/', views.OrderItemsCreate.as_view(), name='order_create'),
    path('update/<int:pk>/', views.OrderItemsUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', views.OrderDelete.as_view(), name='order_delete'),
    path('detail/<int:pk>/', views.OrderRead.as_view(), name='order_detail'),
    path('forming/complete/<int:pk>/', views.order_forming_complete, name='order_complete'),
    re_path(r'^product/(?P<pk>\d+)/price/$', views.get_product_price),
]
