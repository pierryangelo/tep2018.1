from django.urls import path

from . import views

urlpatterns = [
    path(r'users/', views.UserList.as_view(), name='user-list'),
    path(r'user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path(r'user/<int:pk>/posts', views.UserPostList.as_view(), name='user-post-list'),
    path(r'user/<int:pk>/post/<int:post_pk>/', views.UserPostDetail.as_view(), name='user-post-detail'),
    path(r'user/<int:pk>/addresses', views.UserAddressList.as_view(), name='user-address-list'),
    path(r'user/<int:pk>/address/<int:address_pk>/', views.UserAddressDetail.as_view(), name='user-address-detail'),
    path(r'posts/', views.PostList.as_view(), name='post-list'),
    path(r'post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path(r'comments/', views.CommentList.as_view(), name='comment-list'),
    path(r'comment/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path(r'addresses/', views.AddressList.as_view(), name='address-list'),
    path(r'address/<int:pk>/', views.AddressDetail.as_view(), name='address-detail'),

]
