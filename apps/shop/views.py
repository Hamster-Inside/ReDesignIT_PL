from django.views.generic import ListView, DetailView
from .models import Category, Product


class ShopHomeView(ListView):
    model = Category
    template_name = 'shop_index.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        descendants = category.get_descendants(include_self=True)
        context['products'] = Product.objects.filter(category__in=descendants)
        return context
