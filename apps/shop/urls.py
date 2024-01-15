from django.urls import path
from .views import ShopHomeView, CategoryDetailView, ProductDetailView

urlpatterns = [
    path('shop/', ShopHomeView.as_view(), name='shop'),
    path('shop/categories/<slug:slug>/',
         CategoryDetailView.as_view(),
         name='category_detail'),
    path('shop/categories/<slug:category_slug>/<slug:product_slug>/',
         ProductDetailView.as_view(),
         name='product_detail'),
]
