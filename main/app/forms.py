from django import forms
from .models import Category, Subcategory, ChildCategory, ProductCategory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']

class ChildCategoryForm(forms.ModelForm):
    class Meta:
        model = ChildCategory
        fields = ['name', 'category', 'subcategory']        

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['title', 'category', 'subcategory' , 'childcategory' , 'price' , 'quantity' , 'image' , 'description']
