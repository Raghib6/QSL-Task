from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("products/<slug:slug>/", views.products, name="products"),
]
