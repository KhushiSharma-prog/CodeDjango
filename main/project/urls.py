from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('category', views.category_list, name='category_list'),
    path('category/create/', views.category_create, name='category_create'),
    path('categories/update/<int:pk>/', views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    path('subcategories/', views.subcategory_list, name='subcategory_list'),
    path('subcategories/create/', views.subcategory_create, name='subcategory_create'),
    path('subcategories/update/<int:pk>/', views.subcategory_update, name='subcategory_update'),
    path('subcategories/delete/<int:pk>/', views.subcategory_delete, name='subcategory_delete'),

    path('childcategories/', views.childcategory_list, name='childcategory_list'),
    path('childcategories/create/', views.childcategory_create, name='childcategory_create'),
    path('childcategories/update/<int:pk>/', views.childcategory_update, name='childcategory_update'),
    path('childcategories/delete/<int:pk>/', views.childcategory_delete, name='childcategory_delete'),


    # path('products/', views.product_list, name='product_list'),
    # path('products/create/', views.product_create, name='product_create'),
    # path('products/update/<int:pk>/', views.product_update, name='product_update'),
    # path('products/delete/<int:pk>/', views.productcategory_delete, name='productcategory_delete'),
    
    # path('', include('products.urls')),  # Include the 'products' app URLs
    path('api/productcategories/', views.product_list, name='product_list'),
    path('api/productcategories/create/', views.product_create, name='product_create'),
    path('api/productcategories/<int:pk>/update/', views.product_update, name='product_update'),
    path('api/productcategories/<int:pk>/delete/', views.product_delete, name='product_delete'),

    path('fetch-subcategories/', views.fetch_subcategories, name='fetch_subcategories'),
    path('fetch_childcategories/',views.fetch_childcategories,name='fetch_childcategories'),
    path('toggle_product_status/', views.toggle_product_status, name='toggle_product_status'),
    
    path('', views.register1, name='register'),
    path('register/api/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('protected/', views.protected_view, name='protected_view'),
    


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
