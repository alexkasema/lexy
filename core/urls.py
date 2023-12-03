
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

]