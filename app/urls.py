from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # path('', views.AddCart.as_view(), name='add_cart'),
    path('', views.CartList.as_view(), name='home'),
    path('login', views.CustomLogin.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register', views.RegisterPage.as_view(), name='register'),
]
