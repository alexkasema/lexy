from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from django.template.loader import render_to_string

from . models import Product, Category, Vendor, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address
from taggit.models import Tag

from django.db.models import Avg

from . forms import ProductReviewForm

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

   
    reviews = ProductReview.objects.filter(product=product).order_by("-date")

    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    p_image = product.p_images.all()

    review_form = ProductReviewForm()

    make_review = True

    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()

        if user_review_count > 0:
            make_review = False

    context = {
        'product': product, 'p_image': p_image, 'products': products,
        'r': reviews, 'average_rating': average_rating, 'review_form': review_form,
        'make_review': make_review,
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

def tag_list_view(request, tag_slug=None):


    products = Product.objects.filter(product_status = "published").order_by("-id")

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context = {
        'products': products, 'tag': tag
    }

    return render(request, 'core/tag.html', context)

def review_form_view(request, pid):
    
    product = Product.objects.get(pid=pid)
    user = request.user

    review = ProductReview.objects.create(
        user = user,
        product = product,
        review = request.POST.get('review'),
        rating = request.POST.get('rating'),
    )

    context = {
        'user': user.username,
        'review': request.POST.get('review'),
        'rating': request.POST.get('rating'),
    }

    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    return JsonResponse(
        {
            'bool': True,
            'context': context,
            'average_reviews': average_reviews,
        }
    )

def search_products_view(request):

    query = request.GET.get("q")
    products = Product.objects.filter(title__icontains=query, product_status = "published").order_by("-date")

    #? products = Product.objects.filter(title__icontains=query, description__icontains=query).order_by("-date")

    context = {
        'products': products,
        'query': query
    }
    return render(request, 'core/search_products.html', context)

def filter_products_view(request):
    categories = request.GET.getlist("category[]")
    vendors = request.GET.getlist("vendor[]")

    min_price = request.GET['min_price']
    max_price = request.GET['max_price']

    products = Product.objects.filter(product_status="published").order_by("-id").distinct()

    products = products.filter(price__gte=min_price) #! product is greater than or equal to min_price
    products = products.filter(price__lte=max_price) #! product is less than or equal to max price

    if len(categories) > 0:
        products = products.filter(category__id__in=categories).distinct()

    if len(vendors) > 0:
        products = products.filter(vendor__id__in=vendors).distinct()

    data = render_to_string("core/async/products_list.html", {'products': products})

    return JsonResponse({'data': data})