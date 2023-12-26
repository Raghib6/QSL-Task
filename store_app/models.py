from django.db import models
from django.urls import reverse


class Seller(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, unique=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="child"
    )
    category_image = models.ImageField(upload_to="categories")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Warranty(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "warranty"
        verbose_name_plural = "warranties"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name="products", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name="all_products", on_delete=models.CASCADE
    )
    warranty = models.ForeignKey(
        Warranty, related_name="_products", on_delete=models.CASCADE
    )
    price = models.IntegerField()
    product_image = models.ImageField(upload_to="products")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
