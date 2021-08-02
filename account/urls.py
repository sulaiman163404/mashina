from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import RegisterView, SignInView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]