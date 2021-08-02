from django.shortcuts import render, redirect, get_object_or_404

from product.forms import CreateProductForm, UpdateProductForm
from product.models import Category, Product

from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required()
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')







#
# def  home_page(request):
#     categories = Category.objects.all()
#     print(categories)
#     #select * from category
#     return render(request, 'product/home.html', {'categories': categories})
#
#
# def product_list(request, slug):
#     products = Product.objects.filter(category__slug=slug)
#     return render(request, 'product/list.html', locals())
#
#
# def product_detail(request, id):
#     product = Product.objects.get(id=id)
#     # print(product)
#     return render(request, 'product/detail.html', {'product': product})
#
#
#
# def create_product(request):
#     if request.method == 'POST':
#         product_form = CreateProductForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product = product_form.save()
#             return redirect(product.get_absolute_url())
#     else:
#         product_form = CreateProductForm()
#     return render(request, 'product/create_product.html', {'product_form': product_form})
#
# def update_product(request, id):
#     product = get_object_or_404(Product, pk=id)
#     product_form = UpdateProductForm(request.POST or None, request.FILES or None, instance=product)
#
#     if product_form.is_valid():
#         product_form.save()
#         return redirect(product.get_absolute_url())
#     return render(request, 'product/update_product.html', {'product_form': product_form})
#
# def delete_product(request, id):
#     product = get_object_or_404(Product, pk=id)
#     if request.method == 'POST':
#         slug = product.category.slug
#         product.delete()
#         return redirect('list', slug)
#     return render(request, 'product/delete_product.html', {'product': product})
