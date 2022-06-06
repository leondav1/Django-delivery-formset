from django.urls import path

from app_delivery.views import DeliveryCreate, DeliveryListView, DeliveryDetail

urlpatterns = [
    path('delivery/create/', DeliveryCreate.as_view(), name='delivery_create_url'),
    path('delivery/', DeliveryListView.as_view(), name='delivery_list_url'),
    path('delivery/<int:pk>/', DeliveryDetail.as_view(), name='delivery_detail_url')
]
