
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    #! product
    path('products', views.product_list_view, name="products"),
    path('product/<pid>', views.product_details_view, name="product"),


    #! category
    path('categories', views.category_list_view, name="categories"),
    path('category/<cid>', views.category_product_list_view, name="category"),

    #! vendor
    path('vendors', views.vendors_list_view, name="vendors"),
    path('vendor/<vid>', views.vendor_details_view, name="vendor"),

    #! tags
    path('products/tags/<slug:tag_slug>', views.tag_list_view, name="tags"),

    #! add reviews
    path('reviews/<pid>', views.review_form_view, name="reviews"),

    #! Search by product title
    path('search/', views.search_products_view, name="search_products"),

    #! filter products by category, vendor
    path('filter_products/', views.filter_products_view, name="filter_products"),

    #! add product to cart
    path('add_to_cart', views.add_to_cart, name="add_to_cart"),

    #! cart page
    path('cart', views.cart_view, name="cart"),

    #! delete-item-from-cart
    path('delete-from-cart', views.delete_item_from_cart, name="delete-from-cart"),

]