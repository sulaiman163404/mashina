from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import *
from product.views import ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]