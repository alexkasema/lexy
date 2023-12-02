from . models import Product, Category, Vendor, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address



def default(request):
    categories = Category.objects.all()

    return {
        'categories': categories,
    }