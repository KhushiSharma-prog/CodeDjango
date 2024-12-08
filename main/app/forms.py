from django import forms
from .models import Category, Subcategory, ChildCategory, ProductCategory
from .models import MyModel

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

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name', 'image']        

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['title', 'category', 'subcategory' , 'childcategory' , 'price' , 'quantity' , 'image' , 'description']
