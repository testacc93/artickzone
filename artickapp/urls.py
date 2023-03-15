from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('products/<str:prodname>', views.singleproduct),

    path('about/', views.about),
    path('contact/', views.contact),
]