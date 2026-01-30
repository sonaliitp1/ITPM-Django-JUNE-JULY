from django.shortcuts import get_object_or_404, render

from store.models import Category, Product

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
    