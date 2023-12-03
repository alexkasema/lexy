from . models import Product, Category, Vendor, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address



def default(request):
    categories = Category.objects.all()

    try:
        address = Address.objects.get(user=request.user)
    except:
        address = None

    return {
        'categories': categories, 'address': address
    }