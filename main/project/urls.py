from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.category_list, name='category_list'),
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


    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/update/<int:pk>/', views.productcategory_update, name='productcategory_update'),
    path('products/delete/<int:pk>/', views.productcategory_delete, name='productcategory_delete'),
    path('fetch-subcategories/', views.fetch_subcategories, name='fetch_subcategories'),
    path('upload/', views.product_create, name='product_create'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

