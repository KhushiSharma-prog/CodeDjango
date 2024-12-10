from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Subcategory, ChildCategory, ProductCategory
from .forms import CategoryForm, SubcategoryForm, ChildCategoryForm, RegisterForm
from .models import DBdata
from django.contrib import messages
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import ProductCategory
from .serializers import ProductCategorySerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated







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


def register1(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create the new user
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Show a success message and redirect
            messages.success(request, "Your account has been created successfully!")
            return redirect('login')  # Redirect to login page after successful registration
        else:
            # If the form is invalid, show the errors
            messages.error(request, "There was an error with your registration. Please try again.")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
# def product_create(request):

#     if request.method == 'POST':

#         form = ProductCategoryForm(request.POST, request.FILES)

#         if form.is_valid():

#             form.save()

#             return redirect('product_list')

#     else:

#         form = ProductCategoryForm()

#     return render(request, 'product.html', {'form': form})
 
# def product_update(request, pk):

#     product_category = get_object_or_404(ProductCategory, pk=pk)

#     form = ProductCategoryForm(request.POST or None, request.FILES or None, instance=product_category)

#     if form.is_valid():

#         form.save()

#         return redirect('product_list')

#     return render(request, 'product.html', {'form': form})


# def productcategory_delete(request, pk):
#     productcategory = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         productcategory.delete()
#         return redirect('product_list')
#     return render(request, 'product_confirm_delete.html', {'productcategory': productcategory})

# List API View
# @api_view(['GET'])
# def product_list(request):
#     """ Retrieve a list of all product categories """
#     productcategories = ProductCategory.objects.all()
#     serializer = ProductCategorySerializer(productcategories, many=True)
#     return Response(serializer.data)

# Create API View
@api_view(['POST'])
def product_create(request):
    """ Create a new product category """
    if request.method == 'POST':
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update API View
@api_view(['PUT'])
def product_update(request, pk):
    """ Update an existing product category """
    product_category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'PUT':
        serializer = ProductCategorySerializer(product_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete API View
@api_view(['DELETE'])
def product_delete(request, pk):
    """ Delete a product category """
    product_category = get_object_or_404(ProductCategory, pk=pk)
    
    if request.method == 'DELETE':
        product_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def fetch_subcategories(request):
    category_id = request.GET.get('category_id')
    print(category_id)
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)

def fetch_childcategories(request):
    subcategory_id = request.GET.get('subcategory_id')
    child_categories = ChildCategory.objects.filter(subcategory_id=subcategory_id).values('id', 'name')
    return JsonResponse(list(child_categories), safe=False)


def toggle_product_status(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')  # Get product ID from the POST data
        current_status = request.POST.get('current_status') == 'true'  # Convert string to boolean

        product = get_object_or_404(ProductCategory, id=product_id)

        # Toggle the status (if it's active, make it inactive, and vice versa)
        new_status = not current_status
        product.is_active = new_status
        product.save()

        return JsonResponse({'success': True, 'new_status': new_status})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'User registered successfully',
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login View using JWT tokens
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'access': access_token,
                'refresh': refresh_token
            }, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# Protected View requiring authentication
@api_view(['GET'])
def protected_view(request):
    # Only accessible if the user is authenticated
    return Response({"message": "This is a protected view"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Only authenticated users can access
def protected_view(request):
    return Response({"message": "This is a protected view"}, status=status.HTTP_200_OK)



