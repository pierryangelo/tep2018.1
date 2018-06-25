from django.urls import path

from . import views

urlpatterns = [
    path(r'profiles/',
         views.ProfileList.as_view(), name='profile-list'),
    path(r'profile/<int:pk>/',
         views.ProfileDetail.as_view(), name='profile-detail'),
    path(r'profile/<int:pk>/posts',
         views.ProfilePostList.as_view(), name='profile-post-list'),
    path(r'profile/<int:pk>/post/<int:post_pk>/',
         views.ProfilePostDetail.as_view(), name='profile-post-detail'),
    path(r'profile/<int:pk>/addresses',
         views.ProfileAddressList.as_view(), name='profile-address-list'),
    path(r'profile/<int:pk>/address/<int:address_pk>/',
         views.ProfileAddressDetail.as_view(), name='profile-address-detail'),
    path(r'profile/<int:pk>/post/<int:post_pk>/comments',
         views.ProfilePostCommentList.as_view(), name='profile-post-comment-list'),
    path(r'profile/<int:pk>/post/<int:post_pk>/comment/<int:comment_pk>',
         views.ProfilePostCommentDetail.as_view(), name='profile-post-comment-detail'),
    path(r'profile-comments/', views.ProfilePostTotalCommentList.as_view(), name='profile-comment'),
    path(r'profile-comment/<int:pk>/', views.ProfilePostTotalCommentDetail.as_view(), name='profile-comment-detail'),
    path(r'profiles-summaries/', views.ProfileSummaryList.as_view(), name='profile-summary-list'),
    path(r'profile-summary/<int:pk>/', views.ProfileSummaryDetail.as_view(), name='profile-summary-detail'),
    path(r'api-token/', views.CustomAuthToken.as_view()),
]
