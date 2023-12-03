from django.shortcuts import render

from . models import Product, Category, Vendor, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address


# Create your views here.

def index(request):
    #! products = Product.objects.all().order_by('-id')
    products = Product.objects.filter(product_status = "published", featured=True).order_by('id')

    context = {
        'products': products
    }
    return render(request, 'core/index.html', context)

def product_list_view(request):

    products = Product.objects.filter(product_status = "published", featured=True).order_by('id')
    categories = Category.objects.all()

    context = {
        'products': products, 'categories': categories
    }
    return render(request, 'core/product_list.html', context)

def product_details_view(request, pid):

    product = Product.objects.get(pid=pid)
    products = Product.objects.filter(category=product.category).exclude(pid=pid)[:4]
    p_image = product.p_images.all()

    context = {
        'product': product, 'p_image': p_image, 'products': products
    }

    return render(request, 'core/product_details.html', context)

def category_list_view(request):

    categories = Category.objects.all()

    context = {'categories': categories}
    return render(request, 'core/category_list.html', context)

def category_product_list_view(request, cid):

    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status = "published", category=category)

    context = {
        'category': category, 'products': products
    }

    return render(request, 'core/category_product_list.html', context)

def vendors_list_view(request):

    vendors = Vendor.objects.all()

    context = {
        'vendors': vendors
    }
    return render(request, 'core/vendors_list.html', context)

def vendor_details_view(request, vid):

    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status = "published")

    context = {
        'vendor': vendor, 'products': products
    }
    return render(request, 'core/vendor_details.html', context)