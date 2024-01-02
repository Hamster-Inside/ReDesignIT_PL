from django.urls import path
from .views import ShopHomeView, CategoryDetailView

urlpatterns = [
    path('shop/', ShopHomeView.as_view(), name='shop'),
    path('shop/categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
]
