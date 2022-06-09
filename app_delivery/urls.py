from django.urls import path

from app_delivery.views import DeliveryCreate, DeliveryListView

urlpatterns = [
    path('create/', DeliveryCreate.as_view(), name='delivery_create_url'),
    path('', DeliveryListView.as_view(), name='delivery_list_url'),
]
