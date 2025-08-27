from django.urls import path
from .views import list_products, product_detail, update_stock, create_product, login_view, logout_view

urlpatterns = [
    path("products/", list_products, name="list_products"),
    path("products/<int:id>/",product_detail, name = "product_detail"),
    path("products/<int:id>/update_stock/", update_stock, name="update_stock"),
    path("products/create/", create_product, name="create_product"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
