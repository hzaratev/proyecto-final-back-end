from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('users/<int:user_id>', views.UserView.as_view(), name='id-users'),
    path('users/', views.UserView.as_view(), name='all-users'),
    path('products/', views.ProductView.as_view(), name='all-products'),
    path('profiles/', views.ProfileView.as_view(), name='all-profiles'),
    path('address/', views.AddressView.as_view(), name='all-address'),
    path('categories/', views.CategoryView.as_view(), name='all-categories'),
    path('likes/', views.LikeView.as_view(), name='all-likes'),
    path('notifications/', views.NotificationView.as_view(), name='all-notifications'),
    path('talks/', views.TalkView.as_view(), name='all-talks'),
]