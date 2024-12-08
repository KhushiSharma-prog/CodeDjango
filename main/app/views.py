from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Subcategory, ChildCategory, ProductCategory
from .forms import CategoryForm, SubcategoryForm, ChildCategoryForm, ProductCategoryForm
from .models import DBdata
from django.contrib import messages
from django.contrib.auth import authenticate, login


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})

def subcategory_list(request):
    subcategories = Subcategory.objects.select_related('category')
    return render(request, 'subcategory_list.html', {'subcategories': subcategories})

def subcategory_create(request):
    form = SubcategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('subcategory_list')
    return render(request, 'subcategory_form.html', {'form': form})

def subcategory_update(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    form = SubcategoryForm(request.POST or None, instance=subcategory)
    if form.is_valid():
        form.save()
        return redirect('subcategory_list')
    return render(request, 'subcategory_form.html', {'form': form})

def subcategory_delete(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        subcategory.delete()
        return redirect('subcategory_list')
    return render(request, 'subcategory_confirm_delete.html', {'subcategory': subcategory})

def childcategory_list(request):
    
    childcategories = ChildCategory.objects.select_related('category', 'subcategory')
    return render(request, 'childcategory_list.html', {'childcategories': childcategories})

def childcategory_create(request):
    form = ChildCategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('childcategory_list')
    
    return render(request, 'childcategory_form.html', {'form': form})

def childcategory_update(request, pk):
    childcategory = get_object_or_404(ChildCategory, pk=pk)
    form = ChildCategoryForm(request.POST or None, instance=childcategory)
    if form.is_valid():
        form.save()
        return redirect('childcategory_list')
    return render(request, 'childcategory_form.html', {'form': form})

def childcategory_delete(request, pk):
    childcategory = get_object_or_404(ChildCategory, pk=pk)
    if request.method == 'POST':
        childcategory.delete()
        return redirect('childcategory_list')
    return render(request, 'childcategory_confirm_delete.html', {'childcategory': childcategory})


def product_list(request):
    productcategories = ProductCategory.objects.select_related('category', 'subcategory', 'childcategory')
    return render(request, 'product_list.html', {'productcategories': productcategories})

def product_create(request):
    
    # form = ProductCategoryForm(request.POST or None)
    form = ProductCategoryForm(request.POST, request.FILES)  # Include `request.FILES` for file uploads
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product.html', {'form': form})

def productcategory_update(request, pk):
    productcategory = get_object_or_404(ProductCategory, pk=pk)
    form = ProductCategoryForm(request.POST or None, instance=productcategory)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product.html', {'form': form})

def productcategory_delete(request, pk):
    productcategory = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        productcategory.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'productcategory': productcategory})

def fetch_subcategories(request):
    category_id = request.GET.get('category_id')
    print(category_id)
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)


