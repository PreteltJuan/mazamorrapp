from django import forms
from .models import Order

class OrderRequest(forms.ModelForm):

    class Meta:
        model = Order
        fields = ["name","amount","address","time"]
        
        
        