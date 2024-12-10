from django import forms
from .models import Category, Subcategory, ChildCategory, ProductCategory, User
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password',]

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise ValidationError("Passwords do not match")
        return password2