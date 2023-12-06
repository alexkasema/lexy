from . models import Product, Category, Vendor, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address
from django.db.models import Min, Max


def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    min_max_price = Product.objects.aggregate(Min("price"), Max("price"))

    try:
        address = Address.objects.get(user=request.user)
    except:
        address = None

    return {
        'categories': categories, 'address': address, 'vendors': vendors, 'min_max_price': min_max_price
    }