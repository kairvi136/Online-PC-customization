from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import Product, Category
from cart.views import _cart_id
from cart.models import CartItem
from .models import ReviewRating
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderProduct
from .models import ProductGallery



def index(request):
    # products = Product.objects.all().filter(is_available=True)
    
    # context = {
    #     'products' : products,
    # }
    return render(request, 'shop/shop/index.html')

def Gaming_chair(request):
  
    return render(request, 'shop/shop/Gaming_chair.html')

def Processor(request):
  
    return render(request, 'shop/shop/Processor.html')

def Mouse(request):
  
    return render(request, 'shop/shop/Mouse.html')

def Monitor(request):
  
    return render(request, 'shop/shop/Monitor.html')

def Motherboard(request):
  
    return render(request, 'shop/shop/Motherboard.html')    


def SSD(request):
  
    return render(request, 'shop/shop/SSD.html')

def Keyboard(request):
  
    return render(request, 'shop/shop/shop.html')

def Graphics_card(request):
  
    return render(request, 'shop/shop/Graphics_card.html')

def Storage(request):
  
    return render(request, 'shop/shop/Storage.html')

def Mouse_pad(request):
  
    return render(request, 'shop/shop/Mouse_pad.html')

def Glass_cleaner(request):
  
    return render(request, 'shop/shop/Glass_cleaner.html')




def Earphone(request):
  
    return render(request, 'shop/shop/Earphone.html')

def Laptop(request):
  
    return render(request, 'shop/shop/Laptop.html')

def Laptop_stand(request):
  
    return render(request, 'shop/shop/Laptop_stand.html')


def shop(request, category_slug=None):
    categories = None
    products = None
    

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
        
    else:
        products = Product.objects.all().filter(is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
        
    
    for product in products:
        reviews = ReviewRating.objects.order_by('-updated_at').filter(product_id=product.id, status=True)

    context = {
        'category_slug': category_slug,
        'products' : paged_products,
        'products_count': products_count,
        
    }
    return render(request, 'shop/shop/shop.html', context)


def product_details(request, category_slug, product_details_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_details_slug)
        
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        return e

    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None

    reviews = ReviewRating.objects.order_by('-updated_at').filter(product_id=single_product.id, status=True)
    product_gallery = ProductGallery.objects.filter(product_id=single_product.id)

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        'orderproduct':orderproduct,
        'reviews': reviews,
        'product_gallery':product_gallery,
    }
    return render(request, 'shop/shop/product_details.html', context)


def search(request):
    products_count = 0
    products = None
    paged_products = None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword :
            products = Product.objects.filter(Q(description__icontains=keyword) | Q(name__icontains=keyword))
            
            products_count = products.count()
            
    
    context = {
        'products': products,
        'products_count': products_count,
    }
    return render(request, 'shop/shop/search.html', context)



def review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id,product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you, your review updated!')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you, your review Posted!')
                return redirect(url)

def gaming_chair(request):
  
    return redirect(request, 'shop/accounts/dashboard/dashboard.html')