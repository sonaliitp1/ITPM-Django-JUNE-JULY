from django.shortcuts import get_object_or_404, render,redirect

from store.models import Category, Product,Cart
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request,'home.html',{'products':products,'categories':categories})

def category_products(request, id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {
        'products': products,
        'categories': categories,
        'category': category
    })
    

@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("cart") 

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

