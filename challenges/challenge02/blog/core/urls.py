from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.ApiRoot.as_view(),
         name=views.ApiRoot.name),

    path('users/',
         views.UserList.as_view(),
         name=views.UserList.name),

    path('user/<int:pk>/',
         views.UserDetail.as_view(),
         name=views.UserDetail.name),

    path('user/<int:pk>/posts/',
         views.PostList.as_view(),
         name=views.PostList.name),

    path('user/<int:pk>/post/<int:pk2>',
         views.PostDetail.as_view(),
         name=views.PostDetail.name),

    path('user/<int:pk>/address/<int:pk2/',
         views.AddressDetail.as_view(),
         name=views.AddressDetail.name),

    path('user/address/<int:pk>/',
         views.AddressDetail.as_view(),
         name=views.AddressDetail.name),

    path('user/comments/',
         views.CommentList.as_view(),
         name=views.CommentList.name),

    path('user/comment/<int:pk>/',
         views.CommentDetail.as_view(),
         name=views.CommentDetail.name)


]
