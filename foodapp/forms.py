from django import forms
from .models import Product, Category, PurchaseList, PurchaseDetail

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class PurchaseListForm(forms.ModelForm):
    class Meta:
        model = PurchaseList
        fields = ['purchase_date']

class PurchaseDetailForm(forms.ModelForm):
    class Meta:
        model = PurchaseDetail
        fields = ['product', 'product_cost']
