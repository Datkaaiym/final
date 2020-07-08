from django.shortcuts import render
from products.models import *
 
# from django.core.paginator import Paginator

def product(request, product_id):
    product = Product.objects.get(id=product_id)


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    # paginator = Paginator(product, 2)
     
    # page_number = request.GET.get('page', 1)
    # page = paginator._get_page(page_number)

    return render(request, 'products/product.html', locals())

# def products_list(request):
#     products = Product.objects.all()
#     paginator = Paginator(product, 2)
    
#     page_number = request.GET.get('page', 1)
#     page = paginator._get_page(page_number)
#     return render(request, 'products/product.html', context={'products': page.object_list})