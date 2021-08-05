from django.contrib.auth.models import User
from django.contrib.auth.views import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

    def post(self, *args, **kwargs):
        data = self.request.POST
        User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
        return redirect(self.success_url)

class SignInView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')
