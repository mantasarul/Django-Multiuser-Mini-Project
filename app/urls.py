from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.CartList.as_view(), name='home'),
    path('login', views.CustomLogin.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
]
