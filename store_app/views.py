from django.shortcuts import render
from .models import Category, Product
from .filters import ProductFilter


# Create your views here.
def index(request):
    categories = Category.objects.filter(parent__isnull=True)
    context = {"categories": categories}
    return render(request, "index.html", context)


def products(request, slug):
    categories = Category.objects.filter(parent__isnull=True)
    subcategories = Category.objects.filter(parent__slug=slug)

    filter = ProductFilter(
        request.GET,
        queryset=Product.objects.filter(category__parent__slug=slug),
    )
    filter.form.fields["category"].queryset = subcategories
    context = {
        "form": filter.form,
        "products": filter.qs,
        "categories": categories,
        "subcategories": subcategories,
        "slug": slug,
    }

    return render(request, "products.html", context)
