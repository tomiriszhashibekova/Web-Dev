
from django.http.response import JsonResponse
from api.models import Product, Category
from django.http import Http404


def product_list(request):

    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe = 0)




def product_detail(request, product_id):

    try:
        product = Product.objects.get(id = product_id)
    except Product.DoesNotExist as e:
        raise Http404
    return JsonResponse(product.to_json())

def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=0)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id = category_id)
    except Category.DoesNotExist as e:
        raise Http404
    return JsonResponse(category.to_json())


def category_products(request, category_id):
    products = Product.objects.all()
    main_info = []
    for item in products:
        if item.category_id.id == category_id:
            main_info.append(item.to_json())
    return JsonResponse(main_info, safe = 0)
