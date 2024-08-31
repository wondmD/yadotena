from django import forms
from .models import Product, Sell, Expense

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']

class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ['Product', 'quantity']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount']