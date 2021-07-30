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
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)


class CustomLogin(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    # success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')


# class AddCart(LoginRequiredMixin, CreateView):
#     model = Cart
#     form_class = CartForm
#     template_name = 'cart.html'
#     success_url = reverse_lazy('add_cart')


class CartList(LoginRequiredMixin, CreateView, ListView):
    template_name = 'cart.html'
    model = Cart
    form_class = CartForm
    success_url = reverse_lazy('home')
    context_object_name = 'cart_item'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CartList, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_item'] = context['cart_item'].filter(user=self.request.user)

        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['cart_item'] = context['cart_item'].filter(item__contains=search_input)

        context['search_input'] = search_input

        return context
