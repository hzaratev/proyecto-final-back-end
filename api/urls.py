from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('users/<int:user_id>', views.UserView.as_view(), name='id-users'),
    path('users/', views.UserView.as_view(), name='all-users'),
    path('products/', views.ProductView.as_view(), name='all-products'),
    path('profiles/', views.ProfileView.as_view(), name='all-profiles'),
]