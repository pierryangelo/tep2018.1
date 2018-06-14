from django.urls import path

from . import views

urlpatterns = [
    path(r'users/',
         views.UserList.as_view(), name='user-list'),
    path(r'user/<int:pk>/',
         views.UserDetail.as_view(), name='user-detail'),
    path(r'user/<int:pk>/posts',
         views.UserPostList.as_view(), name='user-post-list'),
    path(r'user/<int:pk>/post/<int:post_pk>/',
         views.UserPostDetail.as_view(), name='user-post-detail'),
    path(r'user/<int:pk>/addresses',
         views.UserAddressList.as_view(), name='user-address-list'),
    path(r'user/<int:pk>/address/<int:address_pk>/',
         views.UserAddressDetail.as_view(), name='user-address-detail'),
    path(r'user/<int:pk>/post/<int:post_pk>/comments',
         views.UserPostCommentList.as_view(), name='user-post-comment-list'),
    path(r'user/<int:pk>/post/<int:post_pk>/comment/<int:comment_pk>',
         views.UserPostCommentDetail.as_view(), name='user-post-comment-detail'),
    path(r'user-comments/', views.UserPostTotalCommentList.as_view(), name='user-comment'),
    path(r'user-comment/<int:pk>/', views.UserPostTotalCommentDetail.as_view(), name='user-comment-detail'),
    path(r'users-summaries/', views.UserSummaryList.as_view(), name='user-summary-list'),
    path(r'user-summary/<int:pk>/', views.UserSummaryDetail.as_view(), name='user-summary-detail'),

]
