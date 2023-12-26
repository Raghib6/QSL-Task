import django_filters
from django import forms
from .models import Product, Seller, Brand, Category, Warranty


class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    seller = django_filters.ModelMultipleChoiceFilter(
        field_name="seller__slug",
        to_field_name="slug",
        queryset=Seller.objects.all().order_by("name"),
        widget=forms.CheckboxSelectMultiple,
    )
    category = django_filters.ModelMultipleChoiceFilter(
        field_name="category__slug",
        to_field_name="slug",
        queryset=Category.objects.filter(parent__isnull=False).order_by("name"),
        widget=forms.CheckboxSelectMultiple,
    )
    brand = django_filters.ModelMultipleChoiceFilter(
        field_name="brand__slug",
        to_field_name="slug",
        queryset=Brand.objects.all().order_by("name"),
        widget=forms.CheckboxSelectMultiple,
    )

    warranty = django_filters.ModelMultipleChoiceFilter(
        field_name="warranty__slug",
        to_field_name="slug",
        queryset=Warranty.objects.all().order_by("created_at"),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Product
        fields = ["category", "seller", "brand", "warranty"]
