from django import forms
from django import forms
from . models import Cart

class CartForm(forms.ModelForm):
    
    class Meta:
        model = Cart
        fields = ("item",)