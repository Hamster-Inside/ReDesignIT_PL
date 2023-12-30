from django.shortcuts import render
from django.views.generic import TemplateView


class ShopHomeView(TemplateView):
    template_name = 'shop_index.html'
