
from django.urls import path, include

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

    #! update cart
    path('update-cart', views.update_cart, name="update-cart"),

    #! Checkout url
    path('checkout', views.checkout_view, name="checkout"),

    #! paypal url
    path('paypal/', include('paypal.standard.ipn.urls')),

    #! payment completed url
    path('payment-completed', views.payment_completed_view, name="payment-completed"),

    #! payment failed url
    path('payment-failed', views.payment_failed_view, name="payment-failed"),

     #! dashboard url
    path('dashboard/', views.dashboard_view, name="dashboard"),

     #! order details url
    path('dashboard/order/<int:id>', views.order_detail_view, name="order-details"),

    #! making address default url
    path('make-default-address', views.make_address_default_view, name="make-default-address"),

]