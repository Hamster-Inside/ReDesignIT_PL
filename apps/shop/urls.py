from django.urls import path
from .views import ShopHomeView

urlpatterns = [
    path('shop/', ShopHomeView.as_view(), name='shop'),
]
