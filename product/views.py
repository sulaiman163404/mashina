from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from .models import *



class SearchListView(ListView):
    model = Product  # Product.objects.all()
    template_name = 'product/search.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if not q:
            return Product.objects.none()
        queryset = queryset.filter(Q(name__icontains=q) | Q(description__icontains=q))
        return queryset

class CategorylistView(ListView):
    model = Category #Category.objects.all()
    template_name = 'index.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = Product #Product.objects.all()
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        queryset = queryset.filter(category__slug=slug)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs.get('slug')
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'

class ProfileView(DetailView):
    model = User
    template_name = 'product/profile.html'
    context_object_name = 'profile'


class IsAdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

class AddReview(IsAdminCheckMixin, ListView):
    model = Reviews
    template_name = 'product/review.html'
    form_class = ReviewForm
    context_object_name = 'review'


class ProductCreateView(IsAdminCheckMixin, CreateView):
    model = Product
    template_name = 'product/create_product.html'
    form_class = CreateProductForm
    context_object_name = 'product_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context

class ProductUpdateView(IsAdminCheckMixin, UpdateView):
    model = Product
    template_name = 'product/update_product.html'
    form_class = UpdateProductForm
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context

class ProductDeleteView(IsAdminCheckMixin, DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('home')



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


