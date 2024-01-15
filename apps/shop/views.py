from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Product


class ShopHomeView(ListView):
    model = Category
    template_name = 'shop_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        prepared_nodes = Category.objects.all()
        for category in prepared_nodes:
            category.indentation_range = range(category.level)
        context['nodes'] = prepared_nodes
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()

        # Needed for list of categories where user is
        breadcrumbs = []
        current_category = category
        while category:
            if current_category is None:
                break
            breadcrumbs.insert(0, current_category)
            current_category = current_category.parent
        context['breadcrumbs'] = breadcrumbs
        descendants = category.get_descendants(include_self=True)
        children = category.get_children()
        context['products'] = Product.objects.filter(category__in=descendants)
        context['category_children'] = children

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        category_slug = self.kwargs.get('category_slug')
        product_slug = self.kwargs.get('product_slug')
        category = get_object_or_404(Category, slug=category_slug)
        return get_object_or_404(Product, category=category, slug=product_slug)
