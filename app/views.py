from app.forms import CartForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy

from .models import Cart
from .forms import CartForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CustomLogin(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    # success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')


class CartList(CreateView, LoginRequiredMixin, ListView):
    template_name = 'cart.html'
    model = Cart
    form_class = CartForm
    success_url = reverse_lazy('home')

