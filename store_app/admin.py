from django.contrib import admin
from store_app.models import Brand, Seller, Category, Warranty, Product


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "created_at"]
    search_fields = ["name"]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "created_at"]
    search_fields = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "parent", "created_at"]
    search_fields = ["name"]


@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "created_at"]
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["category"]
    search_fields = ["name", "category__name"]
    list_display = ["name", "brand", "category", "price", "seller", "warranty"]
